import param
import panel as pn

class A(param.Parameterized):
    select = param.Selector(objects=['opt1', 'opt2'])

    field1 = param.Selector(objects=['a1', 'a2', 'a3'], label='Field1')
    number1 = param.Number(3)

    field2 = param.Selector(objects=['b1', 'b2', 'b3'], label='Field2')
    number2 = param.Number(5)

    def __init__(self, **param):
        super(A, self).__init__(**param)

        panel1 =  pn.panel(self.param, parameters=['field1', 'number1'], widgets={'field1': pn.widgets.RadioButtonGroup})
        self.col1 = pn.Column(*panel1[1:])

        panel2 =  pn.panel(self.param, parameters=['field2', 'number2'], widgets={'field2': pn.widgets.RadioButtonGroup})
        self.col2 = pn.Column(*panel2[1:])

        self.column = pn.Column(panel1, self.col1)

    @param.depends('select', watch=True)
    def _update_select(self):
        if self.select == 'opt1':
            self.column[1] = self.col1
        elif self.select == 'opt2':
            self.column[1] = self.col2

    def panel(self):
        return self.column

a = A()
a.panel().show()