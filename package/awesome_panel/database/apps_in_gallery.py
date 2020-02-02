"""In this module we define all apps in the gallery as Resources and expose them via the
**APPS_IN_GALLERY** list.

Please note that all apps in the list

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/gallery/
- include the tags *tags.CODE* and *tags.APP_IN_GALLERY* as a minimum
"""
from awesome_panel.database import (
    authors,
    tags,
)
from awesome_panel.database.settings import (
    GITHUB_BLOB_MASTER_URL,
    THUMBNAILS_ROOT,
)
from awesome_panel.shared.models import Resource

GITHUB_GALLERY_URL = GITHUB_BLOB_MASTER_URL + "src/pages/gallery/"

# Please keep this list sorted by name
APPS_IN_GALLERY = [
    Resource(
        name="Bootstrap Dashboard",
        url=GITHUB_GALLERY_URL + "bootstrap_dashboard/main.py",
        thumbnail_path=THUMBNAILS_ROOT + "bootstrap_dashboard.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Custom Bokeh Model",
        url=GITHUB_GALLERY_URL + "custom_bokeh_model/custom.py",
        thumbnail_path=THUMBNAILS_ROOT + "custom_bokeh_model.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Image Classifier",
        url=GITHUB_GALLERY_URL + "image_classifier/image_classifier.py",
        thumbnail_path=THUMBNAILS_ROOT + "image_classifier.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Owid Choropleth Map",
        url=GITHUB_GALLERY_URL + "owid_choropleth_map/main.py",
        thumbnail_path=THUMBNAILS_ROOT + "owid_choropleth_map.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Kickstarter Dashboard",
        url=GITHUB_GALLERY_URL + "kickstarter_dashboard/main.py",
        thumbnail_path=THUMBNAILS_ROOT + "kickstarter_dashboard.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Param Reference Example",
        url=GITHUB_GALLERY_URL + "param_reference_example/param_reference_example.py",
        thumbnail_path=THUMBNAILS_ROOT + "param_reference_example.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Yahoo Query",
        url=GITHUB_GALLERY_URL + "yahooquery_app/yahooquery_app.py",
        thumbnail_path=THUMBNAILS_ROOT + "yahooquery_app.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Bootstrap Alerts",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_bootstrap_alerts.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_bootstrap_alerts.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Bootstrap Card",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_bootstrap_card.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_bootstrap_card.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Code",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_code.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_code.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test DataFrame",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_dataframe.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_dataframe.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Divider",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_divider.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_divider.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test FontAwesome",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_fontawesome.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_fontawesome.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Headings",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_headings.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_headings.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Markdown",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_markdown.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_markdown.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Modal",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_modal.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_modal.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Progress Extension",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_progress_ext.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_progress_ext.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Share Links",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_share_links.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_share_links.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Spinners",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_spinners.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_spinners.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
]
