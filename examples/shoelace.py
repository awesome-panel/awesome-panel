"""This is a **custom Panel template** based on [Shoelace](https://shoelace.style/).
Shoelace provides a set of mature and awesome web components in the style of Bootstrap.
It's the best set of **Bootstrap like** web components I've been able to find. I want web
components because they work well in Jupyter Notebooks and because I believe they are the future of
the web.

The vision is to extend this to a Template similar to the
[Bootstrap Template](https://panel.holoviz.org/user_guide/Templates.html) and develop a set of
of Shoelace widgets for Panel.

This template includes a modal popup which was originally requested on
[Discourse 1207](https://discourse.holoviz.org/t/can-i-use-create-a-modal-dialog-in-panel/1207)

Developed by [awesome-panel.org](/).
"""
import hvplot.pandas  # pylint: disable=unused-import
import panel as pn
import param
from bokeh.sampledata import sea_surface_temperature as sst

from awesome_panel import config
from awesome_panel.assets.html import SHOELACE_TEMPLATE_PATH


@config.cached
def _read_template() -> str:
    return SHOELACE_TEMPLATE_PATH.read_text(encoding="utf-8")


TEMPLATE = _read_template()


class TemplateWithDialog(pn.template.Template):
    """Custom Panel Template With a Dialog"""

    dialog_open = param.Action()
    dialog_close = param.Action()

    def __init__(self, header, main, dialog, dialog_label: str):
        super().__init__(
            template=TEMPLATE,
        )

        self.add_panel("header", header)
        self.add_panel("main", main)
        self.add_panel("dialog", dialog)
        self.add_variable("dialog_label", dialog_label)


EXAMPLES = """
<sl-alert open>
  <sl-icon slot="icon" name="info-circle"></sl-icon>
  This is a standard alert. You can customize its content and even the icon.
</sl-alert><br/>

<div class="badge-pulse">
  <sl-badge type="primary" pill pulse>1</sl-badge>
  <sl-badge type="success" pill pulse>1</sl-badge>
  <sl-badge type="info" pill pulse>1</sl-badge>
  <sl-badge type="warning" pill pulse>1</sl-badge>
  <sl-badge type="danger" pill pulse>1</sl-badge>
</div><br/>
<style>
  .badge-pulse sl-badge:not(:last-of-type) {
    margin-right: 1rem;
  }
</style>

<sl-button type="default">Default</sl-button>
<sl-button type="primary">Primary</sl-button>
<sl-button type="success">Success</sl-button>
<sl-button type="info">Info</sl-button>
<sl-button type="warning">Warning</sl-button>
<sl-button type="danger">Danger</sl-button>
<sl-button size="small" pill>Small</sl-button>
<sl-button size="medium" pill>Medium</sl-button>
<sl-button size="large" pill>Large</sl-button>
<br/>

<sl-checkbox>Checkbox</sl-checkbox><br/>

<sl-icon-button name="pencil" label="Edit" style="font-size: 1.5rem;"></sl-icon-button>
<sl-icon-button name="pencil" label="Edit" style="font-size: 2rem;"></sl-icon-button>
<sl-icon-button name="pencil" label="Edit" style="font-size: 2.5rem;"></sl-icon-button><br/>

<sl-range min="0" max="100" step="1"></sl-range><br/>

<div class="skeleton-overview">
  <header>
    <sl-skeleton></sl-skeleton>
    <sl-skeleton></sl-skeleton>
  </header>

  <sl-skeleton></sl-skeleton>
  <sl-skeleton></sl-skeleton>
  <sl-skeleton></sl-skeleton>
</div><br/>

<style>
  .skeleton-overview header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
  }

  .skeleton-overview header sl-skeleton:last-child {
    flex: 0 0 auto;
    width: 30%;
  }

  .skeleton-overview sl-skeleton {
    margin-bottom: 1rem;
  }

  .skeleton-overview sl-skeleton:nth-child(1) {
    float: left;
    width: 3rem;
    height: 3rem;
    margin-right: 1rem;
    vertical-align: middle;
  }

  .skeleton-overview sl-skeleton:nth-child(3) {
    width: 95%;
  }

  .skeleton-overview sl-skeleton:nth-child(4) {
    width: 80%;
  }
</style>

<sl-textarea></sl-textarea><br/>
"""


def _get_sea_surface_temperature_plot():
    if "dialog_template_plot" not in pn.state.cache:
        pn.state.cache["dialog_template_plot"] = sst.sea_surface_temperature.hvplot.kde().opts(
            height=300, width=500
        )
    return pn.state.cache["dialog_template_plot"]


def view(intro_section):
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
        intro_section,
        pn.pane.Alert(
            """The below are just a small set of the nice ShoeLace components that could
        power Panel one day! **Try clicking the "Open Dialog" button at the bottom!**"""
        ),
        pn.pane.HTML(EXAMPLES, height=700),
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


if __name__.startswith("bokeh"):
    app = config.extension(url="shoelace", template=None, intro_section=False)
    view(intro_section=app.intro_section()).servable()
