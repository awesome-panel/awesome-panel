"""In this module we define all apps in the gallery as Pages and expose them via the
**APPS_IN_GALLERY** list.

Please note that all apps in the list

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/gallery/
- include the tags *tags.CODE* and *tags.APP_IN_GALLERY* as a minimum
"""
from src.config.settings import GITHUB_BLOB_MASTER_URL, THUMBNAILS_ROOT
from awesome_panel.models import Page
from src.pages import gallery
from src import pages
# from src.pages.gallery import bootstrap_dashboard, custom_bokeh_model
from src.config import authors, tags
from awesome_panel.services import PAGE_SERVICE

GITHUB_GALLERY_URL = GITHUB_BLOB_MASTER_URL + "src/pages/gallery/"

# Please keep this list sorted by name
PAGE_SERVICE.bulk_create(
    [
        Page(
            name="Bootstrap Dashboard",
            source_code_url=GITHUB_GALLERY_URL + "bootstrap_dashboard/main.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "bootstrap_dashboard.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.bootstrap_dashboard,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Custom Bokeh Model",
            source_code_url=GITHUB_GALLERY_URL + "custom_bokeh_model/custom.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "custom_bokeh_model.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.custom_bokeh_model,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="DataExplorer - Loading...",
            source_code_url=GITHUB_GALLERY_URL + "dataexplorer_loading/dataexplorer_loading.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "dataexplorer_loading.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.DataExplorer,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Image Classifier",
            source_code_url=GITHUB_GALLERY_URL + "image_classifier/image_classifier.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "image_classifier.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.image_classifier,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Kickstarter Dashboard",
            source_code_url=GITHUB_GALLERY_URL + "kickstarter_dashboard/main.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "kickstarter_dashboard.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.kickstarter_dashboard,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Owid Choropleth Map",
            source_code_url=GITHUB_GALLERY_URL + "owid_choropleth_map/main.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "owid_choropleth_map.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.owid_choropleth_map,
            author=authors.MARC_SKOV_MADSEN,
        ),

        Page(
            name="Param Reference Example",
            source_code_url=GITHUB_GALLERY_URL + "param_reference_example/param_reference_example.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "param_reference_example.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.param_reference_example,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Yahoo Query",
            source_code_url=GITHUB_GALLERY_URL + "yahooquery_app/yahooquery_app.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "yahooquery_app.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY,],
            component=pages.yahooquery_app,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Bootstrap Alerts",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_bootstrap_alerts.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_bootstrap_alerts.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_bootstrap_alerts,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Bootstrap Card",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_bootstrap_card.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_bootstrap_card.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_bootstrap_card,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Code",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_code.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_code.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_code,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test DataFrame",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_dataframe.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_dataframe.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_dataframe,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Divider",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_divider.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_divider.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_divider,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test FontAwesome",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_fontawesome.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_fontawesome.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_fontawesome,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Headings",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_headings.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_headings.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_headings,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Markdown",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_markdown.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_markdown.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_markdown,
            author=authors.MARC_SKOV_MADSEN,
        ),
        # Page(
        #     name="Test Modal",
        #     source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_modal.py",
        #     thumbnail_png_url=THUMBNAILS_ROOT + "test_modal.png",
        #     tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
        #     component=pages.test_modal,
        #     author=authors.MARC_SKOV_MADSEN,
        # ),
        Page(
            name="Test Progress Extension",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_progress_ext.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_progress_ext.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_progress_ext,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Share Links",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_share_links.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_share_links.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_share_links,
            author=authors.MARC_SKOV_MADSEN,
        ),
        Page(
            name="Test Spinners",
            source_code_url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_spinners.py",
            thumbnail_png_url=THUMBNAILS_ROOT + "test_spinners.png",
            tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
            component=pages.test_spinners,
            author=authors.MARC_SKOV_MADSEN,
        ),
    ]
)