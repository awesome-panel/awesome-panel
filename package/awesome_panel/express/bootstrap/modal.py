"""In this module we provide the functionality of a Modal.

The Modal can be used to focus some kind of information like text, images, chart or an interactive
dashboard.

The implementation is inspired by

- https://css-tricks.com/considerations-styling-modal/
    - https://codepen.io/henchmen/embed/preview/PzQpvk
- https://getbootstrap.com/docs/4.3/components/modal/
"""
import panel as pn
import param

_CSS = """
.bk.modal {
  /* This way it could be display flex or grid or whatever also. */
  display: block;
  max-width: 100%;
  max-height: 100%;
  position: fixed!important;
  z-index: 100;

  left: 0!important;
  top: 0!important;
  bottom: 0!important;
  right: 0!important;

  margin: auto!important;
  box-shadow: 5px 5px 20px grey;
  box-shadow: 0 0 60px 10px rgba(0, 0, 0, 0.9);

  border: 1px solid rgba(0,0,0,.125);
  border-radius: 0.25rem;
}
.closed {
  display: none!important;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 50;

  background: rgba(0, 0, 0, 0.6);
}
.modal-body {
  overflow: auto;
}
"""


class Modal(param.Parameterized):
    """The Modal can be used to focus some kind of information like text, images, chart or an
    interactive dashboard.

    In order to use this modal you need to

    - Instantiate the Modal
    - Add the CSS from the get_css function to the app
        - using `pn.config.raw_css.append` or
        - directly in your template

    The implementation is inspired by

    - https://css-tricks.com/considerations-styling-modal/
        - https://codepen.io/henchmen/embed/preview/PzQpvk
    - https://getbootstrap.com/docs/4.3/components/modal/
    """

    title = param.String(default="Modal")
    body = param.List()

    def __init__(self, **params):
        super().__init__(**params)
        self.modal_overlay = pn.pane.HTML('<div class="modal-overlay" id="modal-overlay"></div>')
        self.close_button = pn.widgets.Button(
            name="X", css_classes=["close-modal-button"], width=50,
        )
        self.close_button.js_on_click(
            code="""
    var modal = document.querySelector(".bk.modal");
    var modalOverlay = document.querySelector("#modal-overlay");
    modal.classList.toggle("closed");
    modalOverlay.classList.toggle("closed");
    """
        )
        self._modal_title = pn.pane.Markdown("# " + self.title)
        self._modal_body = pn.Column(*self.body)  # pylint: disable=not-an-iterable

        self.modal = pn.Column(
            pn.Column(
                pn.Row(self._modal_title, pn.layout.HSpacer(), self.close_button,),
                pn.layout.Divider(),
                self._modal_body,
                sizing_mode="stretch_width",
                margin=10,
            ),
            background="white",
            width=400,
            height=400,
            css_classes=["modal"],
        )

    @staticmethod
    def get_open_modal_button(name: str = "Open Modal", **kwargs) -> pn.widgets.Button:
        """A Button to open the modal with"""
        open_modal_button = pn.widgets.Button(
            name=name, css_classes=["open-modal-button"], **kwargs
        )
        open_modal_button.js_on_click(
            code="""
    var modal = document.querySelector(".modal");
    var modalOverlay = document.querySelector("#modal-overlay");

    modal.classList.toggle("closed");
    modalOverlay.classList.toggle("closed");
    """
        )

        return open_modal_button

    @staticmethod
    def get_css() -> str:
        """Add the CSS from this function to the app

        - using `pn.config.raw_css.append` or
        - directly in your template

        Returns:
            str: The css string
        """
        return _CSS

    @param.depends(
        "title", watch=True,
    )
    def set_modal_title(self,):
        """Updates the title of the modal"""
        self._modal_title.object = "# " + self.title

    @param.depends(
        "body", watch=True,
    )
    def set_modal_body(self,):
        """Updates the body of the modal"""
        self._modal_body[:] = self.body
