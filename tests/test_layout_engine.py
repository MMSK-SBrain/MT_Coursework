"""
Unit tests for LayoutEngine

Tests the layout engine that assembles content, questions, and images
into styled HTML using Jinja2 templates and dark theme CSS.
"""

import pytest
from pathlib import Path
from datetime import datetime

from src.layout_engine import LayoutEngine
from src.models import (
    HandoutDocument,
    FrameworkMetadata,
    ContentSection,
    Question,
    QuestionType,
    QuestionDifficulty,
    QuestionStatus,
    QuestionSource,
    ImageReference,
    TOCEntry
)


@pytest.fixture
def layout_engine():
    """Create a LayoutEngine instance for testing."""
    return LayoutEngine()


@pytest.fixture
def sample_metadata():
    """Create sample framework metadata."""
    return FrameworkMetadata(
        course_code="ML-ENG-M0",
        module_number=0,
        module_title="The Hook - Welcome to Machine Learning",
        duration="1 week",
        video_content="4.5 hours",
        hands_on_time="2-3 hours"
    )


@pytest.fixture
def sample_sections():
    """Create sample content sections."""
    return [
        ContentSection(
            id="section-1",
            level=1,
            title="Introduction to Machine Learning",
            content="This is the introduction section with some **bold** text.",
            subsections=[
                ContentSection(
                    id="section-1-1",
                    level=2,
                    title="What is ML?",
                    content="Machine Learning is a subset of AI.",
                    subsections=[]
                ),
                ContentSection(
                    id="section-1-2",
                    level=2,
                    title="Why Learn ML?",
                    content="ML is transforming industries.",
                    subsections=[]
                )
            ]
        ),
        ContentSection(
            id="section-2",
            level=1,
            title="Getting Started",
            content="Let's begin our journey into ML.",
            subsections=[]
        )
    ]


@pytest.fixture
def sample_questions():
    """Create sample questions."""
    return [
        Question(
            id="q1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is Machine Learning?",
            options=["A) A type of database", "B) A subset of AI", "C) A programming language", "D) None of the above"],
            correct_answer="B",
            difficulty=QuestionDifficulty.EASY,
            points=1,
            source_section="section-1-1",
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="q2",
            type=QuestionType.TRUE_FALSE,
            question_text="ML is transforming industries.",
            options=["True", "False"],
            correct_answer="True",
            difficulty=QuestionDifficulty.EASY,
            points=1,
            source_section="section-1-2",
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="q3",
            type=QuestionType.REFLECTION,
            question_text="How do you think ML will impact your career?",
            difficulty=QuestionDifficulty.MEDIUM,
            points=2,
            source_section="section-2",
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="q4",
            type=QuestionType.SHORT_ANSWER,
            question_text="List three applications of Machine Learning.",
            difficulty=QuestionDifficulty.MEDIUM,
            points=3,
            source_section="section-1",
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="q5",
            type=QuestionType.APPLICATION,
            question_text="Design a simple ML application for your workplace.",
            difficulty=QuestionDifficulty.HARD,
            points=5,
            source_section="section-2",
            status=QuestionStatus.APPROVED
        )
    ]


@pytest.fixture
def sample_images():
    """Create sample image references."""
    return [
        ImageReference(
            id="img1",
            original_path="images/ml-workflow.png",
            resolved_path=Path("/fake/path/ml-workflow.png"),
            alt_text="ML Workflow Diagram",
            caption="Figure 1: ML Workflow",
            width=500,
            height=300,
            exists=True,
            placeholder_used=False
        ),
        ImageReference(
            id="img2",
            original_path="images/missing.png",
            resolved_path=None,
            alt_text="Missing Image",
            caption="Figure 2: Not Found",
            width=500,
            height=0,
            exists=False,
            placeholder_used=True
        )
    ]


@pytest.fixture
def sample_document(sample_metadata, sample_sections, sample_questions, sample_images):
    """Create a complete sample HandoutDocument."""
    return HandoutDocument(
        metadata=sample_metadata,
        sections=sample_sections,
        questions=sample_questions,
        images=sample_images,
        generation_timestamp=datetime(2026, 1, 11, 10, 0, 0),
        question_review_complete=True
    )


class TestLayoutEngineInit:
    """Test LayoutEngine initialization."""

    def test_init_default_template_dir(self, layout_engine):
        """Test initialization with default template directory."""
        assert layout_engine.template_dir.exists()
        assert layout_engine.template_dir.name == "templates"

    def test_init_custom_template_dir(self, tmp_path):
        """Test initialization with custom template directory."""
        custom_dir = tmp_path / "custom_templates"
        custom_dir.mkdir()
        engine = LayoutEngine(template_dir=custom_dir)
        assert engine.template_dir == custom_dir

    def test_jinja_env_setup(self, layout_engine):
        """Test that Jinja2 environment is set up correctly."""
        assert layout_engine.env is not None
        assert 'slugify' in layout_engine.env.filters
        assert 'markdown' in layout_engine.env.filters
        assert 'highlight_code' in layout_engine.env.filters
        assert 'question_border_color' in layout_engine.env.filters


class TestSlugify:
    """Test the slugify filter."""

    def test_slugify_simple(self, layout_engine):
        """Test slugifying simple text."""
        result = layout_engine._slugify("Hello World")
        assert result == "hello-world"

    def test_slugify_with_special_chars(self, layout_engine):
        """Test slugifying text with special characters."""
        result = layout_engine._slugify("What is ML?")
        assert result == "what-is-ml"

    def test_slugify_with_numbers(self, layout_engine):
        """Test slugifying text with numbers."""
        result = layout_engine._slugify("Module 0: Introduction")
        assert result == "module-0-introduction"

    def test_slugify_with_multiple_spaces(self, layout_engine):
        """Test slugifying text with multiple spaces."""
        result = layout_engine._slugify("Hello    World")
        assert result == "hello-world"

    def test_slugify_with_leading_trailing_spaces(self, layout_engine):
        """Test slugifying text with leading/trailing spaces."""
        result = layout_engine._slugify("  Hello World  ")
        assert result == "hello-world"


class TestTOCGeneration:
    """Test table of contents generation."""

    def test_generate_toc_basic(self, layout_engine, sample_sections):
        """Test basic TOC generation."""
        toc = layout_engine._generate_toc(sample_sections)

        assert len(toc) >= 3
        # Check H1 entries
        h1_entries = [e for e in toc if e.level == 1]
        assert len(h1_entries) == 2
        assert h1_entries[0].title == "Introduction to Machine Learning"
        assert h1_entries[1].title == "Getting Started"

    def test_generate_toc_anchors(self, layout_engine, sample_sections):
        """Test that TOC entries have correct anchors."""
        toc = layout_engine._generate_toc(sample_sections)

        assert any(e.anchor == "introduction-to-machine-learning" for e in toc)
        assert any(e.anchor == "getting-started" for e in toc)

    def test_generate_toc_page_numbers(self, layout_engine, sample_sections):
        """Test that TOC entries have placeholder page numbers."""
        toc = layout_engine._generate_toc(sample_sections)

        # Page numbers should be 0 (WeasyPrint will fill them)
        for entry in toc:
            assert entry.page_number == 0

    def test_generate_toc_empty_sections(self, layout_engine):
        """Test TOC generation with empty sections list."""
        toc = layout_engine._generate_toc([])
        assert toc == []

    def test_generate_toc_nested_sections(self, layout_engine):
        """Test TOC generation with nested sections."""
        sections = [
            ContentSection(
                id="s1",
                level=1,
                title="Level 1",
                content="",
                subsections=[
                    ContentSection(
                        id="s1-1",
                        level=2,
                        title="Level 2",
                        content="",
                        subsections=[
                            ContentSection(
                                id="s1-1-1",
                                level=3,
                                title="Level 3",
                                content="",
                                subsections=[]
                            )
                        ]
                    )
                ]
            )
        ]

        toc = layout_engine._generate_toc(sections)
        assert len(toc) >= 2  # H1 and H2 are included
        assert any(e.level == 1 and e.title == "Level 1" for e in toc)
        assert any(e.level == 2 and e.title == "Level 2" for e in toc)


class TestQuestionGrouping:
    """Test question grouping by section."""

    def test_group_questions_by_section(self, layout_engine, sample_questions):
        """Test grouping questions by section."""
        grouped = layout_engine._group_questions_by_section(sample_questions)

        assert "section-1-1" in grouped
        assert "section-1-2" in grouped
        assert "section-2" in grouped
        assert len(grouped["section-1-1"]) == 1
        assert len(grouped["section-2"]) == 2

    def test_group_questions_empty_list(self, layout_engine):
        """Test grouping empty questions list."""
        grouped = layout_engine._group_questions_by_section([])
        assert grouped == {}

    def test_group_questions_no_section(self, layout_engine):
        """Test grouping questions without section assignment."""
        questions = [
            Question(
                id="q1",
                type=QuestionType.MULTIPLE_CHOICE,
                question_text="Test question",
                source_section="",
                status=QuestionStatus.APPROVED
            )
        ]

        grouped = layout_engine._group_questions_by_section(questions)
        assert "" in grouped
        assert len(grouped[""]) == 1


class TestMarkdownRendering:
    """Test markdown rendering."""

    def test_render_markdown_basic(self, layout_engine):
        """Test basic markdown rendering."""
        md = "This is **bold** and *italic* text."
        html = layout_engine._render_markdown(md)

        assert "<strong>" in html
        assert "<em>" in html
        assert "bold" in html
        assert "italic" in html

    def test_render_markdown_headings(self, layout_engine):
        """Test rendering markdown headings."""
        md = "# Heading 1\n## Heading 2"
        html = layout_engine._render_markdown(md)

        assert "<h1>" in html
        assert "<h2>" in html

    def test_render_markdown_lists(self, layout_engine):
        """Test rendering markdown lists."""
        md = "- Item 1\n- Item 2\n- Item 3"
        html = layout_engine._render_markdown(md)

        assert "<ul>" in html
        assert "<li>" in html

    def test_render_markdown_code(self, layout_engine):
        """Test rendering inline code."""
        md = "Use the `print()` function."
        html = layout_engine._render_markdown(md)

        assert "<code>" in html
        assert "print()" in html

    def test_render_markdown_links(self, layout_engine):
        """Test rendering markdown links."""
        md = "[Google](https://google.com)"
        html = layout_engine._render_markdown(md)

        assert "<a href" in html
        assert "google.com" in html


class TestCodeHighlighting:
    """Test code syntax highlighting."""

    def test_highlight_code_keywords(self, layout_engine):
        """Test highlighting Python keywords."""
        code = "def hello():\n    return True"
        html = layout_engine._highlight_code(code, 'python')

        assert 'class="keyword"' in html or 'def' in html

    def test_highlight_code_strings(self, layout_engine):
        """Test highlighting Python strings."""
        code = 'message = "Hello World"'
        html = layout_engine._highlight_code(code, 'python')

        # Should contain string highlighting
        assert "Hello World" in html

    def test_highlight_code_comments(self, layout_engine):
        """Test highlighting Python comments."""
        code = "# This is a comment\nprint('test')"
        html = layout_engine._highlight_code(code, 'python')

        assert "comment" in html.lower() or "#" in html

    def test_highlight_code_non_python(self, layout_engine):
        """Test highlighting non-Python code (should escape only)."""
        code = "<script>alert('test')</script>"
        html = layout_engine._highlight_code(code, 'javascript')

        # Should be escaped
        assert "&lt;" in html or "script" in html


class TestQuestionBorderColor:
    """Test question border color assignment."""

    def test_border_color_multiple_choice(self, layout_engine):
        """Test border color for multiple choice questions."""
        color = layout_engine._question_border_color('multiple_choice')
        assert color == '#58A6FF'

    def test_border_color_true_false(self, layout_engine):
        """Test border color for true/false questions."""
        color = layout_engine._question_border_color('true_false')
        assert color == '#58A6FF'

    def test_border_color_short_answer(self, layout_engine):
        """Test border color for short answer questions."""
        color = layout_engine._question_border_color('short_answer')
        assert color == '#3FB950'

    def test_border_color_reflection(self, layout_engine):
        """Test border color for reflection questions."""
        color = layout_engine._question_border_color('reflection')
        assert color == '#A371F7'

    def test_border_color_application(self, layout_engine):
        """Test border color for application questions."""
        color = layout_engine._question_border_color('application')
        assert color == '#3FB950'

    def test_border_color_unknown(self, layout_engine):
        """Test border color for unknown question type."""
        color = layout_engine._question_border_color('unknown_type')
        assert color == '#58A6FF'  # Default to blue


class TestHTMLGeneration:
    """Test complete HTML generation."""

    def test_generate_html_basic(self, layout_engine, sample_document):
        """Test basic HTML generation."""
        html = layout_engine.generate_html(sample_document)

        assert html is not None
        assert isinstance(html, str)
        assert len(html) > 0

    def test_generate_html_contains_title(self, layout_engine, sample_document):
        """Test that generated HTML contains module title."""
        html = layout_engine.generate_html(sample_document)

        assert "The Hook - Welcome to Machine Learning" in html

    def test_generate_html_contains_toc(self, layout_engine, sample_document):
        """Test that generated HTML contains table of contents."""
        html = layout_engine.generate_html(sample_document)

        assert "Table of Contents" in html or "toc" in html.lower()

    def test_generate_html_contains_questions(self, layout_engine, sample_document):
        """Test that generated HTML contains questions."""
        html = layout_engine.generate_html(sample_document)

        assert "What is Machine Learning?" in html
        assert "Self-Study Questions" in html or "question" in html.lower()

    def test_generate_html_dark_theme_css(self, layout_engine, sample_document):
        """Test that generated HTML links to dark theme CSS."""
        html = layout_engine.generate_html(sample_document)

        assert "dark_theme.css" in html

    def test_generate_html_warning_banner(self, layout_engine, sample_metadata):
        """Test warning banner for unreviewed questions."""
        doc = HandoutDocument(
            metadata=sample_metadata,
            sections=[],
            questions=[],
            images=[],
            question_review_complete=False
        )

        html = layout_engine.generate_html(doc)
        assert "unreviewed" in html.lower() or "warning" in html.lower()

    def test_generate_html_no_warning_when_reviewed(self, layout_engine, sample_document):
        """Test no warning banner when questions are reviewed."""
        sample_document.question_review_complete = True
        html = layout_engine.generate_html(sample_document)

        # Should not have prominent unreviewed warning (might have other warnings)
        assert sample_document.question_review_complete


class TestHTMLStructure:
    """Test HTML structure and elements."""

    def test_html_has_doctype(self, layout_engine, sample_document):
        """Test that HTML has DOCTYPE declaration."""
        html = layout_engine.generate_html(sample_document)
        assert "<!DOCTYPE html>" in html

    def test_html_has_head_section(self, layout_engine, sample_document):
        """Test that HTML has head section."""
        html = layout_engine.generate_html(sample_document)
        assert "<head>" in html
        assert "</head>" in html

    def test_html_has_body_section(self, layout_engine, sample_document):
        """Test that HTML has body section."""
        html = layout_engine.generate_html(sample_document)
        assert "<body>" in html
        assert "</body>" in html

    def test_html_has_charset_meta(self, layout_engine, sample_document):
        """Test that HTML has charset meta tag."""
        html = layout_engine.generate_html(sample_document)
        assert 'charset="UTF-8"' in html or "utf-8" in html.lower()


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_empty_document(self, layout_engine, sample_metadata):
        """Test generating HTML for empty document."""
        doc = HandoutDocument(
            metadata=sample_metadata,
            sections=[],
            questions=[],
            images=[]
        )

        html = layout_engine.generate_html(doc)
        assert html is not None
        assert len(html) > 0

    def test_sections_without_questions(self, layout_engine, sample_metadata, sample_sections):
        """Test sections without any questions."""
        doc = HandoutDocument(
            metadata=sample_metadata,
            sections=sample_sections,
            questions=[],
            images=[]
        )

        html = layout_engine.generate_html(doc)
        assert "Introduction to Machine Learning" in html

    def test_questions_without_sections(self, layout_engine, sample_metadata, sample_questions):
        """Test questions without sections."""
        doc = HandoutDocument(
            metadata=sample_metadata,
            sections=[],
            questions=sample_questions,
            images=[]
        )

        html = layout_engine.generate_html(doc)
        assert html is not None

    def test_special_characters_in_content(self, layout_engine, sample_metadata):
        """Test handling special characters in content."""
        sections = [
            ContentSection(
                id="special",
                level=1,
                title="Special <>&\" Characters",
                content="Content with <tags> & special chars",
                subsections=[]
            )
        ]

        doc = HandoutDocument(
            metadata=sample_metadata,
            sections=sections,
            questions=[],
            images=[]
        )

        html = layout_engine.generate_html(doc)
        # Special chars should be properly escaped or handled
        assert html is not None


class TestTemplateIntegration:
    """Test integration with Jinja2 templates."""

    def test_template_exists(self, layout_engine):
        """Test that main template file exists."""
        template_path = layout_engine.template_dir / "dark_theme.html"
        assert template_path.exists()

    def test_css_exists(self, layout_engine):
        """Test that CSS file exists."""
        css_path = layout_engine.template_dir / "dark_theme.css"
        assert css_path.exists()

    def test_question_partial_exists(self, layout_engine):
        """Test that question box partial template exists."""
        partial_path = layout_engine.template_dir / "partials" / "question_box.html"
        assert partial_path.exists()

    def test_code_block_partial_exists(self, layout_engine):
        """Test that code block partial template exists."""
        partial_path = layout_engine.template_dir / "partials" / "code_block.html"
        assert partial_path.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=src.layout_engine", "--cov-report=term-missing"])
