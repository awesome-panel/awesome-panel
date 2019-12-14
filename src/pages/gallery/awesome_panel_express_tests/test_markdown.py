"""In this module we test the `Markdown` functionality of `awesome_panel.express`

The `Markdown` functionality of Panel is limited as it does not support

- One liners for using Markdown from files
- Code blocks
- Indented Markdown text as is often what is used in Editors like VS Code.

Please note you need to run `Code.extend()` in order to add the CODE_HILITE CSS to the app.
"""
import pathlib

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp

TEST_MD_FILE = pathlib.Path(__file__).parent / "data" / "test.md"

pnx.Code.extend()


def test_markdown():
    """We test that

    - A "Header is shown"
    - The background is blue
    - The sizing_mode is "stretch_width" by default. DOES NOT WORK CURRENTLY
    """
    return TestApp(
        test_markdown,
        pnx.Markdown("# Header", name="basic", background="lightblue"),
        sizing_mode="stretch_width",
        background="lightgray",
        max_width=600,
    )


def test_markdown_from_file():
    """We test that

    - A path to a markdown file can used directly in one line
    """
    return TestApp(
        test_markdown_from_file,
        pnx.Markdown(path=TEST_MD_FILE, name="file", background="lightblue"),
    )


def test_markdown_indendation():
    """We test the Markdown pane

    - can handle leading spaces, i.e. this line shows as a bullited list and not in mono-space
"""
    return TestApp(test_markdown_indendation, sizing_mode="stretch_width",)


def test_markdown_code_block():
    """We test that

    - A code blocks are supported. Sort of. BUT THE INDENTATION IS CURRENTLY LOST!
    - Indented markdown test from editors is supported. The Panel Markdown does not support this.
    """
    code_block = """
This is not indented

```python
print("Hello Awesome Panel World")
return TestApp(
    test_markdown_code_block,
    pnx.Markdown(code_block, name="code block", background="lightblue"),
```

    This is indented```
    """

    return TestApp(
        test_markdown_code_block,
        pnx.Markdown(code_block, name="code block", background="lightblue"),
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- An Column containing all the tests
    """
    return pn.Column(
        pnx.Markdown(__doc__),
        test_markdown,
        test_markdown_from_file,
        test_markdown_indendation,
        test_markdown_code_block,
    )


if __name__.startswith("bk"):
    view().servable("test_markdown")
