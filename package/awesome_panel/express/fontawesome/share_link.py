"""This module provides button to share on social media"""
import urllib.parse

import panel as pn
import param

DEFAULT_URL = "https://awesome-panel.org"
DEFAULT_CLASS = "fas fa-external-link-alt"
DEFAULT_TEXT = "Checkout"
FACEBOOK_CLASS = "fab fa-facebook-f"
LINKEDIN_CLASS = "fab fa-linkedin-in"
TWITTER_CLASS = "fab fa-twitter"
REDDIT_CLASS = "fab fa-reddit-alien"
MAIL_CLASS = "fas fa-envelope"


class ShareOnBase(param.Parameterized):
    """Base class for implementing ShareOnFacebook, ShareOnLinkedIn links etc.

    - The href property should be overridden
    """

    url = param.String(DEFAULT_URL)
    icon_class = param.String(DEFAULT_CLASS)
    text = param.String(DEFAULT_TEXT)

    @property
    def _url_parsed(
        self,
    ):
        return urllib.parse.quote(self.url).replace(
            "/",
            "%2F",
        )

    @property
    def href(
        self,
    ) -> str:
        """The href to goto when clicked

        Override this method in a base class

        Raises:
            NotImplementedError:

        Returns:
            str: A href string
        """
        raise NotImplementedError()

    def __html__(
        self,
    ) -> str:
        """A html string with link and icon tags

        Returns:
            str: A html string with link and icon tags
        """
        return (
            f'<a href="{self.href}" class="button-share-link">'
            f'<i class="{self.icon_class}"></i></a>'
        )

    @param.depends(
        "url",
        "icon_class",
    )
    def view(
        self,
    ) -> pn.pane.HTML:
        """A HTML pane with the a link and icon

        Returns:
            pn.pane.HTML: A HTML pane with the link and icon
        """
        return pn.pane.HTML(self.__html__())


class ShareOnFacebook(ShareOnBase):
    """A Share on Facebook button"""

    icon_class = param.String(FACEBOOK_CLASS)

    @property
    def href(
        self,
    ):
        return f"https://www.facebook.com/sharer/sharer.php?u={self._url_parsed}"


class ShareOnLinkedIn(ShareOnBase):
    """A Share on LinkedIn button"""

    icon_class = param.String(LINKEDIN_CLASS)

    @property
    def href(
        self,
    ):
        return (
            f"http://www.linkedin.com/shareArticle?mini=true&url={self._url_parsed}"
            f"&title={self.text}"
        )


class ShareOnTwitter(ShareOnBase):
    """A Share on Twitter button"""

    icon_class = param.String(TWITTER_CLASS)

    @property
    def href(
        self,
    ):
        return f"https://twitter.com/intent/tweet?url={self._url_parsed}&text={self.text}"


class ShareOnReddit(ShareOnBase):
    """A Share on Reddit button"""

    icon_class = param.String(REDDIT_CLASS)

    @property
    def href(
        self,
    ):
        return f"https://reddit.com/submit?url={self._url_parsed}&amp;title={self.text}"


class ShareOnMail(ShareOnBase):
    """A Share on Mail button"""

    icon_class = param.String(MAIL_CLASS)

    @property
    def href(
        self,
    ):
        return f"mailto:?subject={self._url_parsed}&amp;body={self.text}&nbsp;{self._url_parsed}"
