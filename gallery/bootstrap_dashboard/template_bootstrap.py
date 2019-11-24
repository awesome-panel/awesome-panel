import panel as pn
import param
import pathlib
from awesome_analytics_apps import stack_overflow

TEMPLATES_ROOT = pathlib.Path(__file__).parent / "templates"
BOOTSTRAP_DASHBOARD_TEMPLATE = TEMPLATES_ROOT / "bootstrap_dashboard.html"


def main() -> pn.Pane:
    app = wrap_in_template(get_main())
    return app


def get_main() -> pn.Pane:
    questions = Questions()

    return pn.Column(
        pn.Row(
            youtube(uid="L91rd1D6XTA"), pn.layout.HSpacer(), sizing_mode="stretch_width"
        ),
        questions.param,
        questions.questions,
        sizing_modes="stretch_width",
        width_policy="max",
    )


def youtube(uid: str) -> pn.Pane:
    return pn.pane.HTML(
        f"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/{uid}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
"""
    )


class Questions(param.Parameterized):
    rows = param.Integer(default=10, bounds=(0, 100))
    df = stack_overflow.read_schema()

    @param.depends("rows")
    def questions(self) -> pn.Pane:
        return pn.Pane(self.df[0 : self.rows])


def wrap_in_template(app: pn.Pane) -> pn.Pane:
    with open(BOOTSTRAP_DASHBOARD_TEMPLATE, "r") as file:
        bootstrap_dashboard_template = file.read()
    template = pn.Template(bootstrap_dashboard_template)
    template.add_panel("app", app)
    return template


if __name__ == "__main__" or __name__.startswith("bk_script"):
    main().servable()
