import param

class TemplateService():
    template = param.ObjectSelector(allow_None=False, doc="The Template to be used to view the application")
