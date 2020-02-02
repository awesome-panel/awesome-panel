"""Models of Resource, Author and Tag used to defined the RESOURCES and APPS_IN_GALLERY list."""
from typing import List, NamedTuple, Optional

_IMAGE_DICT = {
    " ": "-",
    "#": "",
}


class Tag(NamedTuple):
    """Model of a Tag"""

    name: str

    def __str__(self,):
        return self.name

    def __repr__(self,):
        return self.name

    def __hash__(self,):
        return hash(self.name)


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

    def to_html(self, width="20px", height="20px",) -> str:
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


class Resource:
    """Model of a Resource

        Args:
            name (str): The name of the Resource
            url (str): The url to the resource
            thumbnail_path (str): A thumbnail image of the resource
            is_awesome (bool): Whether or not the Resource should be included in the awesome-panel
            list of awesome resources.
            tags (Optional[List[Tag]], optional): A list of Tags describing the Resource.
            Used to search for Resources. Defaults to None.
            author (Optional[Author], optional): The author of the resource. Defaults to None.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        url: str,
        thumbnail_path: str,
        is_awesome: bool,
        tags: Optional[List[Tag]] = None,
        author: Optional[Author] = None,
    ):
        self.name = name
        self.url = url
        self.thumbnail_path = thumbnail_path
        self.is_awesome = is_awesome
        if tags:
            self.tags = tags
        else:
            self.tags = []
        self.author = author

    def to_markdown_bullet(self,) -> str:
        """A markdown bullet string

        Returns:
            str: The Resource as a Markdown bullet string
        """
        result = f"- [{self.name}]({self.url})"
        if self.author:
            result += f" by [{self.author.name}]({self.author.url})"
        if self.tags:
            result += " (#" + ", #".join(sorted([tag.name for tag in self.tags])) + ")"

        return result

    def __str__(self,):
        return self.name

    def __repr__(self,):
        return f"Resource(name={self.name})"

    @property
    def screenshot_file(self,) -> str:
        """The file name of a screenshot of the resource

        Returns:
            str: The file name of screenshot of the resource
        """
        file = f"{self.name.lower()}.png"
        for (original, new,) in _IMAGE_DICT.items():
            file = file.replace(original, new,)
        return file
