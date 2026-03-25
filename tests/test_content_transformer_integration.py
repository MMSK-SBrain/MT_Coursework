"""
Integration tests for ContentTransformer with real-world scenarios.

These tests demonstrate the transformer working with realistic framework content
and configuration scenarios.
"""

import pytest
from src.content_transformer import create_transformer
from src.models import ContentSection


class TestContentTransformerIntegration:
    """Integration tests with realistic scenarios."""

    @pytest.fixture
    def realistic_config(self):
        """Configuration matching handout_config.yaml."""
        return {
            'content': {
                'exclude_patterns': [
                    '## Video Production Notes',
                    '### For Instructors',
                    '## Instructor Notes',
                    '## 🎬 Video Production*'
                ],
                'transform_rules': {}
            }
        }

    @pytest.fixture
    def sample_framework_sections(self):
        """Sample framework sections mimicking real ML course content."""
        return [
            ContentSection(
                id="intro",
                level=1,
                title="# Module 0: The Hook - Welcome to Machine Learning",
                content="""
**Course Code:** ML-ENG-M0
**Duration:** 1 week (self-paced)
**Total Video Content:** ~4.5 hours
""",
                subsections=[
                    ContentSection(
                        id="session1",
                        level=2,
                        title="## Session 1: The 5 Amazing Demos",
                        content="""
**Duration:** ~1.5 hours video + 0.5 hour exploration
**Goal:** Create the "WOW" moment

### Video 1: Welcome to Machine Learning (10 min)
**Content:**
- Welcome! Who am I, and why ML?
- What you'll achieve in 17 weeks
- Course philosophy: AI as your coding partner

<!-- INSTRUCTOR ONLY -->
**Production Notes:**
- Use energetic tone
- Show demo preview clips
- Background music: upbeat electronic
<!-- END INSTRUCTOR ONLY -->

Let's dive into the demos!
""",
                        subsections=[
                            ContentSection(
                                id="session1-demo1",
                                level=3,
                                title="### Demo #1 - Stock Price Predictor",
                                content="""
**The Hook:** "Want to make better investment decisions?"

**Demo Flow:**
1. The Problem: Raj wants to predict stock prices
2. The Demo: Show web app predicting AAPL stock
3. The Wow Factor: 78% confidence in 2 seconds
"""
                            ),
                            ContentSection(
                                id="session1-instructor",
                                level=3,
                                title="### For Instructors",
                                content="""
**Assessment Materials:**
- Quiz questions for each demo
- Grading rubrics
- Auto-checker scripts

**Demo Applications:**
- Deployed URLs for all 5 demos
- Maintenance guide
"""
                            )
                        ]
                    ),
                    ContentSection(
                        id="video-production",
                        level=2,
                        title="## Video Production Notes",
                        content="""
### Session 1 (Demos)
- High energy, excitement-focused
- Quick cuts between demos
- Background music (upbeat)

### Session 2 (Setup)
- Slower pace, clear step-by-step
- Pause prompts
"""
                    ),
                    ContentSection(
                        id="session2",
                        level=2,
                        title="## Session 2: Setup Your AI Assistant",
                        content="""
**Duration:** ~1.5 hours
**Goal:** Get tools ready

<!-- INSTRUCTOR -->
Pacing note: Allow 20 minutes for account setup
<!-- /INSTRUCTOR -->

Follow these steps to set up your environment.
"""
                    )
                ]
            )
        ]

    def test_realistic_framework_transformation(
        self,
        realistic_config,
        sample_framework_sections
    ):
        """Test transformation of realistic framework structure."""
        transformer = create_transformer(realistic_config)
        transformed = transformer.transform(sample_framework_sections)

        # Module intro should be included
        assert transformed[0].include_in_handout
        assert "ML-ENG-M0" in transformed[0].content

        # Session 1 should be included but cleaned
        session1 = transformed[0].subsections[0]
        assert session1.include_in_handout
        assert "Welcome to Machine Learning" in session1.content
        assert "Let's dive into the demos!" in session1.content

        # Instructor notes should be removed from session 1
        assert "Production Notes:" not in session1.content
        assert "Use energetic tone" not in session1.content

        # Demo #1 subsection should be included
        demo1 = session1.subsections[0]
        assert demo1.include_in_handout
        assert "Stock Price Predictor" in demo1.title

        # "For Instructors" subsection should be excluded
        instructor_section = session1.subsections[1]
        assert not instructor_section.include_in_handout

        # "Video Production Notes" section should be excluded
        video_prod = transformed[0].subsections[1]
        assert not video_prod.include_in_handout

        # Session 2 should be included but cleaned
        session2 = transformed[0].subsections[2]
        assert session2.include_in_handout
        assert "Follow these steps" in session2.content
        assert "Pacing note" not in session2.content

    def test_get_student_ready_content(
        self,
        realistic_config,
        sample_framework_sections
    ):
        """Test extraction of student-ready content only."""
        transformer = create_transformer(realistic_config)
        transformed = transformer.transform(sample_framework_sections)
        student_sections = transformer.get_included_sections(transformed)

        # Should have 1 top-level section (module intro)
        assert len(student_sections) == 1

        # Should have 2 subsections (Session 1 and Session 2)
        # Video Production Notes excluded
        assert len(student_sections[0].subsections) == 2

        # Session 1 should have 1 subsection (Demo #1)
        # "For Instructors" excluded
        session1 = student_sections[0].subsections[0]
        assert len(session1.subsections) == 1
        assert "Stock Price Predictor" in session1.subsections[0].title

    def test_statistics_on_realistic_content(
        self,
        realistic_config,
        sample_framework_sections
    ):
        """Test statistics calculation on realistic content."""
        transformer = create_transformer(realistic_config)
        transformed = transformer.transform(sample_framework_sections)
        stats = transformer.get_statistics(transformed)

        # Total: 1 module + 3 sessions + 2 subsections = 6 sections
        assert stats['total_sections'] == 6

        # Excluded: "For Instructors" + "Video Production Notes" = 2
        assert stats['excluded_sections'] == 2

        # Included: 4 sections
        assert stats['included_sections'] == 4

        # Rate: 4/6 = 66.7%
        assert stats['inclusion_rate'] == 66.7

    def test_nested_html_comments_in_sections(self, realistic_config):
        """Test HTML comments at various nesting levels."""
        sections = [
            ContentSection(
                id="parent",
                level=2,
                title="## Parent Section",
                content="""
Parent content here.

<!-- INSTRUCTOR ONLY -->
Parent instructor notes.
<!-- END INSTRUCTOR ONLY -->

More parent content.
""",
                subsections=[
                    ContentSection(
                        id="child",
                        level=3,
                        title="### Child Section",
                        content="""
Child content.

<!-- INSTRUCTOR -->
Child instructor notes.
<!-- /INSTRUCTOR -->

More child content.
"""
                    )
                ]
            )
        ]

        transformer = create_transformer(realistic_config)
        transformed = transformer.transform(sections)

        # Both sections included but cleaned
        assert transformed[0].include_in_handout
        assert transformed[0].subsections[0].include_in_handout

        # Parent content cleaned
        assert "Parent content here." in transformed[0].content
        assert "More parent content." in transformed[0].content
        assert "Parent instructor notes." not in transformed[0].content

        # Child content cleaned
        child = transformed[0].subsections[0]
        assert "Child content." in child.content
        assert "More child content." in child.content
        assert "Child instructor notes." not in child.content

    def test_transformation_preserves_markdown_formatting(self, realistic_config):
        """Test that markdown formatting is preserved during transformation."""
        section = ContentSection(
            id="formatted",
            level=2,
            title="## Session with Formatting",
            content="""
# Heading 1
## Heading 2

**Bold text** and *italic text*

- List item 1
- List item 2
  - Nested item

```python
def example():
    return "code block"
```

[Link text](https://example.com)

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |

<!-- INSTRUCTOR ONLY -->
This should be removed.
<!-- END INSTRUCTOR ONLY -->

> Blockquote text
"""
        )

        transformer = create_transformer(realistic_config)
        transformed = transformer.transform_section(section)

        # All markdown formatting should be preserved
        assert "# Heading 1" in transformed.content
        assert "**Bold text**" in transformed.content
        assert "- List item 1" in transformed.content
        assert "```python" in transformed.content
        assert "[Link text]" in transformed.content
        assert "| Column 1 |" in transformed.content
        assert "> Blockquote text" in transformed.content

        # Instructor content should be removed
        assert "This should be removed." not in transformed.content

    def test_empty_configuration_allows_all_content(self):
        """Test that empty config includes all content."""
        config = {
            'content': {
                'exclude_patterns': [],
                'transform_rules': {}
            }
        }

        sections = [
            ContentSection(
                id="s1",
                level=2,
                title="## Video Production Notes",
                content="Production content"
            ),
            ContentSection(
                id="s2",
                level=3,
                title="### For Instructors",
                content="Instructor content"
            )
        ]

        transformer = create_transformer(config)
        transformed = transformer.transform(sections)

        # With no exclusion patterns, all sections included
        assert all(s.include_in_handout for s in transformed)

    def test_case_variations_in_patterns(self, realistic_config):
        """Test case-insensitive matching of various pattern formats."""
        test_titles = [
            "## VIDEO PRODUCTION NOTES",
            "## video production notes",
            "## Video Production Notes",
            "### FOR INSTRUCTORS",
            "### for instructors",
            "### For Instructors",
            "## Instructor notes",
            "## INSTRUCTOR NOTES"
        ]

        transformer = create_transformer(realistic_config)

        for title in test_titles:
            section = ContentSection(
                id="test",
                level=2,
                title=title,
                content="Content"
            )
            transformed = transformer.transform_section(section)
            assert not transformed.include_in_handout, \
                f"Title '{title}' should be excluded but wasn't"
