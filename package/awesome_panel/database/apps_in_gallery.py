"""In this module we define the list of apps contributed to the Gallery

Please note that all contribute apps should

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/
gallery/<app_name_folder>
- include that tags tags.CODE, tags.APP_IN_GALLERY as a minimum
"""
from awesome_panel.database import authors, tags
from awesome_panel.database.settings import GITHUB_BLOB_MASTER_URL
from awesome_panel.shared.models import Resource

GITHUB_GALLERY_URL = GITHUB_BLOB_MASTER_URL + "gallery/"

APPS_IN_GALLERY = [
    Resource(
        name="Bootstrap Dashboard",
        url=GITHUB_GALLERY_URL + "bootstrap_dashboard/main.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Spinners",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_spinners.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
]
