from awesome_panel.styler.stylers.app_styler import AppStyler
import pytest

@pytest.fixture
def app_styler():
    return AppStyler()

def test_can_construct_app_styler(app_styler):
    assert isinstance(app_styler, AppStyler)

    assert app_styler.theme == "default"

    assert app_styler.body_color == "#000000"
    assert app_styler.body_background == "#ffffff"
    assert app_styler.font_family == "Times New Roman"

    assert app_styler.bar_color == "#ffffff"
    assert app_styler.bar_background == "#4caf50"
    assert app_styler.bar_shadow == True
    assert app_styler.bar_line == False

    assert app_styler.container_color == "#ffffff"
    assert app_styler.container_background == "#4caf50"
    assert app_styler.container_shadow == True
    assert app_styler.container_line == False

    assert app_styler.settings_color == "#ffffff"
    assert app_styler.settings_background == "#4caf50"
    assert app_styler.settings_line_right == False
    assert app_styler.settings_line_left == False

    assert app_styler.css=""

def test_can_change_theme(app_styler):
    # When:
    app_styler.theme = "material-dark"
    # Then
    assert app_styler.body_color == "#000000"
    assert app_styler.body_background == "#ffffff"
    assert app_styler.font_family == "Times New Roman"

    assert app_styler.bar_color == "#ffffff"
    assert app_styler.bar_background == "#4caf50"
    assert app_styler.bar_shadow == True
    assert app_styler.bar_line == False

    assert app_styler.container_color == "#ffffff"
    assert app_styler.container_background == "#4caf50"
    assert app_styler.container_shadow == True
    assert app_styler.container_line == False

    assert app_styler.settings_color == "#ffffff"
    assert app_styler.settings_background == "#4caf50"
    assert app_styler.settings_line_right == False
    assert app_styler.settings_line_left == False

    assert isinstance(app_styler.css, str)


