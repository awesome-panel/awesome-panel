# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from awesome_panel.application.views import ApplicationView


def test_can_construct(application_view):
    assert isinstance(application_view, ApplicationView)
    assert hasattr(application_view, "main")
    assert hasattr(application_view, "sidebar")
    assert hasattr(application_view, "topbar")
    assert hasattr(application_view, "spinner")
    assert hasattr(application_view, "navigation")

    assert isinstance(application_view.application_css, pn.pane.HTML)
    assert isinstance(application_view.application_js, pn.pane.HTML)
    assert isinstance(application_view.theme_css, pn.pane.HTML)
    assert isinstance(application_view.theme_js, pn.pane.HTML)
    assert isinstance(application_view.page_css, pn.pane.HTML)
    assert isinstance(application_view.page_js, pn.pane.HTML)

    assert application_view.application_js.sizing_mode == "fixed"
    assert application_view.application_css.sizing_mode == "fixed"
    assert application_view.theme_css.sizing_mode == "fixed"
    assert application_view.theme_js.sizing_mode == "fixed"
    assert application_view.page_css.sizing_mode == "fixed"
    assert application_view.page_js.sizing_mode == "fixed"

    assert application_view.application_js.width == 0
    assert application_view.application_css.width == 0
    assert application_view.theme_css.width == 0
    assert application_view.theme_js.width == 0
    assert application_view.page_css.width == 0
    assert application_view.page_js.width == 0

    assert application_view.application_js.height == 0
    assert application_view.application_css.height == 0
    assert application_view.theme_css.height == 0
    assert application_view.theme_js.height == 0
    assert application_view.page_css.height == 0
    assert application_view.page_js.height == 0

    assert application_view.application_js.margin == 0
    assert application_view.application_css.margin == 0
    assert application_view.theme_css.margin == 0
    assert application_view.theme_js.margin == 0
    assert application_view.page_css.margin == 0
    assert application_view.page_js.margin == 0
