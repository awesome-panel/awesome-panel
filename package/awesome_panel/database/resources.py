"""Simple 'database' of models

Here you maintain the list of awesome resources
"""
from awesome_panel.database import authors, tags
from awesome_panel.database.apps_in_gallery import APPS_IN_GALLERY
# pylint: disable=line-too-long
from awesome_panel.shared.models import Resource

# panel FILE ROOTS

RESOURCES = [
    Resource(
        name="Awesome-panel.org",
        url="https://awesome-panel.org",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
] + APPS_IN_GALLERY

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
