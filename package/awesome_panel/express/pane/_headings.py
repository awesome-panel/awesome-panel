"""In this module we implement a title, heading and subheading"""
from typing import Optional

import panel as pn


class HeadingBase(pn.pane.Markdown):
    """Base class for headings like Title, Header and SubHeader"""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        text: str = "",
        level: int = 1,
        sizing_mode="stretch_width",
        text_align="left",
        url: Optional[str] = None,
        **kwargs,
    ):
        """Base class for headings like Title, Header and SubHeader

        Keyword Arguments:
            text {str} -- The heading to display (default: {""})
            level {int} -- 1 is Title, 2 is Header, ... (default: {1})
            sizing_mode {str} -- (default: {"stretch_width"})
            text_align {str} -- The header can be aligned 'left', 'center' or 'right'
                (default: {"left"})
            url {Optional[str]} -- If not None the heading will link to the url
        """
        if url:
            heading = f"{'#'*level} [{text}]({url})"
        else:
            heading = f"{'#'*level} {text}"
        if "style" in kwargs:
            kwargs["style"]["text-align"] = text_align
        else:
            kwargs["style"] = {"text-align": text_align}
        super().__init__(
            heading,
            sizing_mode=sizing_mode,
            **kwargs,
        )


class Title(HeadingBase):
    """A Markdown Pane with the title"""

    def __init__(
        self,
        text: str = "",
        sizing_mode="stretch_width",
        text_align="left",
        url: Optional[str] = None,
        **kwargs,
    ):
        """A Markdown Pane with the title

        Keyword Arguments:
            text {str} -- The title to display (default: {""})
            sizing_mode {str} -- (default: {"stretch_width"})
            text_align {str} -- The header can be aligned 'left', 'center' or 'right'
                (default: {"left"})
            url {Optional[str]} -- If not None the heading will link to the url
        """
        super().__init__(
            text=text,
            level=1,
            sizing_mode=sizing_mode,
            text_align=text_align,
            url=url,
            **kwargs,
        )


class Header(HeadingBase):
    """A Markdown Pane with the header"""

    def __init__(
        self,
        text: str = "",
        sizing_mode="stretch_width",
        text_align="left",
        url: Optional[str] = None,
        **kwargs,
    ):
        """A Markdown Pane with the header

        Keyword Arguments:
            text {str} -- The header to display (default: {""})
            sizing_mode {str} -- (default: {"stretch_width"})
            text_align {str} -- The header can be aligned 'left', 'center' or 'right'
                (default: {"left"})
            url {Optional[str]} -- If not None the heading will link to the url
        """
        super().__init__(
            text=text,
            level=2,
            sizing_mode=sizing_mode,
            text_align=text_align,
            url=url,
            **kwargs,
        )


class SubHeader(HeadingBase):
    """A Markdown Pane with the sub header"""

    def __init__(
        self,
        text: str = "",
        sizing_mode="stretch_width",
        text_align="left",
        url: Optional[str] = None,
        **kwargs,
    ):
        """A Markdown Pane with the sub header

        Keyword Arguments:
            text {str} -- The sub header to display (default: {""})
            sizing_mode {str} -- (default: {"stretch_width"})
            text_align {str} -- The header can be aligned 'left', 'center' or 'right'
                (default: {"left"})
            url {Optional[str]} -- If not None the heading will link to the url
        """
        super().__init__(
            text=text,
            level=3,
            sizing_mode=sizing_mode,
            text_align=text_align,
            url=url,
            **kwargs,
        )
