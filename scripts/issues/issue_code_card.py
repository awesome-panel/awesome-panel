import panel as pn
import param


class Card(pn.Column):
    def __init__(
        self, header, body, **kwargs,
    ):
        print("__init__")
        content = pn.Row(body)
        header_pane = pn.pane.HTML(f"<h5>{header}</h5>")
        super().__init__(
            header_pane, content, **kwargs,
        )
        return

    def clone(self, **kwargs):
        header, body = self.objects
        return super().clone(header.object, body, **kwargs)


class Dummy(param.Parameterized):
    value = param.Parameter("abcd")


dummy = Dummy()


@param.depends(dummy.param.value)
def get_card(value):
    print("get_card")
    return Card("Code", pn.pane.HTML(f"<strong>{value}</strong>"))


pn.Column(get_card).servable()
