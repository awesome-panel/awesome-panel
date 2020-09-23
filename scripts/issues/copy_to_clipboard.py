import panel as pn


def copy_to_clipboard():
    """### Copy to Clipboard Example

    This example was developed as a response to
    [Discourse Post 949](https://discourse.holoviz.org/t/using-panel-with-javascript-to-make-a-copy-text-to-clipboard-button/949)
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


copy_to_clipboard().servable()
