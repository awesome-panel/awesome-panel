import panel as pn
import param
import ptvsd

ptvsd.enable_attach(address=("localhost", 5678,))
ptvsd.wait_for_attach()  # Only include this line if you always wan't to attach the debugger


def action(event,):
    print("Nice to be here!")


class App(param.Parameterized):
    action = param.Action(default=action)

    def view(self,):
        return pn.Column(pn.pane.Markdown("# Hello Panel World"), self.param,)


app = App()
app.view().servable()
