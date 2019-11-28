"""In this module we test the markdown component"""
import awesome_panel.express as pnx
import panel as pn
import pathlib

TEST_MD_FILE = pathlib.Path(__file__).parent / "data" / "test.md"


def test_pn_original():
    """## test_pn_original

    Manual test that

    - [] A "Header is shown"
    - [] The background is blue
    - [] The sizing_mode is "stretch_width" by default
    """
    app = pn.Column(
        test_pn_original.__doc__,
        pnx.Markdown("# Header", name="test", background="blue"),
        sizing_mode="stretch_width",
        background="lightgray",
        max_width=600,
    )
    app.servable("test_pn_original")


def test_pn_file():
    """## test_pn_file

    Manual test that

    [x] A path to a markdown file can be specified and shown
    """
    app = pn.Column(test_pn_file.__doc__, pnx.Markdown(path=TEST_MD_FILE, name="test"),)
    app.servable("test_pn_file")


if __name__.startswith("bk"):
    test_pn_original()
    test_pn_file()
