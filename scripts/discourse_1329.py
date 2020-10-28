import param


class Test1(param.Parameterized):
    input_dict = param.Dict(default=None, allow_None=False)

    def __init__(self, something_else=None, **kwds):
        self.something = kwds.pop("something", None)

        super().__init__(**kwds)

        self.something_else = something_else


Test1()
Test1(something=["something"])
Test1(something_else=["something_else"])
Test1(something=["something"], something_else=["something_else"])

print("Done")
