import param
import panel as pn
class Test(param.Parameterized):
    window_size = param.Integer(default=6, bounds=(1, 21))
    test = param.Integer()
    
    @param.depends('window_size', watch=True)
    def update(self):
        self.test=self.window_size

    @param.depends("test")
    def view(self):
        return "Test: " + str(self.test)
    
test = Test(name='Test')
pn.Column(test.param, test.view).servable()
