"""
Unit Tests for Image Processor

Tests cover:
- Image validation (format, size, existence)
- Path resolution (relative/absolute)
- Image resizing (aspect ratio maintenance)
- Placeholder generation (dark theme)
- Error handling
- Security (path traversal prevention)
"""

import pytest
import tempfile
from pathlib import Path
from PIL import Image

from src.image_processor import ImageProcessor, ImageProcessorError
from src.models import ImageReference


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def config():
    """Default configuration for tests"""
    return {
        'images': {
            'base_directory': './test_images',
            'max_width': 500,
            'placeholder_on_missing': True,
            'placeholder_color': '#21262D',
            'formats_supported': ['png', 'jpg', 'jpeg', 'svg']
        }
    }


@pytest.fixture
def image_processor(config, temp_dir):
    """Create ImageProcessor instance with test config"""
    # Update config to use temp directory
    config['images']['base_directory'] = str(temp_dir)
    placeholder_path = temp_dir / 'placeholder.png'
    processor = ImageProcessor(config, placeholder_path=placeholder_path)
    return processor


@pytest.fixture
def test_image(temp_dir):
    """Create a small test image (100x100 PNG)"""
    img_path = temp_dir / 'test_image.png'
    img = Image.new('RGB', (100, 100), color='blue')
    img.save(img_path, 'PNG')
    return img_path


@pytest.fixture
def test_image_large(temp_dir):
    """Create a large test image (1000x800 PNG)"""
    img_path = temp_dir / 'test_image_large.png'
    img = Image.new('RGB', (1000, 800), color='red')
    img.save(img_path, 'PNG')
    return img_path


@pytest.fixture
def test_image_jpeg(temp_dir):
    """Create a JPEG test image"""
    img_path = temp_dir / 'test_image.jpg'
    img = Image.new('RGB', (200, 200), color='green')
    img.save(img_path, 'JPEG')
    return img_path


@pytest.fixture
def test_image_huge_file(temp_dir):
    """Create a test image >10MB"""
    img_path = temp_dir / 'test_image_huge.png'
    # Create a 3000x3000 image (will be >10MB uncompressed)
    img = Image.new('RGB', (3000, 3000), color='white')
    # Fill with random-looking data to prevent compression
    pixels = img.load()
    for i in range(3000):
        for j in range(3000):
            pixels[i, j] = (i % 256, j % 256, (i+j) % 256)
    img.save(img_path, 'PNG', compress_level=0)
    return img_path


class TestImageProcessorInit:
    """Test ImageProcessor initialization"""

    def test_init_with_config(self, config):
        """Test initialization with valid config"""
        processor = ImageProcessor(config)
        assert processor.max_width == 500
        assert processor.placeholder_color == '#21262D'
        assert '.png' in processor.formats_supported
        assert '.jpg' in processor.formats_supported

    def test_init_with_defaults(self):
        """Test initialization with minimal config"""
        processor = ImageProcessor({})
        assert processor.max_width == 500  # Default
        assert processor.placeholder_on_missing is True  # Default

    def test_temp_dir_creation(self, config):
        """Test temp directory is created"""
        processor = ImageProcessor(config)
        assert processor.temp_dir.exists()
        assert processor.temp_dir.is_dir()


class TestPathResolution:
    """Test image path resolution"""

    def test_resolve_absolute_path(self, image_processor, test_image):
        """Test resolving absolute path"""
        resolved, exists = image_processor._resolve_image_path(str(test_image))
        assert exists
        assert resolved.exists()

    def test_resolve_relative_path(self, image_processor, temp_dir, test_image):
        """Test resolving relative path"""
        # Use just the filename
        resolved, exists = image_processor._resolve_image_path(test_image.name)
        assert exists
        assert resolved.name == test_image.name

    def test_resolve_nonexistent_path(self, image_processor):
        """Test resolving non-existent path"""
        resolved, exists = image_processor._resolve_image_path('nonexistent.png')
        assert not exists

    def test_resolve_path_traversal_blocked(self, image_processor):
        """Test path traversal attempts are blocked"""
        # Should not allow traversal
        resolved, exists = image_processor._resolve_image_path('../../etc/passwd')
        assert not exists


class TestFormatValidation:
    """Test image format validation"""

    def test_validate_png_format(self, image_processor, test_image):
        """Test PNG format is valid"""
        assert image_processor._validate_format(test_image)

    def test_validate_jpg_format(self, image_processor, test_image_jpeg):
        """Test JPG format is valid"""
        assert image_processor._validate_format(test_image_jpeg)

    def test_validate_svg_format(self, image_processor, temp_dir):
        """Test SVG format is valid"""
        svg_path = temp_dir / 'test.svg'
        svg_path.write_text('<svg></svg>')
        assert image_processor._validate_format(svg_path)

    def test_reject_invalid_format(self, image_processor, temp_dir):
        """Test invalid format is rejected"""
        invalid_path = temp_dir / 'test.bmp'
        invalid_path.touch()
        assert not image_processor._validate_format(invalid_path)


class TestSizeValidation:
    """Test image size validation"""

    def test_validate_small_file(self, image_processor, test_image):
        """Test small file passes validation"""
        assert image_processor._validate_size(test_image)

    def test_reject_large_file(self, image_processor, test_image_huge_file):
        """Test file >10MB is rejected"""
        # Check file size first
        file_size = test_image_huge_file.stat().st_size
        if file_size > ImageProcessor.MAX_FILE_SIZE:
            assert not image_processor._validate_size(test_image_huge_file)
        else:
            pytest.skip("Test image not large enough (compression reduced size)")


class TestImageResizing:
    """Test image resizing"""

    def test_resize_large_image(self, image_processor, test_image_large):
        """Test large image is resized to max width"""
        resized_path = image_processor._resize_image(test_image_large)
        assert resized_path.exists()

        # Check dimensions
        with Image.open(resized_path) as img:
            width, height = img.size
            assert width == 500  # Max width
            # Check aspect ratio maintained (1000x800 -> 500x400)
            expected_height = int(800 * (500 / 1000))
            assert height == expected_height

    def test_no_resize_small_image(self, image_processor, test_image):
        """Test small image is not resized"""
        resized_path = image_processor._resize_image(test_image)
        # Should return original path (no resize needed)
        assert resized_path == test_image

        # Verify dimensions unchanged
        with Image.open(resized_path) as img:
            width, height = img.size
            assert width == 100
            assert height == 100

    def test_resize_jpeg_image(self, image_processor, temp_dir):
        """Test JPEG image resizing"""
        # Create large JPEG
        jpeg_path = temp_dir / 'large.jpg'
        img = Image.new('RGB', (1000, 600), color='blue')
        img.save(jpeg_path, 'JPEG')

        resized_path = image_processor._resize_image(jpeg_path)
        assert resized_path.exists()

        # Check dimensions
        with Image.open(resized_path) as img:
            width, height = img.size
            assert width == 500
            assert height == 300  # 1000x600 -> 500x300

    def test_skip_svg_resize(self, image_processor, temp_dir):
        """Test SVG files are not resized (vector format)"""
        svg_path = temp_dir / 'test.svg'
        svg_path.write_text('<svg width="1000" height="800"></svg>')

        resized_path = image_processor._resize_image(svg_path)
        # Should return original path (SVG not resized)
        assert resized_path == svg_path

    def test_resize_maintains_aspect_ratio(self, image_processor, temp_dir):
        """Test aspect ratio is maintained during resize"""
        # Create image with specific aspect ratio (16:9)
        img_path = temp_dir / 'aspect.png'
        img = Image.new('RGB', (1600, 900), color='purple')
        img.save(img_path, 'PNG')

        resized_path = image_processor._resize_image(img_path)

        with Image.open(resized_path) as img:
            width, height = img.size
            assert width == 500
            # 1600x900 -> 500x281.25 -> 281
            expected_height = int(900 * (500 / 1600))
            assert height == expected_height

    def test_resize_rgba_to_jpeg(self, image_processor, temp_dir):
        """Test RGBA image is converted to RGB when saving as JPEG"""
        # Create RGBA PNG
        rgba_path = temp_dir / 'rgba.png'
        img = Image.new('RGBA', (1000, 500), color=(255, 0, 0, 128))
        img.save(rgba_path, 'PNG')

        # Rename to .jpg to trigger JPEG save
        jpeg_path = temp_dir / 'rgba.jpg'
        rgba_path.rename(jpeg_path)

        resized_path = image_processor._resize_image(jpeg_path)

        # Should successfully save as JPEG (no transparency)
        with Image.open(resized_path) as img:
            assert img.mode == 'RGB'


class TestPlaceholderGeneration:
    """Test placeholder image generation"""

    def test_generate_placeholder_default(self, image_processor, temp_dir):
        """Test generating placeholder with defaults"""
        output_path = temp_dir / 'placeholder.png'
        result_path = image_processor.generate_placeholder(output_path)

        assert result_path.exists()
        assert result_path == output_path

        # Check image properties
        with Image.open(result_path) as img:
            assert img.size == (500, 300)
            assert img.mode == 'RGB'

    def test_generate_placeholder_custom_size(self, image_processor, temp_dir):
        """Test generating placeholder with custom size"""
        output_path = temp_dir / 'placeholder_custom.png'
        result_path = image_processor.generate_placeholder(
            output_path,
            width=400,
            height=200
        )

        with Image.open(result_path) as img:
            assert img.size == (400, 200)

    def test_placeholder_has_dark_background(self, image_processor, temp_dir):
        """Test placeholder has correct dark theme background color"""
        output_path = temp_dir / 'placeholder.png'
        image_processor.generate_placeholder(output_path)

        with Image.open(output_path) as img:
            # Check background color (sample pixel from corner)
            pixel = img.getpixel((10, 10))
            # Should be #21262D = (33, 38, 45)
            expected = (33, 38, 45)
            # Allow small difference due to potential font rendering
            assert abs(pixel[0] - expected[0]) <= 5
            assert abs(pixel[1] - expected[1]) <= 5
            assert abs(pixel[2] - expected[2]) <= 5

    def test_hex_to_rgb_conversion(self, image_processor):
        """Test hex color to RGB conversion"""
        rgb = image_processor._hex_to_rgb('#21262D')
        assert rgb == (33, 38, 45)

        rgb2 = image_processor._hex_to_rgb('#FFFFFF')
        assert rgb2 == (255, 255, 255)

        rgb3 = image_processor._hex_to_rgb('#000000')
        assert rgb3 == (0, 0, 0)


class TestProcessImage:
    """Test processing individual images"""

    def test_process_valid_image(self, image_processor, test_image):
        """Test processing a valid image"""
        img_ref = ImageReference(
            id='img-1',
            original_path=str(test_image),
            alt_text='Test image'
        )

        result = image_processor.process_image(img_ref)

        assert result.exists
        assert result.resolved_path is not None
        assert not result.placeholder_used
        assert result.width > 0
        assert result.height > 0

    def test_process_missing_image(self, image_processor):
        """Test processing a missing image uses placeholder"""
        img_ref = ImageReference(
            id='img-missing',
            original_path='nonexistent.png',
            alt_text='Missing image'
        )

        # Generate placeholder first
        image_processor.generate_placeholder()

        result = image_processor.process_image(img_ref)

        assert result.exists  # Placeholder exists
        assert result.placeholder_used
        assert result.resolved_path == image_processor.placeholder_path

    def test_process_unsupported_format(self, image_processor, temp_dir):
        """Test processing unsupported format uses placeholder"""
        # Create .bmp file (not supported)
        bmp_path = temp_dir / 'test.bmp'
        img = Image.new('RGB', (100, 100), color='blue')
        img.save(bmp_path, 'BMP')

        img_ref = ImageReference(
            id='img-bmp',
            original_path=str(bmp_path),
            alt_text='BMP image'
        )

        # Generate placeholder first
        image_processor.generate_placeholder()

        result = image_processor.process_image(img_ref)

        assert result.placeholder_used

    def test_process_large_image_resized(self, image_processor, test_image_large):
        """Test large image is resized"""
        img_ref = ImageReference(
            id='img-large',
            original_path=str(test_image_large),
            alt_text='Large image'
        )

        result = image_processor.process_image(img_ref)

        assert result.exists
        assert result.width == 500  # Resized to max width
        assert result.height == 400  # Aspect ratio maintained (1000x800 -> 500x400)


class TestProcessImages:
    """Test batch processing of images"""

    def test_process_multiple_images(self, image_processor, test_image, test_image_jpeg):
        """Test processing multiple images"""
        img_refs = [
            ImageReference(id='img-1', original_path=str(test_image), alt_text='PNG'),
            ImageReference(id='img-2', original_path=str(test_image_jpeg), alt_text='JPEG'),
        ]

        results = image_processor.process_images(img_refs)

        assert len(results) == 2
        assert all(img.exists for img in results)
        assert not any(img.placeholder_used for img in results)

    def test_process_mixed_valid_invalid(self, image_processor, test_image):
        """Test processing mix of valid and invalid images"""
        # Generate placeholder first
        image_processor.generate_placeholder()

        img_refs = [
            ImageReference(id='img-1', original_path=str(test_image), alt_text='Valid'),
            ImageReference(id='img-2', original_path='missing.png', alt_text='Missing'),
        ]

        results = image_processor.process_images(img_refs)

        assert len(results) == 2
        assert results[0].exists and not results[0].placeholder_used
        assert results[1].exists and results[1].placeholder_used

    def test_process_empty_list(self, image_processor):
        """Test processing empty list"""
        results = image_processor.process_images([])
        assert len(results) == 0


class TestStatistics:
    """Test statistics generation"""

    def test_get_stats(self, image_processor, test_image, test_image_jpeg):
        """Test getting statistics about processed images"""
        # Generate placeholder
        image_processor.generate_placeholder()

        img_refs = [
            ImageReference(id='img-1', original_path=str(test_image), alt_text='PNG'),
            ImageReference(id='img-2', original_path=str(test_image_jpeg), alt_text='JPEG'),
            ImageReference(id='img-3', original_path='missing.png', alt_text='Missing'),
        ]

        results = image_processor.process_images(img_refs)
        stats = image_processor.get_stats(results)

        assert stats['total'] == 3
        assert stats['valid'] == 2
        assert stats['placeholders'] == 1
        assert '.png' in stats['formats']
        assert '.jpg' in stats['formats']


class TestCleanup:
    """Test cleanup operations"""

    def test_cleanup_temp_files(self, image_processor, test_image_large):
        """Test cleaning up temporary resized files"""
        # Process a large image (creates temp file)
        img_ref = ImageReference(
            id='img-large',
            original_path=str(test_image_large),
            alt_text='Large'
        )
        image_processor.process_image(img_ref)

        # Verify temp file exists
        temp_files = list(image_processor.temp_dir.glob('resized_*'))
        assert len(temp_files) > 0

        # Cleanup
        image_processor.cleanup_temp_files()

        # Verify temp files removed
        temp_files = list(image_processor.temp_dir.glob('resized_*'))
        assert len(temp_files) == 0


class TestErrorHandling:
    """Test error handling"""

    def test_corrupted_image_uses_placeholder(self, image_processor, temp_dir):
        """Test corrupted image file uses placeholder"""
        # Create a file that's not a valid image
        corrupted_path = temp_dir / 'corrupted.png'
        corrupted_path.write_bytes(b'not an image')

        # Generate placeholder
        image_processor.generate_placeholder()

        img_ref = ImageReference(
            id='img-corrupt',
            original_path=str(corrupted_path),
            alt_text='Corrupted'
        )

        result = image_processor.process_image(img_ref)

        # Should fall back to placeholder
        assert result.placeholder_used

    def test_process_image_permission_error(self, image_processor):
        """Test handling permission errors"""
        # This test is platform-dependent, may skip on some systems
        img_ref = ImageReference(
            id='img-perm',
            original_path='/root/restricted.png',  # Likely no permission
            alt_text='Restricted'
        )

        # Generate placeholder
        image_processor.generate_placeholder()

        result = image_processor.process_image(img_ref)

        # Should use placeholder when file can't be accessed
        assert result.placeholder_used or not result.exists


class TestIntegration:
    """Integration tests with realistic scenarios"""

    def test_full_workflow(self, image_processor, temp_dir):
        """Test complete workflow from parsing to processing"""
        # Create test images
        img1 = temp_dir / 'photo1.png'
        img2 = temp_dir / 'photo2.jpg'
        img3 = temp_dir / 'diagram.png'

        Image.new('RGB', (800, 600), 'blue').save(img1, 'PNG')
        Image.new('RGB', (1200, 800), 'green').save(img2, 'JPEG')
        Image.new('RGB', (400, 300), 'red').save(img3, 'PNG')

        # Generate placeholder
        image_processor.generate_placeholder()

        # Create references (like from parser)
        img_refs = [
            ImageReference(id='img-1', original_path=str(img1), alt_text='Photo 1'),
            ImageReference(id='img-2', original_path=str(img2), alt_text='Photo 2'),
            ImageReference(id='img-3', original_path=str(img3), alt_text='Diagram'),
            ImageReference(id='img-4', original_path='missing.png', alt_text='Missing'),
        ]

        # Process all images
        results = image_processor.process_images(img_refs)

        # Verify results
        assert len(results) == 4
        assert results[0].width == 500  # Resized from 800
        assert results[1].width == 500  # Resized from 1200
        assert results[2].width == 400  # Not resized (under max)
        assert results[3].placeholder_used  # Missing image

        # Get stats
        stats = image_processor.get_stats(results)
        assert stats['valid'] == 3
        assert stats['placeholders'] == 1

        # Cleanup
        image_processor.cleanup_temp_files()
