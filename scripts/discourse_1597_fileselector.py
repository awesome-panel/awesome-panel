import panel as pn
import param

class Dashboard(param.Parameterized):
    file_selector = param.FileSelector()
    progress = pn.widgets.Progress(active=False)

    @param.depends('file_selector', watch=True)
    def activate_upload_status(self):
        self.progress.active = True

dashboard=Dashboard()
pn.Column(dashboard.progress, pn.Param(dashboard.param.file_selector)).servable()