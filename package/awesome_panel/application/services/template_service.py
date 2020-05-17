"""This module implementes the TemplateService

The TemplateService enables the user to change the Template of the application"""
import param


class TemplateService:  # pylint: disable=too-few-public-methods
    """The TemplateService enables the user to change the Template of the application"""

    template = param.ObjectSelector(
        allow_None=False, doc="The Template to be used to view the application"
    )
