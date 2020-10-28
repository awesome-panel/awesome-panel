"""This test is here for legacy reasons

Originally the `Markdown` functionality of Panel was limited as it did not support

- Code blocks
- Indented Markdown text as is often what is used in Editors like VS Code.

So here we test that
"""
import pathlib

import awesome_panel.express as pnx
import panel as pn
from awesome_panel.express.testing import TestApp

from application.template import get_template

TEST_MD_FILE = pathlib.Path(__file__).parent / "data" / "test.md"


def test_markdown():
    """
    We test that

    - A "Header is shown"
    - The background is blue
    - The sizing_mode is "stretch_width" by default. DOES NOT WORK CURRENTLY
    """
    return TestApp(
        test_markdown,
        pn.pane.Markdown(
            "# Header",
            name="basic",
            background="lightblue",
        ),
        sizing_mode="stretch_width",
        background="lightgray",
        max_width=600,
    )


def test_markdown_from_file():
    """
    We test that

    - A path to a markdown file can be used directly in one line
    """
    return TestApp(
        test_markdown_from_file,
        pn.pane.Markdown(
            TEST_MD_FILE.read_text(),
            name="file",
            background="lightblue",
        ),
    )


def test_markdown_indendation():
    """
    We test the Markdown pane

    - can handle leading spaces, i.e. this line shows as a bullited list and not in mono-space"""
    return TestApp(
        test_markdown_indendation,
        sizing_mode="stretch_width",
    )


def test_markdown_code_block():
    """
    We test that

    - Code blocks are supported.
    - Indented markdown strings from inside functions is supported
    """
    code_block = """
    This is indented

    ```python
    print("Hello Awesome Panel World")
    return TestApp(
        test_markdown_code_block,
        pn.pane.Markdown(code_block, name="code block", background="lightblue"),
    ```
    """

    return TestApp(
        test_markdown_code_block,
        pn.pane.Markdown(
            code_block,
            name="code block",
            background="lightblue",
        ),
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    main = [
        pn.pane.Markdown(__doc__),
        test_markdown,
        test_markdown_from_file,
        test_markdown_indendation,
        test_markdown_code_block,
    ]
    return get_template(title="Test Markdown", main=main)


if __name__.startswith("bokeh"):
    view().servable("test_markdown")
