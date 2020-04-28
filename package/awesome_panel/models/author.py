"""Models of Resource, Author and Tag used to defined the RESOURCES and APPS_IN_GALLERY list."""
from typing import List, NamedTuple, Optional

class Author(NamedTuple):
    """Model of an Author"""

    name: str
    url: str
    github_url: str
    github_avatar_url: str

    def __str__(self,):
        return self.name

    def __repr__(self,):
        return self.name

    def _repr_html_(self, width="20px", height="20px",) -> str:
        """## A valid HTML string with the GitHub image and GitHub url link

        Returns:
            str: A valid HTML string with the github avatar link
        """
        return (
            f'<a href="{self.github_url}" title="Author: {self.name}" target="_blank">'
            f'<img src="{self.github_avatar_url}" alt="{self.name}" '
            f'style="border-radius: 50%;width: {width};height: {height};'
            'vertical-align: text-bottom;">'
            "</img></a>"
        )