"""Models of Resource, Author and Tag used to defined the RESOURCES and APPS_IN_GALLERY list."""
from awesome_panel.models.resource import Resource
import param

class Page(Resource):
    description = param.String()