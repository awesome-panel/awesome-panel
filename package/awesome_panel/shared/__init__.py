"""In this module we define a Model"""
import param


class Model(param.Parameterized):
    """A Domain Model"""

    def __str__(self,):
        return self.name

    def __repr__(self,):
        return self.name
