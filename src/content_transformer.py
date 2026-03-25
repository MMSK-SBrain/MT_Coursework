"""
Content Transformer for Student Handout Generator.

This module filters instructor-only content and transforms framework content
into student-appropriate format. It removes sections based on configurable
patterns and applies transformation rules.
"""

import logging
import re
from typing import Any, Optional

from src.models import ContentSection

logger = logging.getLogger(__name__)


class ContentTransformer:
    """
    Transforms framework content by filtering instructor-only sections
    and applying transformation rules.

    The transformer supports:
    - Section title pattern matching (case-insensitive)
    - HTML comment block removal (<!-- INSTRUCTOR ONLY --> ... <!-- END INSTRUCTOR ONLY -->)
    - Configurable exclusion patterns
    - Optional find-and-replace terminology transformations
    """

    def __init__(self, config: dict[str, Any]):
        """
        Initialize the ContentTransformer with configuration.

        Args:
            config: Configuration dictionary containing:
                - exclude_patterns: List of section title patterns to exclude
                - transform_rules: Optional find-and-replace rules (dict)
        """
        self.config = config
        self.exclude_patterns = self._compile_patterns(
            config.get('exclude_patterns', [])
        )
        self.transform_rules = config.get('transform_rules', {})

        logger.info(
            f"ContentTransformer initialized with {len(self.exclude_patterns)} "
            f"exclusion patterns and {len(self.transform_rules)} transform rules"
        )

    def _compile_patterns(self, patterns: list[str]) -> list[re.Pattern]:
        """
        Compile exclusion patterns into regex objects.

        Args:
            patterns: List of pattern strings

        Returns:
            List of compiled regex Pattern objects
        """
        compiled = []
        for pattern in patterns:
            try:
                # Escape special regex characters except wildcards
                # Support simple wildcards: * becomes .*
                escaped_pattern = re.escape(pattern).replace(r'\*', '.*')
                compiled.append(re.compile(escaped_pattern, re.IGNORECASE))
                logger.debug(f"Compiled exclusion pattern: {pattern}")
            except re.error as e:
                logger.warning(
                    f"Invalid exclusion pattern '{pattern}': {e}. Skipping."
                )

        return compiled

    def _should_exclude_section(self, title: str) -> bool:
        """
        Check if a section title matches any exclusion pattern.

        Args:
            title: Section title to check

        Returns:
            True if section should be excluded, False otherwise
        """
        for pattern in self.exclude_patterns:
            if pattern.search(title):
                logger.debug(f"Section '{title}' matched exclusion pattern")
                return True

        return False

    def _remove_html_comment_blocks(self, content: str) -> str:
        """
        Remove content between HTML comment tags.

        Removes blocks between:
        - <!-- INSTRUCTOR ONLY --> ... <!-- END INSTRUCTOR ONLY -->
        - <!-- INSTRUCTOR --> ... <!-- /INSTRUCTOR -->
        - Handles multiple blocks in same content

        Args:
            content: Markdown content string

        Returns:
            Content with instructor-only blocks removed
        """
        # Pattern 1: <!-- INSTRUCTOR ONLY --> ... <!-- END INSTRUCTOR ONLY -->
        pattern1 = re.compile(
            r'<!--\s*INSTRUCTOR\s+ONLY\s*-->.*?<!--\s*END\s+INSTRUCTOR\s+ONLY\s*-->',
            re.DOTALL | re.IGNORECASE
        )

        # Pattern 2: <!-- INSTRUCTOR --> ... <!-- /INSTRUCTOR -->
        pattern2 = re.compile(
            r'<!--\s*INSTRUCTOR\s*-->.*?<!--\s*/INSTRUCTOR\s*-->',
            re.DOTALL | re.IGNORECASE
        )

        # Remove all matching blocks
        content = pattern1.sub('', content)
        content = pattern2.sub('', content)

        # Clean up any resulting multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)

        return content.strip()

    def _apply_transformation_rules(self, content: str) -> str:
        """
        Apply find-and-replace transformation rules to content.

        Args:
            content: Markdown content string

        Returns:
            Transformed content
        """
        for find, replace in self.transform_rules.items():
            # Use word boundaries to avoid partial matches
            pattern = re.compile(rf'\b{re.escape(find)}\b', re.IGNORECASE)
            content = pattern.sub(replace, content)

        return content

    def transform_section(
        self,
        section: ContentSection,
        parent_excluded: bool = False
    ) -> ContentSection:
        """
        Transform a single content section and its subsections recursively.

        Args:
            section: ContentSection to transform
            parent_excluded: Whether parent section was excluded

        Returns:
            Transformed ContentSection with include_in_handout flag set
        """
        # Check if this section should be excluded
        exclude_this = self._should_exclude_section(section.title)

        # If parent or this section is excluded, mark for exclusion
        if parent_excluded or exclude_this:
            section.include_in_handout = False
            logger.info(f"Excluding section: {section.title}")

            # Still process subsections (they might be independently excluded)
            section.subsections = [
                self.transform_section(subsection, parent_excluded=True)
                for subsection in section.subsections
            ]

            return section

        # Section is included - clean its content
        # Remove HTML comment blocks
        cleaned_content = self._remove_html_comment_blocks(section.content)

        # Apply transformation rules
        if self.transform_rules:
            cleaned_content = self._apply_transformation_rules(cleaned_content)

        section.content = cleaned_content
        section.include_in_handout = True

        # Recursively transform subsections
        section.subsections = [
            self.transform_section(subsection, parent_excluded=False)
            for subsection in section.subsections
        ]

        return section

    def transform(self, sections: list[ContentSection]) -> list[ContentSection]:
        """
        Transform all content sections.

        Args:
            sections: List of ContentSection objects to transform

        Returns:
            List of transformed ContentSection objects with include_in_handout flags set
        """
        logger.info(f"Transforming {len(sections)} top-level sections")

        transformed_sections = [
            self.transform_section(section)
            for section in sections
        ]

        # Count excluded sections
        total_sections = self._count_sections(sections)
        excluded_sections = self._count_excluded_sections(transformed_sections)

        logger.info(
            f"Transformation complete: {excluded_sections}/{total_sections} "
            f"sections excluded"
        )

        return transformed_sections

    def _count_sections(self, sections: list[ContentSection]) -> int:
        """Count total sections including subsections."""
        count = len(sections)
        for section in sections:
            count += self._count_sections(section.subsections)
        return count

    def _count_excluded_sections(self, sections: list[ContentSection]) -> int:
        """Count excluded sections including subsections."""
        count = sum(1 for s in sections if not s.include_in_handout)
        for section in sections:
            count += self._count_excluded_sections(section.subsections)
        return count

    def get_included_sections(
        self,
        sections: list[ContentSection]
    ) -> list[ContentSection]:
        """
        Filter sections to only those marked for inclusion.

        Args:
            sections: List of transformed ContentSection objects

        Returns:
            List of sections where include_in_handout is True
        """
        included = []

        for section in sections:
            if section.include_in_handout:
                # Recursively filter subsections
                section.subsections = self.get_included_sections(
                    section.subsections
                )
                included.append(section)

        return included

    def get_statistics(self, sections: list[ContentSection]) -> dict[str, int]:
        """
        Get statistics about transformed sections.

        Args:
            sections: List of transformed ContentSection objects

        Returns:
            Dictionary with statistics:
                - total_sections: Total number of sections
                - included_sections: Number of sections included
                - excluded_sections: Number of sections excluded
                - inclusion_rate: Percentage of sections included
        """
        total = self._count_sections(sections)
        excluded = self._count_excluded_sections(sections)
        included = total - excluded

        return {
            'total_sections': total,
            'included_sections': included,
            'excluded_sections': excluded,
            'inclusion_rate': round((included / total * 100) if total > 0 else 0, 1)
        }


def create_transformer(config: dict[str, Any]) -> ContentTransformer:
    """
    Factory function to create a ContentTransformer instance.

    Args:
        config: Configuration dictionary (typically from handout_config.yaml)

    Returns:
        Configured ContentTransformer instance

    Example:
        >>> config = {
        ...     'exclude_patterns': [
        ...         '## Video Production Notes',
        ...         '### For Instructors'
        ...     ],
        ...     'transform_rules': {
        ...         'learners': 'students'
        ...     }
        ... }
        >>> transformer = create_transformer(config)
        >>> sections = transformer.transform(parsed_sections)
    """
    # Extract content transformation config
    content_config = config.get('content', {})

    return ContentTransformer(content_config)
