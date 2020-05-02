import panel as pn

text = """\
## Wide images in markdown overflows the page

A wide image in markdown overflows the page

**I think it's a friction point that could be easily solved by setting `max-width: 100%` in the default css of Panel**.
Or alternative by default adding `max-width: 100%` to the styling of the `pn.pane.Markdown` unless otherwise specified

![Overflow image](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)

"""

# <img application="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true" style="max-width: 100%" />

markdown = pn.pane.Markdown(text)
app = pn.Column(markdown, width=500,)
app.servable()
