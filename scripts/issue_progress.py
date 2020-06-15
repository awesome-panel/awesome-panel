import panel as pn

progress = pn.widgets.Progress(active=False)
pn.Column(progress, pn.Param(progress, parameters=["active"])).servable()
progress.active = True
progress.active = False
