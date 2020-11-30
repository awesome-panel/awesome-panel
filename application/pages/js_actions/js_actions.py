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

from application.config import site

APPLICATION = site.create_application(
    url="js-actions",
    name="JS Actions",
    author="Marc Skov Madsen",
    introduction="Shows how to use a little bit of javascript with Panel",
    description=__doc__,
    thumbnail_url="js_actions.png",
    code_url="js_actions/js_actions.py",
    tags=[
        "JavaScript",
    ],
)
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


@site.add(APPLICATION)
def view():
    """Returns a view of the app

    Used by the awesome-panel.org gallery"""
    pn.config.sizing_mode = "stretch_width"
    style = pn.pane.HTML(STYLE, width=0, height=0, sizing_mode="fixed", margin=0)
    example_tabs = pn.Tabs(copy_to_clipboard())
    info = APPLICATION.intro_section()
    main = [
        info,
        pn.Column(
            style,
            example_tabs,
        ),
    ]
    return site.create_template(title="JS Actions", main=main)


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show()
