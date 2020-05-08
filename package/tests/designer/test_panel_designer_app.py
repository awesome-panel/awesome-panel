import param

from awesome_panel.designer.panel_designer_app import PanelDesignerApp


def test_can_construct():
    panel_designer_app = PanelDesignerApp()
    assert panel_designer_app.title == "Awesome Panel Designer"
    assert panel_designer_app.logo_url
    assert panel_designer_app.param.sub_component_parameters == []
    assert panel_designer_app.sub_component_parameters == [
        "background",
        "height",
        "sizing_mode",
        "style",
        "width",
    ]
    assert not panel_designer_app.css_path
    assert not panel_designer_app.js_path
    assert not panel_designer_app.component
    assert not panel_designer_app.component_instance
    assert panel_designer_app.modules_to_reload==[]

def test_fixture_is_as_expected(panel_designer_app, component, component_parameters, css_path, js_path):
    isinstance(panel_designer_app, PanelDesignerApp)

    assert panel_designer_app.component == component
    assert panel_designer_app.component_instance
    assert panel_designer_app.component_parameters == component_parameters

    assert panel_designer_app.css_path == css_path
    assert panel_designer_app.js_path == js_path

    assert len(panel_designer.param.sub_component.objects) > 1
    assert panel_designer.param.sub_component.default == panel_designer_app.component_instance
    assert panel_designer.sub_component == panel_designer_app.component_instance

# endregion
# region: Actions


def test_can_reload_component(panel_designer_app):
    # Given: I have my panel_designer_app with an existing component_instance
    old_instance = panel_designer_app.component_instance
    # When: I reload the component
    panel_designer_app.reload_component_instance()
    # Then: I have a new component instance
    assert panel_designer_app.component_instance != old_instance


def test_can_reload_css_file(panel_designer_app):
    panel_designer_app.reload_css_file()


def test_can_reload_js_file(panel_designer_app):
    panel_designer_app.reload_js_file()


def test_can_start_and_stop_server_without_error(panel_designer_app):
    panel_designer_app.show()
    panel_designer_app.stop_server()


# region Panes

def test_has_view(panel_design_app):
    panel_design_app.view

def test_has_main_pane(panel_design_app):
    panel_design_app.component_pane


def test_has_design_pane(panel_design_app):
    panel_design_app.design_pane

def test_has_action_pane(panel_design_app):
    panel_design_app.action_pane


def test_has_sub_component_pane(panel_design_app):
    panel_design_app.sub_component_pane


def test_has_css_pane(panel_design_app):
    panel_design_app.css_pane


def test_has_js_pane(panel_design_app):
    panel_design_app.js_pane


def test_has_logo_pane(panel_design_app):
    panel_design_app.logo_pane


# endregion
