import panel as pn
import param


class MyClass(param.Parameterized):
    value = param.Boolean()

    @param.depends("value")
    def view(self):
        return pn.pane.Markdown(str(self.value))


def test_depends_func():
    view = MyClass().view
    main = [view]
    template = pn.template.VanillaTemplate(main=main)
    template.show()
