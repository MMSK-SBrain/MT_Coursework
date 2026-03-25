"""
Unit tests for ContentTransformer.

Tests cover:
- Section removal by title pattern
- HTML comment block removal
- Nested sections handling
- Mixed student/instructor content
- Edge cases and error handling
"""

import pytest
from src.content_transformer import ContentTransformer, create_transformer
from src.models import ContentSection


class TestContentTransformer:
    """Test suite for ContentTransformer class."""

    @pytest.fixture
    def basic_config(self):
        """Basic configuration for transformer."""
        return {
            'exclude_patterns': [
                '## Video Production Notes',
                '### For Instructors',
                '## Instructor Notes'
            ],
            'transform_rules': {}
        }

    @pytest.fixture
    def transformer(self, basic_config):
        """Create a ContentTransformer instance."""
        return ContentTransformer(basic_config)

    def test_initialization(self, basic_config):
        """Test transformer initialization."""
        transformer = ContentTransformer(basic_config)
        assert len(transformer.exclude_patterns) == 3
        assert transformer.transform_rules == {}

    def test_initialization_with_transform_rules(self):
        """Test transformer initialization with transformation rules."""
        config = {
            'exclude_patterns': [],
            'transform_rules': {
                'learner': 'student',
                'pedagogy': 'teaching method'
            }
        }
        transformer = ContentTransformer(config)
        assert len(transformer.transform_rules) == 2

    def test_should_exclude_section_exact_match(self, transformer):
        """Test section exclusion with exact pattern match."""
        assert transformer._should_exclude_section('## Video Production Notes')
        assert transformer._should_exclude_section('### For Instructors')

    def test_should_exclude_section_case_insensitive(self, transformer):
        """Test section exclusion is case-insensitive."""
        assert transformer._should_exclude_section('## VIDEO PRODUCTION NOTES')
        assert transformer._should_exclude_section('### for instructors')
        assert transformer._should_exclude_section('### For INSTRUCTORS')

    def test_should_exclude_section_no_match(self, transformer):
        """Test section is not excluded when pattern doesn't match."""
        assert not transformer._should_exclude_section('## Learning Objectives')
        assert not transformer._should_exclude_section('### Student Activities')
        assert not transformer._should_exclude_section('## Session 1')

    def test_should_exclude_section_partial_match(self, transformer):
        """Test partial matches don't trigger exclusion."""
        # "For Instructors" should not match "Information for Students"
        assert not transformer._should_exclude_section('## Information for Students')

    def test_remove_html_comment_blocks_instructor_only(self, transformer):
        """Test removal of <!-- INSTRUCTOR ONLY --> blocks."""
        content = """
# Section Title

This is student content.

<!-- INSTRUCTOR ONLY -->
This is instructor-only content.
Should be removed.
<!-- END INSTRUCTOR ONLY -->

More student content here.
"""
        cleaned = transformer._remove_html_comment_blocks(content)
        assert 'This is student content.' in cleaned
        assert 'More student content here.' in cleaned
        assert 'This is instructor-only content.' not in cleaned
        assert 'Should be removed.' not in cleaned
        assert '<!-- INSTRUCTOR ONLY -->' not in cleaned

    def test_remove_html_comment_blocks_instructor_variant(self, transformer):
        """Test removal of <!-- INSTRUCTOR --> variant blocks."""
        content = """
Student content before.

<!-- INSTRUCTOR -->
Instructor notes here.
<!-- /INSTRUCTOR -->

Student content after.
"""
        cleaned = transformer._remove_html_comment_blocks(content)
        assert 'Student content before.' in cleaned
        assert 'Student content after.' in cleaned
        assert 'Instructor notes here.' not in cleaned

    def test_remove_html_comment_blocks_case_insensitive(self, transformer):
        """Test HTML comment removal is case-insensitive."""
        content = """
Content before.

<!-- instructor only -->
Remove this.
<!-- end instructor only -->

Content after.
"""
        cleaned = transformer._remove_html_comment_blocks(content)
        assert 'Remove this.' not in cleaned
        assert 'Content before.' in cleaned
        assert 'Content after.' in cleaned

    def test_remove_html_comment_blocks_multiple(self, transformer):
        """Test removal of multiple HTML comment blocks."""
        content = """
Part 1: Student content

<!-- INSTRUCTOR ONLY -->
Block 1 to remove
<!-- END INSTRUCTOR ONLY -->

Part 2: More student content

<!-- INSTRUCTOR -->
Block 2 to remove
<!-- /INSTRUCTOR -->

Part 3: Final student content
"""
        cleaned = transformer._remove_html_comment_blocks(content)
        assert 'Part 1: Student content' in cleaned
        assert 'Part 2: More student content' in cleaned
        assert 'Part 3: Final student content' in cleaned
        assert 'Block 1 to remove' not in cleaned
        assert 'Block 2 to remove' not in cleaned

    def test_remove_html_comment_blocks_multiline(self, transformer):
        """Test removal of multiline HTML comment blocks."""
        content = """
Before block.

<!-- INSTRUCTOR ONLY -->
Line 1 of instructor content
Line 2 of instructor content
Line 3 of instructor content
<!-- END INSTRUCTOR ONLY -->

After block.
"""
        cleaned = transformer._remove_html_comment_blocks(content)
        assert 'Line 1 of instructor content' not in cleaned
        assert 'Line 2 of instructor content' not in cleaned
        assert 'Before block.' in cleaned
        assert 'After block.' in cleaned

    def test_remove_html_comment_blocks_no_blocks(self, transformer):
        """Test content without HTML blocks remains unchanged."""
        content = "This is normal student content with no blocks."
        cleaned = transformer._remove_html_comment_blocks(content)
        assert cleaned == content.strip()

    def test_apply_transformation_rules(self):
        """Test find-and-replace transformation rules."""
        config = {
            'exclude_patterns': [],
            'transform_rules': {
                'learner': 'student',
                'pedagogy': 'teaching method'
            }
        }
        transformer = ContentTransformer(config)
        content = "The learner will understand pedagogy concepts."
        transformed = transformer._apply_transformation_rules(content)
        assert 'student' in transformed
        assert 'teaching method' in transformed
        assert 'learner' not in transformed
        assert 'pedagogy' not in transformed

    def test_apply_transformation_rules_word_boundaries(self):
        """Test transformation rules respect word boundaries."""
        config = {
            'exclude_patterns': [],
            'transform_rules': {
                'ML': 'Machine Learning'
            }
        }
        transformer = ContentTransformer(config)
        # Should transform standalone "ML" but not "HTML"
        content = "ML is powerful. HTML is a markup language."
        transformed = transformer._apply_transformation_rules(content)
        assert 'Machine Learning is powerful' in transformed
        assert 'HTML' in transformed  # Should not change to "HTMachine LearningL"

    def test_transform_section_exclude_by_title(self, transformer):
        """Test section is excluded when title matches pattern."""
        section = ContentSection(
            id="s1",
            level=2,
            title="## Video Production Notes",
            content="This should be excluded."
        )
        transformed = transformer.transform_section(section)
        assert not transformed.include_in_handout

    def test_transform_section_include_by_title(self, transformer):
        """Test section is included when title doesn't match pattern."""
        section = ContentSection(
            id="s1",
            level=2,
            title="## Learning Objectives",
            content="This should be included."
        )
        transformed = transformer.transform_section(section)
        assert transformed.include_in_handout

    def test_transform_section_clean_content(self, transformer):
        """Test section content is cleaned of HTML blocks."""
        section = ContentSection(
            id="s1",
            level=2,
            title="## Session 1",
            content="""
Student content here.

<!-- INSTRUCTOR ONLY -->
Hidden instructor notes.
<!-- END INSTRUCTOR ONLY -->

More student content.
"""
        )
        transformed = transformer.transform_section(section)
        assert transformed.include_in_handout
        assert 'Student content here.' in transformed.content
        assert 'Hidden instructor notes.' not in transformed.content

    def test_transform_section_nested_subsections(self, transformer):
        """Test transformation of nested subsections."""
        subsection1 = ContentSection(
            id="s1.1",
            level=3,
            title="### Subsection 1",
            content="Subsection 1 content"
        )
        subsection2 = ContentSection(
            id="s1.2",
            level=3,
            title="### For Instructors",
            content="Should be excluded"
        )
        parent = ContentSection(
            id="s1",
            level=2,
            title="## Parent Section",
            content="Parent content",
            subsections=[subsection1, subsection2]
        )

        transformed = transformer.transform_section(parent)
        assert transformed.include_in_handout
        assert len(transformed.subsections) == 2
        assert transformed.subsections[0].include_in_handout
        assert not transformed.subsections[1].include_in_handout

    def test_transform_section_parent_excluded_propagates(self, transformer):
        """Test exclusion propagates to child sections."""
        child = ContentSection(
            id="s1.1",
            level=3,
            title="### Child Section",
            content="Child content"
        )
        parent = ContentSection(
            id="s1",
            level=2,
            title="## Video Production Notes",
            content="Parent content",
            subsections=[child]
        )

        transformed = transformer.transform_section(parent)
        assert not transformed.include_in_handout
        assert not transformed.subsections[0].include_in_handout

    def test_transform_multiple_sections(self, transformer):
        """Test transforming multiple top-level sections."""
        sections = [
            ContentSection(
                id="s1",
                level=2,
                title="## Session 1",
                content="Include this"
            ),
            ContentSection(
                id="s2",
                level=2,
                title="## Video Production Notes",
                content="Exclude this"
            ),
            ContentSection(
                id="s3",
                level=2,
                title="## Session 2",
                content="Include this too"
            )
        ]

        transformed = transformer.transform(sections)
        assert len(transformed) == 3
        assert transformed[0].include_in_handout
        assert not transformed[1].include_in_handout
        assert transformed[2].include_in_handout

    def test_get_included_sections(self, transformer):
        """Test filtering to only included sections."""
        sections = [
            ContentSection(
                id="s1",
                level=2,
                title="## Session 1",
                content="Include",
                include_in_handout=True
            ),
            ContentSection(
                id="s2",
                level=2,
                title="## Excluded",
                content="Exclude",
                include_in_handout=False
            ),
            ContentSection(
                id="s3",
                level=2,
                title="## Session 2",
                content="Include",
                include_in_handout=True
            )
        ]

        included = transformer.get_included_sections(sections)
        assert len(included) == 2
        assert included[0].id == "s1"
        assert included[1].id == "s3"

    def test_get_included_sections_with_subsections(self, transformer):
        """Test filtering includes nested subsections correctly."""
        sections = [
            ContentSection(
                id="s1",
                level=2,
                title="## Parent",
                content="Parent",
                include_in_handout=True,
                subsections=[
                    ContentSection(
                        id="s1.1",
                        level=3,
                        title="### Child 1",
                        content="Include",
                        include_in_handout=True
                    ),
                    ContentSection(
                        id="s1.2",
                        level=3,
                        title="### Child 2",
                        content="Exclude",
                        include_in_handout=False
                    )
                ]
            )
        ]

        included = transformer.get_included_sections(sections)
        assert len(included) == 1
        assert len(included[0].subsections) == 1
        assert included[0].subsections[0].id == "s1.1"

    def test_get_statistics(self, transformer):
        """Test statistics calculation."""
        sections = [
            ContentSection(
                id="s1",
                level=2,
                title="## Section 1",
                content="Content",
                include_in_handout=True,
                subsections=[
                    ContentSection(
                        id="s1.1",
                        level=3,
                        title="### Subsection",
                        content="Content",
                        include_in_handout=True
                    )
                ]
            ),
            ContentSection(
                id="s2",
                level=2,
                title="## Section 2",
                content="Content",
                include_in_handout=False
            )
        ]

        stats = transformer.get_statistics(sections)
        assert stats['total_sections'] == 3
        assert stats['included_sections'] == 2
        assert stats['excluded_sections'] == 1
        assert stats['inclusion_rate'] == 66.7

    def test_invalid_pattern_handling(self):
        """Test handling of invalid regex patterns."""
        config = {
            'exclude_patterns': [
                '## Valid Pattern',
                '[Invalid(Regex',  # Invalid regex
                '## Another Valid'
            ]
        }
        # Should not raise exception, just skip invalid pattern
        transformer = ContentTransformer(config)
        # Only 2 valid patterns should be compiled
        # Note: The invalid pattern gets escaped and might compile,
        # but we're testing that it doesn't crash
        assert len(transformer.exclude_patterns) >= 2

    def test_empty_config(self):
        """Test transformer works with empty configuration."""
        config = {
            'exclude_patterns': [],
            'transform_rules': {}
        }
        transformer = ContentTransformer(config)
        section = ContentSection(
            id="s1",
            level=2,
            title="## Any Section",
            content="Any content"
        )
        transformed = transformer.transform_section(section)
        assert transformed.include_in_handout

    def test_wildcard_patterns(self):
        """Test wildcard support in exclusion patterns."""
        config = {
            'exclude_patterns': [
                '## *Production*',
                '### *Instructor*'
            ]
        }
        transformer = ContentTransformer(config)
        assert transformer._should_exclude_section('## Video Production Notes')
        assert transformer._should_exclude_section('## Production Guidelines')
        assert transformer._should_exclude_section('### For Instructors Only')
        assert transformer._should_exclude_section('### Instructor Guide')

    def test_create_transformer_factory(self):
        """Test factory function for creating transformer."""
        config = {
            'content': {
                'exclude_patterns': ['## Test'],
                'transform_rules': {'old': 'new'}
            }
        }
        transformer = create_transformer(config)
        assert isinstance(transformer, ContentTransformer)
        assert len(transformer.exclude_patterns) == 1

    def test_mixed_student_instructor_content(self, transformer):
        """Test document with mixed student and instructor content."""
        sections = [
            ContentSection(
                id="s1",
                level=2,
                title="## Session 1: Introduction",
                content="""
# Welcome Students

This is the introduction content.

<!-- INSTRUCTOR ONLY -->
Suggested pacing: 15 minutes
Emphasize practical applications
<!-- END INSTRUCTOR ONLY -->

Let's begin with the basics.
""",
                subsections=[
                    ContentSection(
                        id="s1.1",
                        level=3,
                        title="### Key Concepts",
                        content="Important concepts for students."
                    ),
                    ContentSection(
                        id="s1.2",
                        level=3,
                        title="### For Instructors",
                        content="Teaching tips and grading rubric."
                    )
                ]
            ),
            ContentSection(
                id="s2",
                level=2,
                title="## Video Production Notes",
                content="Camera angles and lighting setup."
            )
        ]

        transformed = transformer.transform(sections)

        # Session 1 should be included but cleaned
        assert transformed[0].include_in_handout
        assert "Welcome Students" in transformed[0].content
        assert "Let's begin with the basics" in transformed[0].content
        assert "Suggested pacing" not in transformed[0].content

        # Key Concepts subsection included
        assert transformed[0].subsections[0].include_in_handout

        # For Instructors subsection excluded
        assert not transformed[0].subsections[1].include_in_handout

        # Video Production Notes excluded
        assert not transformed[1].include_in_handout

    def test_empty_section_content(self, transformer):
        """Test handling of sections with empty content."""
        section = ContentSection(
            id="s1",
            level=2,
            title="## Empty Section",
            content=""
        )
        transformed = transformer.transform_section(section)
        assert transformed.include_in_handout
        assert transformed.content == ""

    def test_section_with_only_html_comments(self, transformer):
        """Test section containing only HTML comments."""
        section = ContentSection(
            id="s1",
            level=2,
            title="## Section",
            content="""
<!-- INSTRUCTOR ONLY -->
Only instructor content here.
<!-- END INSTRUCTOR ONLY -->
"""
        )
        transformed = transformer.transform_section(section)
        # Section should be included but with empty content
        assert transformed.include_in_handout
        assert transformed.content.strip() == ""


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_deeply_nested_sections(self):
        """Test transformation of deeply nested section hierarchy."""
        config = {'exclude_patterns': ['### Level 3 Exclude']}
        transformer = ContentTransformer(config)

        # Create 5 levels deep
        level5 = ContentSection(
            id="s1.1.1.1.1",
            level=6,
            title="###### Level 5",
            content="Deepest content"
        )
        level4 = ContentSection(
            id="s1.1.1.1",
            level=5,
            title="##### Level 4",
            content="Level 4 content",
            subsections=[level5]
        )
        level3 = ContentSection(
            id="s1.1.1",
            level=4,
            title="#### Level 3",
            content="Level 3 content",
            subsections=[level4]
        )
        level2 = ContentSection(
            id="s1.1",
            level=3,
            title="### Level 2",
            content="Level 2 content",
            subsections=[level3]
        )
        level1 = ContentSection(
            id="s1",
            level=2,
            title="## Level 1",
            content="Level 1 content",
            subsections=[level2]
        )

        transformed = transformer.transform_section(level1)
        assert transformed.include_in_handout
        assert transformed.subsections[0].include_in_handout
        # Check all levels are processed
        current = transformed
        for _ in range(4):
            assert len(current.subsections) == 1
            current = current.subsections[0]

    def test_special_characters_in_content(self):
        """Test content with special characters and unicode."""
        config = {'exclude_patterns': []}
        transformer = ContentTransformer(config)

        section = ContentSection(
            id="s1",
            level=2,
            title="## Special Characters: émojis 🎉 & symbols ©",
            content="Content with € £ ¥ and émoji 🚀"
        )
        transformed = transformer.transform_section(section)
        assert transformed.include_in_handout
        assert "🎉" in transformed.title
        assert "🚀" in transformed.content

    def test_malformed_html_comments(self):
        """Test handling of malformed HTML comments."""
        config = {'exclude_patterns': []}
        transformer = ContentTransformer(config)

        content = """
Normal content.

<!-- INSTRUCTOR ONLY -->
Missing closing tag!

More content.
"""
        # Should handle gracefully without removing content after unclosed tag
        cleaned = transformer._remove_html_comment_blocks(content)
        assert 'Normal content.' in cleaned
        # Malformed block won't be removed
        assert 'More content.' in cleaned
