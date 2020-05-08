from awesome_panel.designer import panel_designer_app

# region old

def get_app_view():
    return panel_designer_app.PanelDesignerApp().view

def test_app():
    component = panel_designer_app.PanelDesignerApp(
        modules_to_reload = [panel_designer_app],
        get_component_view = get_app_view
    )
    component.view.show()

# endregion