"""The Awesome Panel Gallery based on the Fast Components"""
# pylint: disable=line-too-long
import panel as pn
from awesome_panel_extensions.site import site
from awesome_panel_extensions.site.gallery import GalleryTemplate

APPLICATION = site.create_application(
    url="gallery",
    name="App Gallery",
    author="Marc Skov Madsen",
    description="""A custom Panel template using the Fast web components""",
    description_long="""The Gallery provides a very visual overview to the applications and associated
    resources""",
    thumbnail="gallery.png",
    resources={
        "code": "gallery/gallery.py",
    },
)


@site.add(APPLICATION)
def view():
    """Return a GalleryTemplate"""
    pn.config.raw_css = [
        css for css in pn.config.raw_css if not css.startswith("/* CUSTOM TEMPLATE CSS */")
    ]
    return GalleryTemplate(
        site="Awesome Panel",
        title="Gallery",
        description="""The purpose of the Awesome Panel Gallery is to inspire and help you create awesome analytics apps in <fast-anchor href="https://panel.holoviz.org" target="_blank" appearance="hypertext">Panel</fast-anchor> using the tools you know and love.""",
        applications=site.applications,
        target="_self",
        theme="dark",
        meta_name="Awesome Panel Gallery",
        meta_description="Gallery of applications at awesome-panel.org",
        meta_keywords=(
            "Awesome, HoloViz, Panel, Gallery, Apps, Science, Data Engineering, Data Science, "
            "Machine Learning, Python"
        ),
        meta_author="Marc Skov Madsen",
    )


if __name__.startswith("bokeh"):
    view().servable()
