import panel as pn

def get_template() -> pn.template.BaseTemplate:
    template = pn.template.VanillaTemplate()

    template.title = "Awesome Panel"
    return template