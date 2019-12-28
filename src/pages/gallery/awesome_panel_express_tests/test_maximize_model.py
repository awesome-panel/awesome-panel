"""Here we test functionality to maximize an existing Panel to a modal window so that it's easier
to study and learn from the content

Inspired by https://css-tricks.com/considerations-styling-modal/
"""

import panel as pn

CSS = """
.modal {
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
  box-shadow: 0 0 60px 10px rgba(0, 0, 0, 0.9);
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
.modal-guts {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  padding: 20px 50px 20px 20px;
}
body {
  background-color:#556;
  background-image: linear-gradient(30deg, #445 12%, transparent 12.5%, transparent 87%, #445 87.5%, #445),
  linear-gradient(150deg, #445 12%, transparent 12.5%, transparent 87%, #445 87.5%, #445),
  linear-gradient(30deg, #445 12%, transparent 12.5%, transparent 87%, #445 87.5%, #445),
  linear-gradient(150deg, #445 12%, transparent 12.5%, transparent 87%, #445 87.5%, #445),
  linear-gradient(60deg, #99a 25%, transparent 25.5%, transparent 75%, #99a 75%, #99a),
  linear-gradient(60deg, #99a 25%, transparent 25.5%, transparent 75%, #99a 75%, #99a);
  background-size:80px 140px;
  background-position: 0 0, 0 0, 40px 70px, 40px 70px, 0 0, 40px 70px;

  font-family: 'Prompt', sans-serif;
}
"""
pn.config.raw_css.append(CSS)


def view():
    modal_overlay = pn.pane.HTML('<div class="modal-overlay" id="modal-overlay"></div>')
    open_modal_button = pn.widgets.Button(name="Open Button", css_classes=["open-modal-button"])
    open_modal_button.js_on_click(
        code="""
var modal = document.querySelector(".modal");
var modalOverlay = document.querySelector("#modal-overlay");

modal.classList.toggle("closed");
modalOverlay.classList.toggle("closed");
"""
    )
    close_modal_button = pn.widgets.Button(
        name="Obvious Close Button", css_classes=["close-modal-button"]
    )
    close_modal_button.js_on_click(
        code="""
var modal = document.querySelector(".bk.modal");
var modalOverlay = document.querySelector("#modal-overlay");
modal.classList.toggle("closed");
modalOverlay.classList.toggle("closed");
"""
    )

    modal_guts = pn.pane.HTML(
        """
<h1>Modal Example</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae expedita corrupti laudantium aperiam, doloremque explicabo ipsum earum dicta saepe delectus totam vitae ipsam doloribus et obcaecati facilis eius assumenda, cumque.</p>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae expedita corrupti laudantium aperiam, doloremque explicabo ipsum earum dicta saepe delectus totam vitae ipsam doloribus et obcaecati facilis eius assumenda, cumque.</p>
        """,
        css_classes=["modal-guts"],
    )
    modal = pn.Column(
        close_modal_button,
        modal_guts,
        width=400,
        height=400,
        background="white",
        css_classes=["modal"],
    )
    return pn.Column(open_modal_button, modal_overlay, modal, sizing_mode="stretch_both")


if __name__.startswith("bk"):
    view().servable()
