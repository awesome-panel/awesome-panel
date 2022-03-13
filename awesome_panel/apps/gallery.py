"""Gallery Page showing all the apps available."""
from awesome_panel_extensions.site.gallery import GalleryTemplate

from awesome_panel import config

if __name__.startswith("bokeh"):
    config.extension(url="gallery", template=None)

    GalleryTemplate(
        site="Awesome Panel",
        title="Gallery",
        description="""The purpose of the Awesome Panel Gallery is to inspire
and help you create awesome analytics apps in
<fast-anchor href="https://panel.holoviz.org" target="_blank"
 appearance="hypertext">Panel</fast-anchor> using the tools you know and
 love.""",
        applications=config.APPLICATIONS,
        target="_self",
        theme="dark",
        meta_name="Awesome Panel Gallery",
        meta_description="Gallery of applications at awesome-panel.org",
        meta_keywords=(
            "Awesome, HoloViz, Panel, Gallery, Apps, Science, Data Engineering, Data Science, "
            "Machine Learning, Python"
        ),
        meta_author="Marc Skov Madsen",
    ).servable()
