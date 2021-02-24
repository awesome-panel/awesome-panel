"""Provides the Gallery app"""
from src.shared import config
from src.shared.templates import GalleryTemplate


def view():
    """Returns the GalleryTemplate to be served in the Site"""
    return GalleryTemplate(resources=list(config.applications.values()))


if __name__.startswith("bokeh"):
    # Run the development server
    # python -m panel serve 'src/apps/gallery.py' --dev --show
    view().servable()
if __name__ == "__main__":
    # Run the server. Useful for integrated debugging in your Editor or IDE.
    # python 'src/apps/gallery.py'
    view().show(port=5007)
