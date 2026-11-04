#!/usr/bin/env python3
"""
Preprocess lecture frameworks for Marp/PowerPoint conversion
Converts instructor-led story framework to Marp-compatible markdown
"""

import re
import sys
from pathlib import Path

def extract_slide_content(text):
    """Extract main content from instructor script blocks"""
    # Remove instructor script markers
    text = re.sub(r'\*\*Instructor Script:\*\*\s*', '', text)

    # Remove blockquote markers but keep content
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)

    # Clean up visual descriptions (convert to comments)
    text = re.sub(r'\*\*Visual:\*\*\s*(.+?)$', r'<!-- Visual: \1 -->', text, flags=re.MULTILINE)

    # Remove leading/trailing quotes from instructor dialogue
    text = re.sub(r'^"(.+)"$', r'\1', text, flags=re.MULTILINE | re.DOTALL)

    # Clean up quote marks at start of lines
    text = re.sub(r'^"', '', text, flags=re.MULTILINE)

    # Clean up quote marks at end of paragraphs
    text = re.sub(r'"$', '', text, flags=re.MULTILINE)

    # Clean up bold markers in lists
    text = re.sub(r'\*\*(.+?)\*\*\s*-', r'**\1** —', text)

    return text.strip()

def parse_framework_to_marp(input_file, output_file):
    """Convert framework markdown to Marp format"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from first heading
    title_match = re.search(r'^# Session \d+:\s*(.+)$', content, re.MULTILINE)
    session_title = title_match.group(1) if title_match else "Automotive Lecture"
    session_num = re.search(r'Session (\d+)', content)
    session_number = session_num.group(1) if session_num else "X"

    # Start with Marp frontmatter
    output = f"""---
marp: true
theme: engineering
paginate: true
math: katex
header: 'Session {session_number}: {session_title}'
---

<!-- _class: title -->
<!-- _paginate: false -->

# {session_title}

**Session {session_number} | Automotive Vehicles (AEL ZC441)**

---

"""

    # Split content into slide blocks
    # Look for patterns like "## Slide X:", "### SLIDE X:", "#### Slide X:", or "##### Slide X:"
    slide_pattern = r'(?:##|###|####|#####)\s+[Ss][Ll][Ii][Dd][Ee]\s+\d+:([^\n]+)(.*?)(?=(?:##|###|####|#####)\s+[Ss][Ll][Ii][Dd][Ee]\s+\d+:|$)'
    slides = re.findall(slide_pattern, content, re.DOTALL)

    for slide_title, slide_content in slides:
        slide_title = slide_title.strip()

        # Skip if this is just the main title slide (we already added it)
        if 'Title' == slide_title and len(output.split('---')) <= 2:
            continue

        # Extract and clean content
        processed_content = extract_slide_content(slide_content)

        # Skip empty slides
        if not processed_content or len(processed_content) < 10:
            continue

        # Skip section markers (SETUP, TRIGGER, RISING ACTION, etc.)
        if any(marker in processed_content for marker in ['**SETUP:', '**TRIGGER:', '**RISING ACTION:', '**CLIMAX:', '**RESOLUTION:']):
            continue

        # Add slide separator and content
        output += f"---\n\n## {slide_title}\n\n{processed_content}\n\n"

    # If no slides were found using the pattern, try alternative approach
    if output.count('---') < 3:  # Less than 3 slides means something went wrong
        # Try extracting content between ### headers
        sections = re.split(r'\n###\s+', content)
        for section in sections[1:]:  # Skip first (metadata)
            lines = section.split('\n')
            section_title = lines[0].strip('*').strip()

            # Skip metadata sections
            if any(skip in section_title.lower() for skip in ['objective', 'story arc', 'instructor']):
                continue

            # Get content
            section_content = '\n'.join(lines[1:])
            processed = extract_slide_content(section_content)

            if processed and len(processed) > 20:
                output += f"---\n\n## {section_title}\n\n{processed}\n\n"

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    return output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python preprocess-framework.py <input-framework.md> [output-dir]")
        print("  If output-dir is not specified, uses ./preprocessed/")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    # Create preprocessed directory
    if len(sys.argv) >= 3:
        # Custom output directory provided
        output_dir = Path(sys.argv[2])
    else:
        # Default: current directory / preprocessed
        output_dir = Path.cwd() / 'preprocessed'

    output_dir.mkdir(parents=True, exist_ok=True)

    # Output file
    output_path = output_dir / input_path.name

    print(f"Preprocessing: {input_path.name}")
    result = parse_framework_to_marp(input_path, output_path)
    print(f"✓ Created: {output_path}")
    print(f"  Slides: {result.count('---') - 1}")  # -1 for frontmatter
