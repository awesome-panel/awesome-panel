"""The Panel [FileInput]\
(https://panel.holoviz.org/reference/widgets/FileInput.html#widgets-gallery-FileInput)
is just an *ugly* button designed in the 1990s.

Here we style the FileInput to make it look like a more modern file upload area that
**SUPPORTS DRAG AND DROP**.

This is done by adding the below css and settings `css_classes=["pnx-file-upload-area"]` on
the `FileInput` widget.

```css
.pnx-file-upload-area input[type=file] {
    width: 100%;
    height: 100%;
    border: 3px dashed #9E9E9E;
    background: transparent;
    border-radius: 5px;
    text-align: left;
    margin: auto;
}
```

If you want a nicer looking `FileInput` in Panel please upvote
[Github Issue 917](https://github.com/holoviz/panel/issues/917) and join the discussion in
[Discourse 1128](https://discourse.holoviz.org/t/what-should-a-better-fileinput-look-like/1128/3).
"""
import panel as pn
from awesome_panel_extensions.site import site

APPLICATION = site.create_application(
    url="fileinput-area",
    name="FileInput Area",
    author="Marc Skov Madsen",
    description="""Shows how to style the Panel FileInput to give it a modern look and feel""",
    description_long=__doc__,
    thumbnail="fileinput-area.png",
    resources={
        "mp4": "",
        "code": "styling/fileinput-area.py",
    },
    tags=["Styling", "FileInput"],
)

STYLE = """
<style>
.pnx-file-upload-area input[type=file] {
    width: 100%;
    height: 100%;
    border: 3px dashed #9E9E9E;
    background: transparent;
    border-radius: 5px;
    text-align: left;
    margin: auto;
}
</style>"""


@site.add(APPLICATION)
def view():
    """Returns the File Input Area App"""
    pn.config.sizing_mode = "stretch_width"
    fileinput_section = pn.Column(
        pn.pane.HTML(STYLE, width=0, height=0, sizing_mode="stretch_width", margin=0),
        pn.widgets.FileInput(height=100, css_classes=["pnx-file-upload-area"]),
    )
    main = [
        APPLICATION.intro_section(),
        fileinput_section,
    ]
    return pn.template.FastListTemplate(main=main)


if __name__.startswith("bokeh"):
    view().servable()
