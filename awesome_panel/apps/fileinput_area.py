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

from awesome_panel import config

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


config.extension(url="fileinput_area")

pn.Column(
    pn.pane.HTML(STYLE, width=0, height=0, sizing_mode="stretch_width", margin=0),
    pn.widgets.FileInput(height=100, css_classes=["pnx-file-upload-area"]),
).servable()
