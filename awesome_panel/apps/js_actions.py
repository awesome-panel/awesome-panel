"""Once in a while you might want sprinkle in some Javascript actions in your Panel Application. The
basics are described in the [Links Section](https://panel.holoviz.org/user_guide/Links.html) of the
Panel user Guide.

This example was developed as a response to
[Discourse Post 949]\
(https://discourse.holoviz.org/t/\
using-panel-with-javascript-to-make-a-copy-text-to-clipboard-button/949)
by [ShanzyHolm](https://discourse.holoviz.org/u/ShanzyHolm/summary).
"""
import panel as pn

from awesome_panel import config

STYLE = """
<style>
.app-bar {
    color: white;
}
</style>
"""


def copy_to_clipboard():
    """Copy"""
    source_textarea = pn.widgets.TextAreaInput(
        value="Copy this text to the clipboard by clicking the button",
        height=100,
    )
    copy_source_button = pn.widgets.Button(name="✂ Copy Source Value", button_type="primary")
    copy_source_code = "navigator.clipboard.writeText(source.value);"
    copy_source_button.js_on_click(args={"source": source_textarea}, code=copy_source_code)
    paste_text_area = pn.widgets.TextAreaInput(placeholder="Paste your value here", height=100)
    return pn.Column(
        pn.Row(source_textarea, copy_source_button, paste_text_area),
        name="✂ Copy to Clipboard",
    )


def main() -> pn.Column:
    """Returns the app main component

    Used by the awesome-panel.org gallery"""
    style = pn.pane.HTML(STYLE, width=0, height=0, sizing_mode="fixed", margin=0)
    example_tabs = pn.Tabs(copy_to_clipboard())
    return pn.Column(
        style,
        example_tabs,
    )


if __name__.startswith("bokeh"):
    config.extension(url="js_actions", main_max_width="800px")

    main().servable()
