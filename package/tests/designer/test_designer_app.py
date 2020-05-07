from awesome_panel.designer import DesignerApp

def get_app_view():
    return DesignerApp().view

def test_app():
    component = DesignerApp(
        modules_to_reload = [],
        get_component_view = get_app_view
    )
    component.view.show()