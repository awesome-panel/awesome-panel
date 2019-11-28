import pathlib

import panel as pn


def customers_view(name="Customers"):
    path = pathlib.Path(__file__).parent / "customers.html"
    with open(path, "r") as file:
        template_html = file.read()
    app = pn.Template(template_html)
    app.add_variable("title", name)
    return pn.Column(app, name=name)
