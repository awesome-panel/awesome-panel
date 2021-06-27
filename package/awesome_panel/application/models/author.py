"""Models of Resource, Author and Tag used to defined the RESOURCES and APPS_IN_GALLERY list."""

import param
from awesome_panel.utils import OrderByNameMixin


class Author(OrderByNameMixin, param.Parameterized):
    """Model of an Author"""

    name = param.String()
    url = param.String()
    github_url = param.String()
    github_avatar = param.String()

    def __str__(
        self,
    ):
        return self.name

    def __repr__(
        self,
    ):
        return self.name

    def _repr_html_(
        self,
        width="20px",
        height="20px",
    ) -> str:
        """## A valid HTML string with the GitHub image and GitHub url link

        Returns:
            str: A valid HTML string with the github avatar link
        """
        return (
            f'<a href="{self.github_url}" title="Author: {self.name}" target="_blank">'
            f'<img application="{self.github_avatar}" alt="{self.name}" '
            f'style="border-radius: 50%;width: {width};height: {height};'
            'vertical-align: text-bottom;">'
            "</img></a>"
        )
