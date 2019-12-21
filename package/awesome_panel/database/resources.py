"""Simple 'database' of models

Here you maintain the list of awesome resources
"""
from awesome_panel.database import authors, tags
from awesome_panel.database.apps_in_gallery import APPS_IN_GALLERY
from awesome_panel.database.settings import THUMBNAILS_ROOT

# pylint: disable=line-too-long
from awesome_panel.shared.models import Resource

# panel FILE ROOTS

RESOURCES = [
    Resource(
        name="Awesome-panel.org",
        url="https://awesome-panel.org",
        thumbnail_path=THUMBNAILS_ROOT + "awesome-panel-org.png?raw=true",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Turn any notebook into a deployable dashboard|PyData Berlin 2019",
        url="https://www.youtube.com/watch?v=Ohr29FJjBi0&list=PLGVZCDnMOq0pNHTYo3i56zYU-Tdw5Uguw",
        thumbnail_path=THUMBNAILS_ROOT + "pydataberlin2019.png?raw=true",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.PHILIPP_RUDIGER,
    ),
] + APPS_IN_GALLERY

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
