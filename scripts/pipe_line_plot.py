import panel as pn
import param

pipeline = pn.pipeline.Pipeline(inherit_params=False)


class Stage(param.Parameterized):
    stage = param.String()

    def __repr__(self):
        return "hello"

    def __str__(self):
        return "hello"

    def panel(self):
        return pn.Spacer(height=200, sizing_mode="stretch_width", background="blue")


for i in range(0, 20):
    pipeline.add_stage(f"Stage Name {i}", Stage())

layout = pipeline.layout
layout.sizing_mode = "stretch_both"
layout.servable()
