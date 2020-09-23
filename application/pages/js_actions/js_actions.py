"""# JS Actions

Once in a while you might want sprinkle in some Javascript actions in your Panel Application. The
basics are described in the [Links Section](https://panel.holoviz.org/user_guide/Links.html) of the
Panel user Guide.

Below we provide additional examples.

**Author:**
[Marc Skov Madsen](https://datamodelsanalytics.com)

**Code:**
[App]\
(https://github.com/MarcSkovMadsen/awesome-panel/blob/master/\
application/pages/js_actions/js_actions.py)

**Tags:**
[Panel](https://panel.holoviz.org/)
"""
import panel as pn

STYLE = """
<style>
.app-bar {
    color: white;
}
</style>
"""


def copy_to_clipboard():
    """This example was developed as a response to
[Discourse Post 949]\
(https://discourse.holoviz.org/t/\
using-panel-with-javascript-to-make-a-copy-text-to-clipboard-button/949)
by [ShanzyHolm](https://discourse.holoviz.org/u/ShanzyHolm/summary).
    """
    text = pn.pane.Markdown(copy_to_clipboard.__doc__)
    source_textarea = pn.widgets.TextAreaInput(
        value="Copy this text to the clipboard by clicking the button"
    )
    copy_source_button = pn.widgets.Button(name="✂ Copy Source Value", button_type="success")
    copy_source_code = "navigator.clipboard.writeText(source.value);"
    copy_source_button.js_on_click(args={"source": source_textarea}, code=copy_source_code)
    paste_text_area = pn.widgets.TextAreaInput(value="Paste your value here")
    return pn.Column(
        text,
        pn.Row(source_textarea, copy_source_button, paste_text_area),
        name="✂ Copy to Clipboard",
    )


def view():
    """Returns a view of the app

    Used by the awesome-panel.org gallery"""
    style = pn.pane.HTML(STYLE, width=0, height=0, sizing_mode="fixed", margin=0)
    panel_logo = pn.pane.PNG(
        object="https://panel.holoviz.org/_static/logo_horizontal.png",
        height=35,
        sizing_mode="fixed",
        align="center",
    )
    app_bar = pn.Row(
        pn.layout.VSpacer(width=10),
        pn.pane.Markdown("### 💪 JS Actions", align="center"),
        panel_logo,
        background="black",
        css_classes=["app-bar"],
        margin=(0, 0, 25, 0),
    )
    example_tabs = pn.Tabs(copy_to_clipboard())
    info = pn.pane.Markdown(__doc__)
    return pn.Column(
        info,
        style,
        app_bar,
        example_tabs,
    )


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    view().servable()
if __name__ == "__main__":
    pn.config.sizing_mode = "stretch_width"
    view().show()
