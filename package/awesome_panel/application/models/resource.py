"""In this Module we define the Resource model"""

import param

from .author import Author

_IMAGE_DICT = {
    " ": "-",
    "#": "",
}


class Resource(param.Parameterized):
    """Model of a Resource

        Args:
            name (str): The name of the Resource
            url (str): The url to the resource
            thumbnail_png_path (str): A thumbnail image of the resource
            is_awesome (bool): Whether or not the Resource should be included in the awesome-panel
            list of awesome resources.
            tags (Optional[List[Tag]], optional): A list of Tags describing the Resource.
            Used to search for Resources. Defaults to None.
            author (Optional[Author], optional): The author of the resource. Defaults to None.
    """

    url = param.String()
    thumbnail_png_path = param.String()
    is_awesome = param.Boolean()
    tags = param.List(allow_None=True)
    author = param.ClassSelector(class_=Author, allow_None=True)
    description = param.String()

    def to_markdown_bullet(self,) -> str:
        """A markdown bullet string

        Returns:
            str: The Resource as a Markdown bullet string
        """
        result = f"- [{self.name}]({self.url})"
        if self.author:
            result += f" by [{self.author.name}]({self.author.url})"
        if self.tags:
            # pylint: disable=not-an-iterable
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
