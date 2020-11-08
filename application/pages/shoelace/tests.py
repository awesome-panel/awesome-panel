# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from application.pages.shoelace import view
from application.pages.shoelace.template import TemplateWithDialog


def test_can_construct_template():
    open_button = pn.widgets.Button(name="Open Dialog")
    close_button = pn.widgets.Button(name="Close Dialog")

    header_panel = pn.Row("allo")
    main_panel = pn.Column("This is an application with a dialog", open_button)
    dialog_panel = pn.Column("This is a dialog", close_button)

    TemplateWithDialog(
        header=header_panel,
        main=main_panel,
        dialog=dialog_panel,
        dialog_label="Hello Dialog World",
    )


def test_can_serve_page_view():
    view().servable()


if __name__.startswith("bokeh"):
    test_can_serve_page_view()
