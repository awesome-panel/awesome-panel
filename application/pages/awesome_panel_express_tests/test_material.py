"""The Material components can give your app **more modern look and feel** than using the default
Panel components. The Material components are a part of the [`awesome-panel-extensions`]\
(https://pypi.org/project/awesome-panel-extensions/) package.

You can find the REFERENCE GUIDES [here](https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html#material)

Right now it is just a PROOF OF CONCEPT. But I would like (some one) to implement the full set of
Material Widgets. They can be implemented using for example the
[MWC Web Components](https://github.com/material-components/material-components-web-components)
"""
import panel as pn
from awesome_panel_extensions.frameworks import material

from application.config import site

APPLICATION = site.create_application(
    url="material-components",
    name="Material Components",
    author="Marc Skov Madsen",
    introduction="""This app demonstrates the look and feel of the Material Components from the
    awesome-panel-extensions package""",
    description=__doc__,
    thumbnail_url="test_material_components.png",
    documentation_url="",
    code_url="awesome_panel_express_tests/test_material.py",
    gif_url="",
    mp4_url="",
    tags=[],
)


def section(component, message=None, show_html=False):
    """Helper function. Turns the component into a tuple of components containing

    - Title
    - Description
    - The Component
    - A Param of the Component parameters
    - A Divider
    """
    title = "## " + str(type(component)).split(".")[4][:-2]

    parameterset = set(component._child_parameters())  # pylint: disable=protected-access
    parameterset = [parameter for parameter in parameterset if "_" not in parameter]
    if show_html:
        parameterset.add("html")
    for parameter in component.parameters_to_watch:
        parameterset.add(parameter)

    parameters = list(parameterset)
    if message:
        return (
            pn.pane.Markdown(title),
            component,
            pn.Param(component, parameters=parameters),
            pn.pane.Markdown(message),
            pn.layout.Divider(),
        )
    return (
        pn.pane.Markdown(title),
        component,
        pn.Param(component, parameters=parameters, show_name=False),
        pn.layout.Divider(),
    )


@site.add(APPLICATION)
def view(configure=True) -> pn.Column:
    """Returns a view of the Material Components

    Args:
        configure (bool, optional): Set this to True to include Material JS and CSS.
        Defaults to False.

    Returns:
        pn.Column: A Column view of the Material Components
    """
    pn.config.sizing_mode = "stretch_width"
    button = material.Button(name="Click Me", icon="favorite")
    # select = material.Select(name="Select me", options=["Data", "Models", "Analytics"], value="Analytics", icon="favorite",)
    intslider = material.IntSlider(name="Slider", value=3, start=1, end=9, step=2)
    floatslider = material.FloatSlider(name="Slide Me", value=2.5, start=0.0, end=5.0, step=0.1)
    linear_progress = material.LinearProgress(name="Progress", value=10, max=100)
    circular_progress = material.CircularProgress(name="Progress", value=75, max=100, density=25)

    objects = [
        APPLICATION.intro_section(),
        pn.pane.Alert("If you don't see the components please reload the page!"),
        *section(button),
        *section(intslider),
        *section(floatslider),
        # *section(select),
        *section(linear_progress),
        *section(circular_progress),
    ]

    if configure:
        objects.append(material.Extension())

    return site.create_template(
        title="Material Components", template="material", main=objects, main_max_width="500px"
    )


if __name__.startswith("bokeh"):
    view(configure=True).servable()
