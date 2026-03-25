"""
Framework Parser for Student Handout Generator

Parses markdown framework files, extracting YAML frontmatter metadata,
building hierarchical section structure, and detecting image references.
"""

import re
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, Union, List, Tuple, Dict

import yaml
from mistune import create_markdown
from mistune.core import BlockState

from .models import (
    FrameworkMetadata,
    ContentSection,
    ImageReference,
    ParseResult,
)


logger = logging.getLogger(__name__)


class FrameworkParserError(Exception):
    """Base exception for framework parsing errors"""
    pass


class FrameworkParser:
    """
    Parses markdown framework files into structured data.

    Features:
    - YAML frontmatter extraction
    - Hierarchical section parsing (H1-H6)
    - Image reference detection
    - UTF-8 encoding support
    - Error handling for malformed files

    Usage:
        parser = FrameworkParser()
        result = parser.parse_file("path/to/framework.md")
        if result.success:
            print(f"Parsed {len(result.sections)} sections")
        else:
            print(f"Errors: {result.errors}")
    """

    # Maximum file size: 5MB (as per PRD)
    MAX_FILE_SIZE = 5 * 1024 * 1024
    MAX_LINES = 5000

    def __init__(self):
        """Initialize the parser with markdown processor"""
        self.markdown = create_markdown(renderer=None)

    def parse_file(self, file_path: Union[str, Path]) -> ParseResult:
        """
        Parse a framework markdown file.

        Args:
            file_path: Path to the framework file

        Returns:
            ParseResult with metadata, sections, images, and any errors/warnings
        """
        result = ParseResult()
        file_path = Path(file_path)

        try:
            # Validate file exists
            if not file_path.exists():
                result.errors.append(f"File not found: {file_path}")
                return result

            # Check file size
            file_size = file_path.stat().st_size
            if file_size > self.MAX_FILE_SIZE:
                result.errors.append(
                    f"File exceeds 5MB limit: {file_size / (1024*1024):.2f}MB"
                )
                return result

            # Read file with UTF-8 encoding
            try:
                content = file_path.read_text(encoding='utf-8')
            except UnicodeDecodeError as e:
                result.errors.append(
                    f"Invalid UTF-8 encoding: {e}. Please ensure file is saved as UTF-8."
                )
                return result

            # Check line count
            lines = content.split('\n')
            if len(lines) > self.MAX_LINES:
                result.warnings.append(
                    f"File has {len(lines)} lines (recommended max: {self.MAX_LINES}). "
                    "Processing may be slow."
                )

            # Extract YAML frontmatter and markdown content
            frontmatter, markdown_content = self._split_frontmatter(content)

            # Parse metadata
            metadata = self._parse_metadata(frontmatter, file_path)
            if metadata is None:
                result.errors.append("Missing required metadata fields")
                return result

            result.metadata = metadata

            # Parse markdown structure
            sections = self._parse_sections(markdown_content)
            result.sections = sections

            # Extract image references
            images = self._extract_images(markdown_content)
            result.images = images

            result.success = True
            logger.info(
                f"Successfully parsed {file_path.name}: "
                f"{len(sections)} sections, {len(images)} images"
            )

        except Exception as e:
            logger.exception(f"Unexpected error parsing {file_path}")
            result.errors.append(f"Unexpected error: {str(e)}")

        return result

    def _split_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """
        Split YAML frontmatter from markdown content.

        Args:
            content: Full file content

        Returns:
            Tuple of (frontmatter_dict, markdown_content)
        """
        # Match YAML frontmatter: --- ... ---
        pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(pattern, content, re.DOTALL)

        if match:
            yaml_str = match.group(1)
            markdown_content = match.group(2)

            try:
                frontmatter = yaml.safe_load(yaml_str) or {}
            except yaml.YAMLError as e:
                logger.warning(f"Invalid YAML frontmatter: {e}")
                frontmatter = {}

            return frontmatter, markdown_content
        else:
            logger.warning("No YAML frontmatter found")
            return {}, content

    def _parse_metadata(
        self, frontmatter: Dict, file_path: Path
    ) -> Optional[FrameworkMetadata]:
        """
        Parse metadata from YAML frontmatter.

        Required fields:
        - course_code
        - module_number
        - module_title

        Args:
            frontmatter: Dictionary from YAML frontmatter
            file_path: Path to source file

        Returns:
            FrameworkMetadata if valid, None if missing required fields
        """
        # Check required fields
        required = ['course_code', 'module_number', 'module_title']
        missing = [f for f in required if f not in frontmatter]

        if missing:
            logger.error(f"Missing required metadata fields: {', '.join(missing)}")
            return None

        # Parse optional date field
        last_updated = None
        if 'last_updated' in frontmatter:
            date_val = frontmatter['last_updated']
            if isinstance(date_val, datetime):
                last_updated = date_val
            elif isinstance(date_val, str):
                try:
                    last_updated = datetime.fromisoformat(date_val)
                except ValueError:
                    logger.warning(f"Invalid date format: {date_val}")

        return FrameworkMetadata(
            course_code=str(frontmatter['course_code']),
            module_number=int(frontmatter['module_number']),
            module_title=str(frontmatter['module_title']),
            duration=frontmatter.get('duration'),
            video_content=frontmatter.get('video_content'),
            hands_on_time=frontmatter.get('hands_on_time'),
            theory_practice_ratio=frontmatter.get('theory_practice_ratio'),
            file_path=file_path,
            last_updated=last_updated,
            version=str(frontmatter.get('version', '1.0')),
        )

    def _parse_sections(self, markdown_content: str) -> List[ContentSection]:
        """
        Parse markdown into hierarchical sections.

        Creates a tree structure of ContentSection objects based on
        heading levels (H1-H6).

        Args:
            markdown_content: Markdown text (without frontmatter)

        Returns:
            List of top-level ContentSection objects
        """
        sections = []
        section_stack = []  # Stack to track nested sections

        # Split by headings while preserving content
        lines = markdown_content.split('\n')
        current_content = []
        current_heading = None
        current_level = 0
        in_code_block = False

        for line in lines:
            # Track code block state (triple backticks)
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                current_content.append(line)
                continue

            # Skip heading detection if inside code block
            if in_code_block:
                current_content.append(line)
                continue

            # Check if line is a heading
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)

            if heading_match:
                # Save previous section if exists
                if current_heading is not None:
                    section = self._create_section(
                        current_heading,
                        current_level,
                        '\n'.join(current_content)
                    )
                    self._add_section_to_hierarchy(
                        section, sections, section_stack, current_level
                    )

                # Start new section
                current_level = len(heading_match.group(1))
                current_heading = heading_match.group(2).strip()
                current_content = []
            else:
                # Add to current section content
                current_content.append(line)

        # Save last section
        if current_heading is not None:
            section = self._create_section(
                current_heading,
                current_level,
                '\n'.join(current_content)
            )
            self._add_section_to_hierarchy(
                section, sections, section_stack, current_level
            )

        return sections

    def _create_section(
        self, title: str, level: int, content: str
    ) -> ContentSection:
        """
        Create a ContentSection object.

        Args:
            title: Section title
            level: Heading level (1-6)
            content: Section content (markdown)

        Returns:
            ContentSection object
        """
        # Generate ID from title
        section_id = re.sub(r'[^a-z0-9-]', '', title.lower().replace(' ', '-'))

        return ContentSection(
            id=section_id,
            level=level,
            title=title,
            content=content.strip(),
            subsections=[],
            metadata={},
            include_in_handout=True,
            question_count=0,
        )

    def _add_section_to_hierarchy(
        self,
        section: ContentSection,
        sections: List[ContentSection],
        section_stack: List[Tuple[int, ContentSection]],
        level: int,
    ):
        """
        Add section to the hierarchical structure.

        Maintains a stack of parent sections to build the tree correctly.

        Args:
            section: Section to add
            sections: Top-level sections list
            section_stack: Stack of (level, section) tuples
            level: Current heading level
        """
        # Pop stack until we find the parent level
        while section_stack and section_stack[-1][0] >= level:
            section_stack.pop()

        if section_stack:
            # Add as subsection to parent
            parent = section_stack[-1][1]
            parent.subsections.append(section)
        else:
            # Add as top-level section
            sections.append(section)

        # Push current section onto stack
        section_stack.append((level, section))

    def _extract_images(self, markdown_content: str) -> List[ImageReference]:
        """
        Extract image references from markdown.

        Detects markdown image syntax: ![alt text](path "caption")

        Args:
            markdown_content: Markdown text

        Returns:
            List of ImageReference objects
        """
        images = []
        # Pattern: ![alt](path) or ![alt](path "caption")
        pattern = r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]+)")?\)'

        matches = re.finditer(pattern, markdown_content)

        for i, match in enumerate(matches, start=1):
            alt_text = match.group(1)
            image_path = match.group(2)
            caption = match.group(3)  # May be None

            image_ref = ImageReference(
                id=f"img-{i}",
                original_path=image_path,
                alt_text=alt_text,
                caption=caption,
            )

            images.append(image_ref)

        logger.debug(f"Found {len(images)} image references")
        return images

    def parse_content(self, content: str) -> ParseResult:
        """
        Parse markdown content directly (without file I/O).

        Useful for testing or processing in-memory content.

        Args:
            content: Markdown content with YAML frontmatter

        Returns:
            ParseResult
        """
        result = ParseResult()

        try:
            # Extract frontmatter and content
            frontmatter, markdown_content = self._split_frontmatter(content)

            # Parse metadata (no file_path)
            if not frontmatter:
                result.warnings.append("No YAML frontmatter found")
                # Create minimal metadata
                metadata = FrameworkMetadata(
                    course_code="UNKNOWN",
                    module_number=0,
                    module_title="Untitled",
                )
            else:
                metadata = self._parse_metadata(frontmatter, Path("unknown"))
                if metadata is None:
                    result.errors.append("Missing required metadata")
                    return result

            result.metadata = metadata

            # Parse sections
            sections = self._parse_sections(markdown_content)
            result.sections = sections

            # Extract images
            images = self._extract_images(markdown_content)
            result.images = images

            result.success = True

        except Exception as e:
            logger.exception("Error parsing content")
            result.errors.append(f"Parse error: {str(e)}")

        return result
