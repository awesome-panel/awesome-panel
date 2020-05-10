import param
import panel as pn


class Component1(param.Parameterized):
    pass


class Component2(param.Parameterized):
    pass


class Service(param.Parameterized):
    component = param.Parameter()
    do_something = param.Action()
    another = param.String()


service1 = Service(name="Service 1")
service2 = Service(name="Service 2")

SERVICES = [service1, service2]


class Designer(param.Parameterized):
    service = param.ObjectSelector()
    service_pane = param.ClassSelector(class_=pn.Param)
    view = param.Parameter()

    def __init__(self, services):
        self.param.service.objects = services
        self.param.service.default = services[0]

        super().__init__()

        self.service_pane = pn.Param(self.param.service, parameters=["do_something"])
        self.service = services[0]
        self.view = pn.Column(
            pn.Param(self, parameters=["service"], show_name=False, expand_button=None),
            self.service_pane,
        )


Designer(SERVICES).view.show()
