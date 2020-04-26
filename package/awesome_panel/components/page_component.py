from .component import Component
import panel as pn
import param

class PageComponent(Component):
    def view(self, **params):
        raise NotImplementedError

    @classmethod
    def create(cls, object):
        if isinstance(object, pn.layout.Reactive):
            return ReactivePageComponent(object=object)
        if isinstance(object, param.Parameterized):
            return ParameterizedClassComponent(object=object)
        raise NotImplementedError()

class ReactivePageComponent(PageComponent):
    object = param.ClassSelector(class_=pn.layout.Reactive)

    def view(self):
        return self.object

class ParameterizedClassComponent(PageComponent):
    object = param.ClassSelector(class_=param.Parameterized)

    def view(self):
        if hasattr(self.object, "view") and callable(self.object.view):
            return self.object.view()
        else:
            return self.object