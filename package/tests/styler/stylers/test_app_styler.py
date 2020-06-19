from awesome_panel.styler.stylers.app_styler import AppStyler
import pytest
import panel as pn


@pytest.fixture
def app_styler():
    return AppStyler()


def test_can_construct_app_styler(app_styler):
    assert isinstance(app_styler, AppStyler)

    assert app_styler.name == "App"
    assert app_styler.body_color == "#000000"
    assert app_styler.body_background == "#ffffff"
    assert app_styler.font_family == "Times New Roman"

    assert app_styler.bar_color == "#ffffff"
    assert app_styler.bar_background == "#4caf50"
    assert app_styler.bar_shadow
    assert not app_styler.bar_line

    assert app_styler.container_color == "#ffffff"
    assert app_styler.container_background == "#4caf50"
    assert app_styler.container_shadow
    assert not app_styler.container_line

    assert app_styler.settings_color == "#ffffff"
    assert app_styler.settings_background == "#4caf50"
    assert not app_styler.settings_line_right
    assert not app_styler.settings_line_left

    expected_css = """\
.app-body {
    color: #000000;
    background: #ffffff;
    font-family: Times New Roman;
}
.app-bar {
    color: #ffffff;
    background: #4caf50;
    box-shadow: 5px 5px 20px #9E9E9E;
}
.app-container {
    color:#ffffff;
    background:#4caf50;
    border-radius: 5px;
    box-shadow: 2px 2px 2px lightgrey;
}"""
    assert app_styler.css == expected_css

    assert isinstance(app_styler.view, pn.Param)


def test_can_apply_theme(app_styler):
    # When:
    app_styler.apply_theme("material-dark")
    # Then
    assert app_styler.font_family == "roboto"

def test_app_styler_can_update_css(app_styler):
    # Given
    org_css = app_styler.css
    # When
    app_styler.body_color = "#ffff00"
    # Then
    assert app_styler.css != org_css

