import param
from .progress import Progress
from .message import Message

class Application(param.Parameterized):
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

    def __init__(
        self, templates, pages, menu_items=[], source_links=[], social_links=[], **params
    ):
        self.param.template.objects = templates
        if "template" in params:
            self.param.template.default = params["template"]
        else:
            self.param.template.default = templates[0]
        self.param.page.objects = pages
        if pages:
            self.param.page.default = pages[0]
        self.param.menu_item.objects = menu_items
        self.param.source_link.objects = source_links
        self.param.social_link.objects = social_links

        super().__init__(**params)

        self.progress = Progress(name="Progress")
        self.message = Message(name="Message")
