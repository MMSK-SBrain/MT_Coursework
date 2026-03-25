# ContentTransformer Usage Guide

## Overview

The `ContentTransformer` filters instructor-only content and transforms framework content into student-appropriate format. It is a core component of the Student Handout Generator system.

## Features

- **Section Removal**: Remove sections by title pattern (case-insensitive)
- **HTML Comment Removal**: Strip instructor-only content between HTML comment tags
- **Recursive Processing**: Handle nested section hierarchies
- **Configurable Patterns**: Define custom exclusion patterns via configuration
- **Transformation Rules**: Optional find-and-replace for terminology
- **Statistics**: Track inclusion/exclusion rates

## Quick Start

### Basic Usage

```python
from src.content_transformer import create_transformer
from src.models import ContentSection

# Load configuration
config = {
    'content': {
        'exclude_patterns': [
            '## Video Production Notes',
            '### For Instructors',
            '<!-- INSTRUCTOR ONLY -->'
        ],
        'transform_rules': {}
    }
}

# Create transformer
transformer = create_transformer(config)

# Transform sections
sections = [...]  # List of ContentSection objects from parser
transformed = transformer.transform(sections)

# Get only included sections
student_sections = transformer.get_included_sections(transformed)

# Get statistics
stats = transformer.get_statistics(transformed)
print(f"Excluded {stats['excluded_sections']} of {stats['total_sections']} sections")
```

### With Configuration File

```python
import yaml
from src.content_transformer import create_transformer

# Load from handout_config.yaml
with open('handout_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

transformer = create_transformer(config)
```

## Configuration

### Exclusion Patterns

Define patterns to exclude in `handout_config.yaml`:

```yaml
content:
  exclude_patterns:
    - "## Video Production Notes"
    - "### For Instructors"
    - "## Instructor Notes"
    - "## 🎬 Video Production*"  # Supports wildcards
```

**Pattern Matching:**
- Case-insensitive
- Exact match required (unless wildcards used)
- Supports `*` wildcard: `*Production*` matches any section containing "Production"

### Transformation Rules (Optional)

Apply find-and-replace rules for terminology:

```yaml
content:
  transform_rules:
    learner: student
    pedagogy: teaching method
```

**Note:** Transformation rules use word boundaries to avoid partial matches.

## HTML Comment Formats

The transformer removes content between the following HTML comment tags:

### Format 1: INSTRUCTOR ONLY

```markdown
Student content here.

<!-- INSTRUCTOR ONLY -->
This will be removed from student handouts.
Can span multiple lines.
<!-- END INSTRUCTOR ONLY -->

More student content.
```

### Format 2: INSTRUCTOR

```markdown
Student content.

<!-- INSTRUCTOR -->
Instructor notes to remove.
<!-- /INSTRUCTOR -->

More student content.
```

**Features:**
- Case-insensitive: `<!-- instructor only -->` also works
- Multiple blocks supported
- Multiline content supported
- Whitespace variations tolerated

## Section Exclusion

### How It Works

1. **Pattern Matching**: Section title is checked against all exclusion patterns
2. **Recursive Processing**: Subsections are processed independently
3. **Flag Setting**: `include_in_handout` flag set to `False` for excluded sections
4. **Parent Propagation**: If parent excluded, all children also excluded

### Example

```python
section = ContentSection(
    id="s1",
    level=2,
    title="## Video Production Notes",
    content="Camera setup and lighting...",
    subsections=[
        ContentSection(
            id="s1.1",
            level=3,
            title="### Session 1",
            content="Filming tips..."
        )
    ]
)

transformed = transformer.transform_section(section)

# Both parent and child excluded
assert not transformed.include_in_handout
assert not transformed.subsections[0].include_in_handout
```

## Advanced Usage

### Custom Patterns with Wildcards

```python
config = {
    'exclude_patterns': [
        '## *Production*',      # Matches "Video Production", "Production Notes", etc.
        '### *Instructor*',     # Matches "For Instructors", "Instructor Guide", etc.
        '## 🎬*'                # Matches any section starting with film emoji
    ]
}
```

### Processing Pipeline Integration

```python
from src.framework_parser import FrameworkParser
from src.content_transformer import create_transformer

# 1. Parse framework
parser = FrameworkParser()
parse_result = parser.parse_file("module-0-framework.md")

# 2. Transform content
transformer = create_transformer(config)
transformed = transformer.transform(parse_result.sections)

# 3. Filter to student-ready content
student_sections = transformer.get_included_sections(transformed)

# 4. Get statistics
stats = transformer.get_statistics(transformed)
print(f"Inclusion rate: {stats['inclusion_rate']}%")
```

### Combining HTML Comments and Pattern Exclusion

```python
# Config excludes "For Instructors" sections
config = {
    'exclude_patterns': ['### For Instructors']
}

# Section with both types of instructor content
section = ContentSection(
    id="s1",
    level=2,
    title="## Session 1",
    content="""
Student content.

<!-- INSTRUCTOR ONLY -->
Pacing notes: 15 minutes
<!-- END INSTRUCTOR ONLY -->

More student content.
""",
    subsections=[
        ContentSection(
            id="s1.1",
            level=3,
            title="### For Instructors",
            content="Teaching tips and rubric"
        )
    ]
)

transformed = transformer.transform([section])

# Session 1 included but cleaned
assert transformed[0].include_in_handout
assert "Pacing notes" not in transformed[0].content

# "For Instructors" subsection excluded
assert not transformed[0].subsections[0].include_in_handout
```

## Output

### Transformed Sections

After transformation, each `ContentSection` has:

- `include_in_handout`: Boolean flag indicating inclusion status
- `content`: Cleaned content (HTML comments removed)
- `subsections`: Recursively transformed subsections

### Statistics

```python
stats = transformer.get_statistics(sections)

# Returns:
{
    'total_sections': 10,
    'included_sections': 8,
    'excluded_sections': 2,
    'inclusion_rate': 80.0
}
```

## Error Handling

### Invalid Patterns

Invalid regex patterns are logged as warnings and skipped:

```python
config = {
    'exclude_patterns': [
        '## Valid Pattern',
        '[Invalid(Regex',  # Invalid - will be skipped
        '## Another Valid'
    ]
}

# Transformer initializes successfully
# Warning logged: "Invalid exclusion pattern '[Invalid(Regex': ..."
```

### Malformed HTML Comments

Unclosed HTML comments are handled gracefully:

```markdown
Content before.

<!-- INSTRUCTOR ONLY -->
Missing closing tag

Content after.
```

**Result:** Content after unclosed tag is preserved (not removed).

## Best Practices

1. **Test Patterns**: Verify exclusion patterns match expected sections
2. **Use Statistics**: Monitor inclusion rates to ensure expected filtering
3. **Preserve Markdown**: Transformation preserves all markdown formatting
4. **Check Logs**: Review logs for pattern warnings
5. **Validate Output**: Use `get_included_sections()` for final content

## Testing

### Unit Tests

```bash
python3 -m pytest tests/test_content_transformer.py -v
```

**Coverage:** 96%+ (exceeds 80% requirement)

### Integration Tests

```bash
python3 -m pytest tests/test_content_transformer_integration.py -v
```

## Examples

See `tests/test_content_transformer_integration.py` for realistic usage examples with:
- Multi-level section hierarchies
- Mixed student/instructor content
- HTML comments at various levels
- Markdown formatting preservation

## API Reference

### ContentTransformer

**Constructor:**
```python
ContentTransformer(config: dict[str, Any])
```

**Methods:**
- `transform(sections: list[ContentSection]) -> list[ContentSection]`
- `transform_section(section: ContentSection, parent_excluded: bool = False) -> ContentSection`
- `get_included_sections(sections: list[ContentSection]) -> list[ContentSection]`
- `get_statistics(sections: list[ContentSection]) -> dict[str, int]`

**Factory Function:**
```python
create_transformer(config: dict[str, Any]) -> ContentTransformer
```

## Changelog

**v1.0.0** (2026-01-11)
- Initial implementation
- Section pattern exclusion (case-insensitive)
- HTML comment block removal
- Recursive section processing
- Wildcard pattern support
- Transformation rules (find-and-replace)
- Statistics tracking
- 96% test coverage
