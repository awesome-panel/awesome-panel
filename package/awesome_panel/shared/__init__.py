import param

class Model(param.Parameterized):
    def __str__(self,):
        return self.name

    def __repr__(self,):
        return self.name