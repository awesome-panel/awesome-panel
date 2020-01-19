"""This code is used to understand how I can show 2 out of 3 parameters in a parametrized class
with custom widgets or settings.

I would really like to make view3 more efficient, i.e. only have one `pn.Param` statement as in
view2. The reason being the I have sometimes experienced that the layout is better with one
instead of multiple `pn.Param`. See
[discourse](https://discourse.holoviz.org/t/how-do-i-align-two-widgets-in-a-row/82). And for example
here there is extra space between show_me2 and show_me3 in view3.
"""
import panel as pn
import param


class Example(param.Parameterized):
    show_me1 = param.Boolean()
    show_me2 = param.String("Show me 2")
    show_me3 = param.String("Show me 3")


example = Example()

view1 = pn.Column(example.param)
view2 = pn.Param(example.param, widgets={"show_me2": {"width": 200,}, "show_me3": {"width": 300},},)
view3 = pn.Param(
    example,
    parameters=["show_me2", "show_me3"],
    widgets={"show_me2": {"width": 200,}, "show_me3": {"width": 300,}},
)

app = pn.Column(
    __doc__,
    pn.Row(
        pn.Column("# 1 - All Parameters", view1,),
        pn.Column("# 2 - All Parameters - custom Widgets", view2,),
        pn.Column("# 3 - Selected Parameters - custom widgets", view3,),
    ),
)
app.servable()
