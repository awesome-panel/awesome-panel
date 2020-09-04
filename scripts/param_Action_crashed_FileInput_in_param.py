import param
import panel as pn
import pandas as pd
from io import StringIO

class TryFileDownload(param.Parameterized):

    data=pd.DataFrame({"a": [1]})
    button1 = param.Action()
    button2 = param.Action()

    def __init__(self,**params):
        super().__init__(**params)
        self.button1 = self.do_something_button1
        self.button2 = self.do_something_button2
        self.file_download = pn.widgets.FileDownload(filename="data.csv", callback=self.get_file)

    def do_something_button1(self, *events):
        print('Dummy print button1')

    def do_something_button2(self, *events):
        print('Dummy print button2')


    def get_file(self):
        output = StringIO()
        self.data.to_csv(output)
        output.seek(0)
        return output

tfd = TryFileDownload()
pn.Column(
    pn.Param(tfd), tfd.file_download
).servable()
