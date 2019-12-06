import panel as pn

text = r"""
<link href="https://use.fontawesome.com/releases/v5.11.2/css/all.css" rel="stylesheet">
<style>
div.bk.navigation div.bk button {
    text-align: left !important;
}
div.bk.icon div.bk *::before {
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
}

div.bk.login div.bk *::before {
    font-family: "Font Awesome 5 Free"; font-weight: 900; content: "\f007";
}

div.bk.tps div.bk *::before {
    font-family: "Font Awesome 5 Free"; font-weight: 400; content: "\f1ea";
}

div.bk.twitter div.bk *::before {
    font-family: "Font Awesome 5 Brands"; content: "\f099";
}

</style>

<ul style="margin: 0;">
  <li><span class="icon login"></span> Login</li>
  <li class="icon tps"> TPS Reports</li>
  <li><span class="icon twitter"></span> Twitter</li>
</ul>
"""
example = pn.pane.HTML(text)
button = pn.widgets.Button(
    name="hello", css_classes=["icon", "twitter", "navigation"], align="start"
)
app = pn.Column(example, button)
app.servable()

