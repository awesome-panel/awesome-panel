"""Models of Resource, Author and Tag used to defined the RESOURCES and APPS_IN_GALLERY list."""
import param

from awesome_panel.application.models.tag import Tag
from awesome_panel.application.models.author import Author
from awesome_panel.utils import OrderByNameMixin

class Page(OrderByNameMixin, param.Parameterized):
    author = param.ClassSelector(class_=Author, allow_None=True)
    description = param.String()
    tags = param.List()
    source_code_url = param.String()
    thumbnail_png_url = param.String()
    component = param.Parameter()
    show_loading_page = param.Boolean(default=False)

    def __hash__(self,):
        return hash(self.name)