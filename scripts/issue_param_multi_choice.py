import panel as pn
import param

YEARS = [2020, 2021]


class MyClass(param.Parameterized):
    years = param.List(label="Years")


instance = MyClass()
years_widget = pn.widgets.MultiChoice(options=YEARS)
years_dict = {
    "type": pn.widgets.MultiChoice,
    "options": YEARS,
    "margin": (0, 50, 0, 0),
    "width": 250,
}
pn.Param(instance, parameters=["years"], widgets={"years": years_dict}).servable()
