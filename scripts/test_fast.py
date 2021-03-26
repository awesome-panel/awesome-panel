import panel as pn


def test_template_theme_parameter():
    template = pn.template.FastGridTemplate(title="Fast", theme="dark")
    # Not '#3f3f3f' which is for the Vanilla theme
    assert template.theme.bokeh_theme._json["attrs"]["Figure"]["background_fill_color"] == "#181818"
    assert template.theme == pn.template.fast.grid.FastDarkTheme
