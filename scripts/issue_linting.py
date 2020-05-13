import param


class MyComponent(param.Parameterized):
    selection = param.ObjectSelector()

    def _update(self):
        print(self.selection)
