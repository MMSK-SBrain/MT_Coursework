"""
Layout Engine for Student Handout Generator

Assembles content, questions, and images into styled HTML using Jinja2 templates
and dark theme CSS, ready for PDF rendering.

Story 6: Layout Engine
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown
from datetime import datetime

from .models import (
    HandoutDocument,
    ContentSection,
    Question,
    ImageReference,
    TOCEntry,
    QuestionType
)


class LayoutEngine:
    """
    Assembles content, questions, and images into styled HTML.

    Features:
    - Generates table of contents with hyperlinks
    - Renders content sections hierarchically (H1-H6)
    - Inserts question boxes at appropriate locations
    - Embeds images with captions
    - Applies dark theme styling
    - Handles pagination and page breaks
    - Renders code blocks with syntax highlighting
    - Generates headers/footers with metadata
    """

    def __init__(self, template_dir: Optional[Path] = None):
        """
        Initialize the layout engine.

        Args:
            template_dir: Directory containing Jinja2 templates.
                         Defaults to ./templates relative to this file.
        """
        if template_dir is None:
            # Default to templates directory in project root
            template_dir = Path(__file__).parent.parent / "templates"

        self.template_dir = Path(template_dir)

        # Set up Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=select_autoescape(['html', 'xml'])
        )

        # Register custom filters
        self.env.filters['slugify'] = self._slugify
        self.env.filters['markdown'] = self._render_markdown
        self.env.filters['highlight_code'] = self._highlight_code
        self.env.filters['question_border_color'] = self._question_border_color

    def generate_html(self, document: HandoutDocument) -> str:
        """
        Generate complete HTML from HandoutDocument.

        Args:
            document: The handout document to render

        Returns:
            Complete HTML string ready for PDF rendering
        """
        # Generate TOC
        toc = self._generate_toc(document.sections)
        document.toc = toc

        # Group questions by section
        questions_by_section = self._group_questions_by_section(
            document.questions
        )

        # Load main template
        template = self.env.get_template('dark_theme.html')

        # Render
        html = template.render(
            metadata=document.metadata,
            sections=document.sections,
            questions_by_section=questions_by_section,
            images=document.images,
            toc=toc,
            generation_timestamp=document.generation_timestamp,
            warnings=document.warnings,
            question_review_complete=document.question_review_complete
        )

        return html

    def _generate_toc(self, sections: List[ContentSection]) -> List[TOCEntry]:
        """
        Generate table of contents from sections.

        Extracts H1 and H2 headings and creates TOC entries with anchors.
        Page numbers will be filled by WeasyPrint during PDF rendering.

        Args:
            sections: List of content sections

        Returns:
            List of TOC entries
        """
        toc = []

        for section in sections:
            # Add H1 and H2 to TOC
            if section.level in [1, 2]:
                anchor = self._slugify(section.title)
                entry = TOCEntry(
                    level=section.level,
                    title=section.title,
                    page_number=0,  # WeasyPrint will fill this
                    anchor=anchor
                )
                toc.append(entry)

            # Recursively process subsections
            if section.subsections:
                toc.extend(self._generate_toc(section.subsections))

        return toc

    def _group_questions_by_section(
        self,
        questions: List[Question]
    ) -> Dict[str, List[Question]]:
        """
        Group questions by their source section.

        Args:
            questions: List of all questions

        Returns:
            Dictionary mapping section_id to list of questions
        """
        grouped = {}
        for question in questions:
            section_id = question.source_section
            if section_id not in grouped:
                grouped[section_id] = []
            grouped[section_id].append(question)

        return grouped

    def _slugify(self, text: str) -> str:
        """
        Convert text to URL-safe slug for anchors.

        Args:
            text: Text to slugify

        Returns:
            Slugified text
        """
        # Convert to lowercase
        slug = text.lower()
        # Replace spaces and special chars with hyphens
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        # Remove leading/trailing hyphens
        slug = slug.strip('-')
        return slug

    def _render_markdown(self, text: str) -> str:
        """
        Render markdown to HTML.

        Args:
            text: Markdown text

        Returns:
            HTML string
        """
        # Use markdown library with extensions
        html = markdown.markdown(
            text,
            extensions=[
                'extra',
                'codehilite',
                'fenced_code',
                'tables'
            ]
        )
        return html

    def _highlight_code(self, code: str, language: str = 'python') -> str:
        """
        Apply syntax highlighting to code.

        Basic highlighting for Python code:
        - Keywords: #FF7B72 (red)
        - Strings: #A5D6FF (light blue)
        - Comments: #8B949E (gray)
        - Functions: #D2A8FF (purple)
        - Numbers: #79C0FF (blue)

        Args:
            code: Code to highlight
            language: Programming language (currently only 'python' supported)

        Returns:
            HTML with syntax highlighting
        """
        if language != 'python':
            # For non-Python, just escape and return
            return self._escape_html(code)

        # Simple regex-based highlighting for Python
        highlighted = code

        # Keywords
        keywords = [
            'def', 'class', 'import', 'from', 'as', 'if', 'else', 'elif',
            'for', 'while', 'in', 'return', 'yield', 'try', 'except',
            'finally', 'with', 'lambda', 'pass', 'break', 'continue',
            'and', 'or', 'not', 'is', 'True', 'False', 'None'
        ]
        for keyword in keywords:
            highlighted = re.sub(
                rf'\b({keyword})\b',
                r'<span class="keyword">\1</span>',
                highlighted
            )

        # Strings (simple case - doesn't handle nested quotes perfectly)
        highlighted = re.sub(
            r'(["\'])([^\1]*?)\1',
            r'<span class="string">\1\2\1</span>',
            highlighted
        )

        # Comments
        highlighted = re.sub(
            r'(#.*?)$',
            r'<span class="comment">\1</span>',
            highlighted,
            flags=re.MULTILINE
        )

        # Numbers
        highlighted = re.sub(
            r'\b(\d+\.?\d*)\b',
            r'<span class="number">\1</span>',
            highlighted
        )

        # Function calls (simple heuristic)
        highlighted = re.sub(
            r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(',
            r'<span class="function">\1</span>(',
            highlighted
        )

        return highlighted

    def _question_border_color(self, question_type: str) -> str:
        """
        Get border color for question type.

        Args:
            question_type: Question type string

        Returns:
            Hex color code
        """
        color_map = {
            'multiple_choice': '#58A6FF',  # Blue
            'true_false': '#58A6FF',       # Blue
            'short_answer': '#3FB950',     # Green
            'reflection': '#A371F7',       # Purple
            'application': '#3FB950'       # Green
        }
        return color_map.get(question_type, '#58A6FF')

    def _escape_html(self, text: str) -> str:
        """
        Escape HTML special characters.

        Args:
            text: Text to escape

        Returns:
            Escaped text
        """
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#x27;'))
