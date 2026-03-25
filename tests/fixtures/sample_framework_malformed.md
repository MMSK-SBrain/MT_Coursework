---
course_code: ML-ENG-M1
module_number: 1
# Missing module_title (required field!)
duration: "2 weeks"
invalid_yaml: [unclosed list
---

# Module 1: Data Exploration

This framework file has several issues to test error handling.

## Section with Missing Content

## Another Section

### Subsection

Some content here.

#### Deep Nesting ####

##### Even Deeper #####

###### Maximum Depth ######

####### Too Many Hashes (Invalid) #######

Regular paragraph with some text.

![Missing Alt Text]()

![Image with No Path](  )

![Valid Image](../images/test.png)

## Malformed Code Block

```python
# This code block is not properly closed
def broken_function():
    print("Missing closing fence")

This text should be in the code block but fence is missing.

## Section After Malformed Code

This should still be parsed.

### Table with Issues

| Column 1 | Column 2 |
|----------|
| Missing cell | Complete |
| Row | Two |

## Broken Image Reference

![Alt text](../images/file with spaces.png)
![Another](broken\\path\\image.jpg)

## Special Characters

Section with émojis 🚀 and spëcial çharacters!

### Nested Lists

- Item 1
  - Nested 1a
    - Deep nest 1a1
  - Nested 1b
- Item 2

1. Numbered item
   1. Nested number
   2. Another nested
2. Item 2

## Very Long Line Test

This is a line with lots of text to test line length handling: Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum.

## HTML in Markdown

<div class="container">
  <p>Some HTML content</p>
  <script>alert('XSS test')</script>
</div>

## Duplicate Heading

## Duplicate Heading

Both sections have the same title - ID generation should handle this.

<!-- Comment that should be preserved -->

> Blockquote with **bold** and *italic* text
> Second line of quote

## Final Section

End of malformed test file.
