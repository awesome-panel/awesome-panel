import param
import panel as pn
import holoviews as hv
from param import parameterized


class testview(param.Parameterized):
    check_val = param.Integer(default=0)
    parameters = param.List(default=[])

    def add_parameters(self, k):
        parameters = self.parameters
        for i in range(k):
            name = f"param{i}"
            self.param._add_parameter(name, param.Integer(default=0))
            parameters.append(name)
        self.param.watch(self.increment_val, parameters)
        self.parameters = parameters

    def increment_val(self, *events):
        self.check_val += 1
        print(self.check_val)

    @param.depends("check_val")
    def plot(self):
        print("plot")
        return hv.Text(0.5, 0.5, str(self.check_val))


viewer = testview()
viewer.add_parameters(3)
pn.Row(pn.Param(viewer.param, parameters=viewer.parameters), viewer.plot).servable()
