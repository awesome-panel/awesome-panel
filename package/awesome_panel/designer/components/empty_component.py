"""This module provides the EmptyComponent to be used if no component is provided to the
Designer"""
import panel as pn
import param


class EmptyComponent(param.Parameterized):
    """Dummy Component used by the Designer when no component is provided"""

    view = param.ClassSelector(class_=pn.Column)

    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.Column("# Empty Component")
