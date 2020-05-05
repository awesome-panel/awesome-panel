"""In this module we define the Application model.

It provides the basic parameters of an application"""
import param

from .message import Message
from .progress import Progress


class Application(param.Parameterized):
    """The Application Model provides the basic parameters of an application"""

    title = param.String()
    url = param.String()
    logo = param.String()
    template = param.ObjectSelector()
    page = param.ObjectSelector()
    menu_item = param.ObjectSelector(allow_None=True)
    source_link = param.ObjectSelector(allow_None=True)
    social_link = param.ObjectSelector(allow_None=True)
    progress = param.ClassSelector(class_=Progress)
    message = param.ClassSelector(class_=Message)

    def __init__( # pylint: disable=too-many-arguments
        self, templates, pages, menu_items=None, source_links=None, social_links=None, **params
    ):
        self.param.template.objects = templates
        if "template" in params:
            self.param.template.default = params["template"]
        else:
            self.param.template.default = templates[0]
        self.param.page.objects = pages
        if pages:
            self.param.page.default = pages[0]

        if menu_items:
            self.param.menu_item.objects = menu_items
        else:
            self.param.menu_item.objects = []
        if source_links:
            self.param.source_link.objects = source_links
        else:
            self.param.source_link.objects = []
        if social_links:
            self.param.social_link.objects = social_links
        else:
            self.param.social_link.objects = []

        super().__init__(**params)

        self.progress = Progress(name="Progress")
        self.message = Message(name="Message")
