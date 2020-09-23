import panel as pn
import param


class Leg(param.Parameterized):
    value = param.Number(default=1, bounds=(0, 1))

    def __str__(self):
        return str(self.value)


shapes = [Leg(), Leg()]


class Spread(param.Parameterized):
    leg1 = param.Parameter(shapes[0])
    data = param.Number()

    def __init__(self, **params):
        super().__init__(**params)

    @param.depends("leg1", "leg1.value", watch=True)
    def _update_data(self):
        self.data = self.leg1.value


spread = Spread()
pn.Column(
    spread.leg1.param,
    pn.Param(spread, parameters=["leg1", "data"]),
).servable()

# from bokeh.plotting import figure
# import numpy as np

# class Shape(param.Parameterized):

#     radius = param.Number(default=1, bounds=(0, 1))

#     def __init__(self, **params):
#         super(Shape, self).__init__(**params)
#         self.figure = figure(x_range=(-1, 1), y_range=(-1, 1))
#         self.renderer = self.figure.line(*self._get_coords())

#     def _get_coords(self):
#         return [], []

#     def view(self):
#         return self.figure


# class Circle(Shape):

#     n = param.Integer(default=100, precedence=-1)

#     def _get_coords(self):
#         angles = np.linspace(0, 2 * np.pi, self.n + 1)
#         return (self.radius * np.sin(angles), self.radius * np.cos(angles))

#     @param.depends("radius", watch=True)
#     def update(self):
#         xs, ys = self._get_coords()
#         self.renderer.data_source.data.update({"x": xs, "y": ys})


# class NGon(Circle):

#     n = param.Integer(default=3, bounds=(3, 10), precedence=1)

#     @param.depends("radius", "n", watch=True)
#     def update(self):
#         xs, ys = self._get_coords()
#         self.renderer.data_source.data.update({"x": xs, "y": ys})


# shapes = [NGon(), Circle()]


# class ShapeViewer(param.Parameterized):

#     shape = param.ObjectSelector(default=shapes[0], objects=shapes)

#     @param.depends("shape")
#     def view(self):
#         return self.shape.view()

#     @param.depends("shape", "shape.radius")
#     def title(self):
#         return "## %s (radius=%.1f)" % (type(self.shape).__name__, self.shape.radius)

#     def panel(self):
#         return pn.Column(self.title, self.view)


# viewer = ShapeViewer()

# pn.Row(viewer.param, viewer.panel()).servable()
