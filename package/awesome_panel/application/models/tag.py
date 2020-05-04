"""Models of Resource, Author and Tag used to defined the RESOURCES and APPS_IN_GALLERY list."""


import param

from awesome_panel.utils import OrderByNameMixin


class Tag(OrderByNameMixin, param.Parameterized):
    """Model of a Tag"""

    name = param.String()

    def __str__(self,):
        return self.name

    def __repr__(self,):
        return self.name

    def __hash__(self,):
        return hash(self.name)
