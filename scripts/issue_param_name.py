import param


class HomePage(param.Parameterized):
    name = param.String("Home")


print(HomePage.param.name.default)
