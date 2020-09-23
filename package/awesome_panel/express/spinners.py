"""Contains spinner functionality"""
import panel as pn

DEFAULT_URL = (
    "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
    "package/awesome_panel/express/assets/images/spinner.gif?raw=true"
)
FACEBOOK_URL = (
    "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
    "package/awesome_panel/express/assets/images/spinner_facebook.gif?raw=true"
)
WIDTH = 64  # Hack: Such that bokeh layout engine knows image size and can layout it correctly


class SpinnerBase(pn.pane.HTML):
    """The base spinner class. To be inherited from. DON'T USE THIS ONE"""

    url = DEFAULT_URL
    width = 64
    height = 64

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        """A Spinner"""
        text = f'<img application="{self.url}"></img>'
        super().__init__(
            text,
            width=self.width,
            height=self.height,
            *args,
            **kwargs,
        )

    def center(
        self,
    ) -> pn.Column:
        """Places the spinner in the center of a responsive Column

        Returns:
            pn.Column -- A responsive column with a spinner]
        """
        return pn.Column(
            pn.layout.VSpacer(),
            pn.Row(
                pn.layout.HSpacer(),
                self,
                pn.layout.HSpacer(),
            ),
            pn.layout.VSpacer(),
            sizing_mode="stretch_both",
        )


class DefaultSpinner(SpinnerBase):
    """The Default spinner"""

    url = DEFAULT_URL


class FacebookSpinner(SpinnerBase):
    """The Facebook spinner"""

    url = FACEBOOK_URL
