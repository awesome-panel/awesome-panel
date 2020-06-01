import param
import panel as pn


class DETRApp(param.Parameterized):
    input_image_url = param.String("https://panel.holoviz.org/_static/logo_stacked.png", label="Input Image URL")
    run_detr = param.Action(label="Run DE:TR:")
    set_random_image = param.Action(label="Random Image")

    view = param.Parameter()

    def __init__(self, **params):
        params["view"] = self._get_view()
        super().__init__(**params)

    def _get_view(self):
        top_selections = pn.Row(
            pn.Param(
                self,
                parameters=["input_image_url", "run_detr", "set_random_image"],
                widgets={"set_random_image": {"button_type": "success", "align": "end"},
                         "run_detr": {"align": "end"}},
                default_layout=pn.Row, show_name=False,
                width=900,
                )
        )
        app_view = pn.Column(
            top_selections,
        )
        return app_view

DETRApp().view.servable()