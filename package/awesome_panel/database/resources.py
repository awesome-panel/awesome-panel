"""In this module we define all Resources (except apps in the gallery) and exposes
them via the RESOURCES list.
"""
from awesome_panel.database import (
    authors,
    tags,
)
from awesome_panel.database.apps_in_gallery import APPS_IN_GALLERY
from awesome_panel.database.settings import THUMBNAILS_ROOT

# pylint: disable=line-too-long
from awesome_panel.shared.models import Resource

# panel FILE ROOTS

RESOURCES = [
    Resource(
        name="XrViz",
        url="https://github.com/intake/xrviz",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP, tags.CODE, tags.INSPIRATION,],
        author=authors.INTAKE,
    ),
    Resource(
        name="Information is Beautiful",
        url=(
            "https://towardsdatascience.com/how-to-build-a-time-series-dashboard-in-python-with-"
            "panel-altair-and-a-jupyter-notebook-c0ed40f02289"
        ),
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL, tags.ARTICLE,],
        author=authors.BENJAMIN_COOLEY,
    ),
    Resource(
        name="Information is Beautiful",
        url="https://informationisbeautiful.net/",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.INSPIRATION],
        author=authors.INFORMATIONISBEUTIFULL,
    ),
    Resource(
        name="Open Source Directions ep. 29: Panel",
        url="https://www.youtube.com/watch?v=hZOsxmM_wyg",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO],
        author=authors.QUANSIGHT,
    ),
    Resource(
        name="Our World in Data",
        url="https://ourworldindata.org/",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.INSPIRATION],
        author=authors.OURWORLDINDATA,
    ),
    Resource(
        name="Panel",
        url="https://panel.pyviz.org/",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Discourse",
        url="https://discourse.holoviz.org/c/panel",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Getting Started",
        url="https://panel.pyviz.org/getting_started/index.html",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="User Guide",
        url="https://panel.pyviz.org/user_guide/index.html",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Gallery",
        url="https://panel.pyviz.org/gallery/index.html",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Reference Gallery",
        url="https://panel.pyviz.org/reference/index.html",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="GitHub",
        url="https://github.com/holoviz/panel",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Announcing Article",
        url="https://medium.com/@philipp.jfr/panel-announcement-2107c2b15f52",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Awesome-panel.org",
        url="https://awesome-panel.org",
        thumbnail_path=THUMBNAILS_ROOT + "awesome-panel-org.png?raw=true",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Github",
        url="https://github.com/marcskovmadsen/awesome-panel",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docs",
        url="https://awesome-panel.readthedocs.io/en/latest/",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docker",
        url="https://hub.docker.com/r/marcskovmadsen/awesome-panel",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="PyPi",
        url="https://pypi.org/project/awesome-panel/",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Dashboards with PyViz Panel for interactive web apps",
        url="https://dmnfarrell.github.io/bioinformatics/pyviz-panel",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ARTICLE],
        author=authors.DAMIAN_FARRELL,
    ),
    Resource(
        name="Turn any Notebook into a Deployable Dashboard | SciPy 2019 | James Bednar",
        url="https://www.youtube.com/watch?v=L91rd1D6XTA&t=274s",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO, tags.TUTORIAL,],
        author=authors.JAMES_BEDNAR,
    ),
    Resource(
        name="Turn any notebook into a deployable dashboard|PyData Berlin 2019",
        url="https://www.youtube.com/watch?v=Ohr29FJjBi0&list=PLGVZCDnMOq0pNHTYo3i56zYU-Tdw5Uguw",
        thumbnail_path=THUMBNAILS_ROOT + "pydataberlin2019.png?raw=true",
        is_awesome=True,
        tags=[tags.VIDEO, tags.TUTORIAL,],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Visualize any Data Easily, from Notebooks to Dashboards",
        url="https://www.youtube.com/watch?v=7deGS4IPAQ0&t=1326s",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO, tags.TUTORIAL,],
        author=authors.JAMES_BEDNAR,
    ),
    Resource(
        name="HoloViz.org - Awesome Resources and Tutorials",
        url="http://holoviz.org/index.html",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL],
        author=authors.HOLOVIZ,
    ),
    Resource(
        name="awesome-streamlit.org",
        url="https://awesome-streamlit.org",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.SISTER_SITES],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Bokeh",
        url="https://bokeh.pydata.org/en/latest/index.html",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.BOKEH,
    ),
    Resource(
        name="Jupyter Voila",
        url="https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.VOILA,
    ),
    Resource(
        name="Plotly Dash",
        url="https://plot.ly/dash/",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.PLOTLY,
    ),
    Resource(
        name="Streamlit",
        url="https://streamlit.io",
        thumbnail_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.STREAMLIT,
    ),
] + APPS_IN_GALLERY

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
