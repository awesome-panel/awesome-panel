"""This module contains the ApplicationComponent"""
import param

from awesome_panel.application.models import Application
from awesome_panel.application.services import Services
from awesome_panel.application.views import ApplicationView


class ApplicationComponent(param.Parameterized):
    """The ApplicationComponent orchestrates the communication between model, services and view"""

    application = param.ClassSelector(class_=Application)
    services = param.ClassSelector(class_=Services)
    view = param.ClassSelector(class_=ApplicationView)
