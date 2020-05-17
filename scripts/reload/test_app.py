import app
from reload_app import ReloadComponent


def get_app_view():
    return app.MyClass().view()


def test_app():
    component = ReloadComponent(get_component_view=get_app_view)
    component.view.show(threaded=True)


test_app()
