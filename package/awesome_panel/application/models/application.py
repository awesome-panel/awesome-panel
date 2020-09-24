"""In this module we define the Application model.

It provides the basic parameters of an application"""
import param
from awesome_panel.application.models.page import Page

# from awesome_panel.application.models.template import Template


class Application(param.Parameterized):
    """The Application Model provides the basic parameters of an application"""

    title = param.String(
        allow_None=False, doc="The Title to show to the user. For example 'AWESOME-PANEL'"
    )
    url = param.String(
        allow_None=False,
        doc="The full url to the application. For example 'https://awesome-panel.org",
    )
    logo = param.String(allow_None=False, doc="An url to a an image")
    default_page = param.ClassSelector(allow_None=False, class_=Page, doc="The default page to use")
    pages = param.List(allow_None=False, doc="The pages available to the application")
    default_template = param.Parameter()
    templates = param.List(allow_None=False, doc="The templates available to the application")
