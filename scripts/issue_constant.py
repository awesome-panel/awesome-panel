import param


class T1(param.Parameterized):
    c = param.Parameter(default=None, constant=True)
    d = param.Parameter(constant=False)

    def __init__(self, *argv, **kwarg):
        if "c" not in kwarg and "d" in kwarg:
            kwarg["c"] = 2 * kwarg["d"]

        super().__init__(*argv, **kwarg)


t1 = T1(d=111)
print("t1.c", t1.c)


class T2(param.Parameterized):
    c = param.Parameter(default=None, constant=True)
    d = param.Parameter(constant=False)

    def __init__(self, *argv, **kwarg):
        super().__init__(*argv, **kwarg)

        if self.c is None:
            with param.edit_constant(self):
                self.c = self.d * 2


t2 = T2(d=222)
print("t2.c", t2.c)
