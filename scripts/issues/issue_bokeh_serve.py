from bokeh.layouts import column
from bokeh.models import Slider
from bokeh.server.server import Server


def get_app(title="My App"):
    def bkapp(doc):
        slider = Slider(start=0, end=30, value=0, step=1, title=title)

        doc.add_root(column(slider))

    return bkapp


applications = {
    "/": get_app("Welcome"),
    "/resources": get_app("Resources"),
    "/about": get_app("About"),
    "/gallery": get_app("Gallery"),
    "/gallery/bootstrap-dashboard": get_app("Bootstrap Dashboard"),
    "/gallery/image-classifier": get_app("Image Classifier"),
}

# Setting num_procs here means we can't touch the IOLoop before now, we must
# let Server handle that. If you need to explicitly handle IOLoops then you
# will need to use the lower level BaseServer class.
server = Server(applications)
server.start()

if __name__ == "__main__":
    print("Opening Bokeh application on http://localhost:5006/")

    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()

import awesome_panel.express.bootstrap
