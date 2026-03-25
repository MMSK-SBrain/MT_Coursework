"""
Image Processor for Student Handout Generator

Validates, resizes, and optimizes images for dark-themed PDFs. Handles:
- Image validation (format, size, existence)
- Path resolution (relative/absolute, security)
- Image resizing (maintain aspect ratio)
- Dark theme optimization
- Placeholder generation for missing images

Usage:
    config = {"images": {"base_directory": "./images", "max_width": 500}}
    processor = ImageProcessor(config)
    processed = processor.process_images(image_references)
"""

import logging
import tempfile
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFont

from .models import ImageReference
from .security import SecurityValidator

logger = logging.getLogger(__name__)


class ImageProcessorError(Exception):
    """Base exception for image processing errors"""
    pass


class ImageProcessor:
    """
    Process images for embedding in PDF handouts.

    Features:
    - Validate image files (format, size, existence)
    - Resolve relative/absolute paths securely
    - Resize images to max width (maintain aspect ratio)
    - Optimize for dark backgrounds
    - Generate placeholders for missing images

    Configuration:
        images:
          base_directory: "./images"
          max_width: 500
          placeholder_on_missing: true
          placeholder_color: "#21262D"
          formats_supported: [png, jpg, jpeg, svg]
    """

    # Supported formats
    SUPPORTED_FORMATS = {'.png', '.jpg', '.jpeg', '.svg'}

    # Max file size (10MB as per PRD)
    MAX_FILE_SIZE = 10 * 1024 * 1024

    # Placeholder dimensions
    PLACEHOLDER_WIDTH = 500
    PLACEHOLDER_HEIGHT = 300

    def __init__(self, config: Dict[str, Any], placeholder_path: Optional[Path] = None):
        """
        Initialize image processor.

        Args:
            config: Configuration dictionary with 'images' section
            placeholder_path: Path to placeholder image (generated if not provided)
        """
        self.config = config.get('images', {})
        self.base_directory = Path(self.config.get('base_directory', './images'))
        self.max_width = self.config.get('max_width', 500)
        self.placeholder_on_missing = self.config.get('placeholder_on_missing', True)
        self.placeholder_color = self.config.get('placeholder_color', '#21262D')
        self.formats_supported = set(
            f".{fmt}" for fmt in self.config.get('formats_supported', ['png', 'jpg', 'jpeg', 'svg'])
        )

        # Placeholder image path
        if placeholder_path:
            self.placeholder_path = placeholder_path
        else:
            self.placeholder_path = Path(__file__).parent.parent / 'assets' / 'placeholder.png'

        # Temp directory for resized images
        self.temp_dir = Path(tempfile.gettempdir()) / 'handout_images'
        self.temp_dir.mkdir(exist_ok=True)

        logger.info(
            f"ImageProcessor initialized: base_dir={self.base_directory}, "
            f"max_width={self.max_width}, formats={self.formats_supported}"
        )

    def process_images(self, image_references: List[ImageReference]) -> List[ImageReference]:
        """
        Process a list of image references.

        Args:
            image_references: List of ImageReference objects from parser

        Returns:
            List of processed ImageReference objects with resolved paths
        """
        processed = []

        for img_ref in image_references:
            try:
                processed_ref = self.process_image(img_ref)
                processed.append(processed_ref)
            except Exception as e:
                logger.error(f"Error processing image {img_ref.id}: {e}")
                # Create placeholder reference
                processed_ref = self._create_placeholder_reference(img_ref, str(e))
                processed.append(processed_ref)

        logger.info(
            f"Processed {len(processed)} images: "
            f"{sum(1 for img in processed if img.exists)} valid, "
            f"{sum(1 for img in processed if img.placeholder_used)} placeholders"
        )

        return processed

    def process_image(self, image_ref: ImageReference) -> ImageReference:
        """
        Process a single image reference.

        Steps:
        1. Resolve image path
        2. Validate format and size
        3. Resize if needed
        4. Update ImageReference with resolved path

        Args:
            image_ref: ImageReference object

        Returns:
            Updated ImageReference with resolved_path, exists flag
        """
        # Resolve path
        resolved_path, exists = self._resolve_image_path(image_ref.original_path)

        if not exists:
            logger.warning(f"Image not found: {image_ref.original_path}")
            if self.placeholder_on_missing:
                return self._create_placeholder_reference(
                    image_ref,
                    f"Image not found: {image_ref.original_path}"
                )
            else:
                image_ref.exists = False
                image_ref.placeholder_used = False
                return image_ref

        # Validate format
        if not self._validate_format(resolved_path):
            logger.warning(f"Unsupported format: {resolved_path.suffix}")
            return self._create_placeholder_reference(
                image_ref,
                f"Unsupported format: {resolved_path.suffix}"
            )

        # Validate file size
        if not self._validate_size(resolved_path):
            file_size_mb = resolved_path.stat().st_size / (1024 * 1024)
            logger.warning(f"Image too large: {file_size_mb:.1f}MB > 10MB")
            return self._create_placeholder_reference(
                image_ref,
                f"Image too large: {file_size_mb:.1f}MB (max 10MB)"
            )

        # Resize image if needed
        try:
            processed_path = self._resize_image(resolved_path)
            width, height = self._get_image_dimensions(processed_path)

            image_ref.resolved_path = processed_path
            image_ref.exists = True
            image_ref.width = width
            image_ref.height = height
            image_ref.placeholder_used = False

            logger.debug(f"Processed image: {image_ref.id} -> {processed_path} ({width}x{height})")

        except Exception as e:
            logger.error(f"Error processing image {resolved_path}: {e}")
            return self._create_placeholder_reference(
                image_ref,
                f"Processing error: {str(e)}"
            )

        return image_ref

    def _resolve_image_path(self, original_path: str) -> Tuple[Path, bool]:
        """
        Resolve image path (relative or absolute).

        Args:
            original_path: Original path from markdown

        Returns:
            Tuple of (resolved_path, exists)
        """
        try:
            # Try to validate as image path
            resolved_path, exists = SecurityValidator.validate_image_path(
                original_path,
                str(self.base_directory)
            )
            return resolved_path, exists

        except ValueError as e:
            # Path validation failed - try relative to base directory
            logger.debug(f"Path validation failed, trying relative: {e}")

            # Clean path (remove ../ and normalize)
            clean_path = Path(original_path).name

            # Try in base directory
            base_path = self.base_directory / clean_path
            if base_path.exists() and base_path.is_file():
                return base_path, True

            # Not found
            return Path(original_path), False

    def _validate_format(self, image_path: Path) -> bool:
        """
        Validate image format.

        Args:
            image_path: Path to image

        Returns:
            True if format is supported
        """
        return image_path.suffix.lower() in self.formats_supported

    def _validate_size(self, image_path: Path) -> bool:
        """
        Validate image file size.

        Args:
            image_path: Path to image

        Returns:
            True if size is acceptable (<10MB)
        """
        try:
            size = image_path.stat().st_size
            return size <= self.MAX_FILE_SIZE
        except OSError:
            return False

    def _resize_image(self, image_path: Path) -> Path:
        """
        Resize image to max width (maintain aspect ratio).

        Uses Pillow's high-quality LANCZOS resampling.
        Saves resized image to temp directory.

        Args:
            image_path: Path to original image

        Returns:
            Path to resized image (or original if no resize needed)
        """
        # Skip SVG files (vector format, doesn't need resizing)
        if image_path.suffix.lower() == '.svg':
            return image_path

        try:
            # Open image
            with Image.open(image_path) as img:
                original_width, original_height = img.size

                # Check if resize needed
                if original_width <= self.max_width:
                    logger.debug(f"Image within max width, no resize: {image_path.name}")
                    return image_path

                # Calculate new dimensions (maintain aspect ratio)
                ratio = self.max_width / original_width
                new_width = self.max_width
                new_height = int(original_height * ratio)

                logger.debug(
                    f"Resizing {image_path.name}: {original_width}x{original_height} -> "
                    f"{new_width}x{new_height}"
                )

                # Resize with high-quality LANCZOS filter
                resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Convert RGBA to RGB if saving as JPEG
                if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                    if resized.mode in ('RGBA', 'LA', 'P'):
                        # Create white background
                        background = Image.new('RGB', resized.size, (255, 255, 255))
                        if resized.mode == 'P':
                            resized = resized.convert('RGBA')
                        background.paste(resized, mask=resized.split()[-1] if resized.mode == 'RGBA' else None)
                        resized = background

                # Save to temp directory
                output_path = self.temp_dir / f"resized_{image_path.name}"

                # Determine save format
                save_kwargs = {}
                if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                    save_kwargs = {'quality': 90, 'optimize': True}
                elif image_path.suffix.lower() == '.png':
                    save_kwargs = {'optimize': True}

                resized.save(output_path, **save_kwargs)

                logger.debug(f"Saved resized image to: {output_path}")

                return output_path

        except Exception as e:
            logger.error(f"Error resizing image {image_path}: {e}")
            raise ImageProcessorError(f"Failed to resize image: {e}")

    def _get_image_dimensions(self, image_path: Path) -> Tuple[int, int]:
        """
        Get image dimensions.

        Args:
            image_path: Path to image

        Returns:
            Tuple of (width, height)
        """
        # For SVG, return default dimensions
        if image_path.suffix.lower() == '.svg':
            return self.max_width, 300  # Default SVG dimensions

        try:
            with Image.open(image_path) as img:
                return img.size
        except Exception as e:
            logger.warning(f"Could not get dimensions for {image_path}: {e}")
            return self.max_width, 300

    def _create_placeholder_reference(
        self,
        original_ref: ImageReference,
        reason: str
    ) -> ImageReference:
        """
        Create placeholder image reference.

        Args:
            original_ref: Original ImageReference
            reason: Reason for placeholder

        Returns:
            ImageReference with placeholder path
        """
        # Ensure placeholder exists
        if not self.placeholder_path.exists():
            logger.warning(f"Placeholder image not found at {self.placeholder_path}, generating...")
            self.generate_placeholder()

        # Update reference
        original_ref.resolved_path = self.placeholder_path
        original_ref.exists = True  # Placeholder exists
        original_ref.placeholder_used = True
        original_ref.width = self.PLACEHOLDER_WIDTH
        original_ref.height = self.PLACEHOLDER_HEIGHT

        logger.debug(f"Using placeholder for {original_ref.id}: {reason}")

        return original_ref

    def generate_placeholder(
        self,
        output_path: Optional[Path] = None,
        width: int = PLACEHOLDER_WIDTH,
        height: int = PLACEHOLDER_HEIGHT
    ) -> Path:
        """
        Generate dark-themed placeholder image.

        Creates a placeholder with:
        - Background: #21262D (dark theme tertiary)
        - Text: #484F58 (muted gray)
        - Text: "Image not found"
        - Size: 500x300px (default)

        Args:
            output_path: Where to save placeholder (default: assets/placeholder.png)
            width: Placeholder width
            height: Placeholder height

        Returns:
            Path to generated placeholder
        """
        if output_path is None:
            output_path = self.placeholder_path

        # Ensure parent directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Convert hex color to RGB
        bg_color = self._hex_to_rgb(self.placeholder_color)
        text_color = self._hex_to_rgb('#484F58')  # Muted gray

        # Create image
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)

        # Text to display
        text = "Image not found"

        # Try to use a nice font, fall back to default if not available
        try:
            # Try to find Inter font (used in dark theme)
            font_size = 24
            font_paths = [
                '/System/Library/Fonts/Supplemental/Arial.ttf',  # macOS
                '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
                'C:\\Windows\\Fonts\\arial.ttf',  # Windows
            ]

            font = None
            for font_path in font_paths:
                if Path(font_path).exists():
                    font = ImageFont.truetype(font_path, font_size)
                    break

            if font is None:
                font = ImageFont.load_default()

        except Exception as e:
            logger.warning(f"Could not load font, using default: {e}")
            font = ImageFont.load_default()

        # Get text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate position (centered)
        x = (width - text_width) // 2
        y = (height - text_height) // 2

        # Draw text
        draw.text((x, y), text, fill=text_color, font=font)

        # Save
        img.save(output_path, 'PNG', optimize=True)

        logger.info(f"Generated placeholder image: {output_path}")

        return output_path

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """
        Convert hex color to RGB tuple.

        Args:
            hex_color: Hex color code (e.g., "#21262D")

        Returns:
            RGB tuple (r, g, b)
        """
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def cleanup_temp_files(self):
        """
        Clean up temporary resized images.

        Call this after PDF generation is complete.
        """
        try:
            if self.temp_dir.exists():
                for file in self.temp_dir.glob('resized_*'):
                    file.unlink()
                logger.info(f"Cleaned up temp files in {self.temp_dir}")
        except Exception as e:
            logger.warning(f"Error cleaning up temp files: {e}")

    def get_stats(self, processed_images: List[ImageReference]) -> Dict[str, Any]:
        """
        Get statistics about processed images.

        Args:
            processed_images: List of processed ImageReference objects

        Returns:
            Dictionary with statistics
        """
        stats = {
            'total': len(processed_images),
            'valid': sum(1 for img in processed_images if img.exists and not img.placeholder_used),
            'placeholders': sum(1 for img in processed_images if img.placeholder_used),
            'missing': sum(1 for img in processed_images if not img.exists),
            'formats': {}
        }

        # Count by format
        for img in processed_images:
            if img.resolved_path:
                fmt = img.resolved_path.suffix.lower()
                stats['formats'][fmt] = stats['formats'].get(fmt, 0) + 1

        return stats
