"""Panel application show casing a Custom Panel Template With a Dialog"""
import hvplot.pandas  # pylint: disable=unused-import
import panel as pn
from bokeh.sampledata import sea_surface_temperature as sst

from .template import TemplateWithDialog


def _get_sea_surface_temperature_plot():
    if "dialog_template_plot" not in pn.state.cache:
        pn.state.cache["dialog_template_plot"] = sst.sea_surface_temperature.hvplot.kde().opts(
            height=300, width=500
        )
    return pn.state.cache["dialog_template_plot"]


def view():
    """Returns a Panel application show casing a Custom Panel Template With a Dialog"""
    top_panel = pn.Row(
            pn.pane.PNG(
                "https://panel.holoviz.org/_static/logo_horizontal.png",
                height=50,
                margin=10,
                link_url="https://panel.holoviz.org",
                sizing_mode="stretch_width",
            ),
            background="black",
            sizing_mode="stretch_width",
        )
    main_panel = pn.Column(
        "This is a Panel application with a dialog",
        "Provided by awesome-panel.org",
        sizing_mode="stretch_width",
    )
    dialog_panel = pn.Column(_get_sea_surface_temperature_plot(), sizing_mode="fixed")

    template = TemplateWithDialog(
        header=top_panel,
        main=main_panel,
        dialog=dialog_panel,
        dialog_label="HvPlot - Sea surface temperature kde",
    )

    return template
