"""In this module we define and register all Pages in the application

Please note that all pages in the list

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/
application/gallery
"""
from application import pages

# from application.pages import bootstrap_dashboard, custom_bokeh_model
from application.config import authors, tags
from application.config.settings import GITHUB_BLOB_MASTER_URL, THUMBNAILS_ROOT
from awesome_panel.application.models import Page

GITHUB_PAGE_URL = GITHUB_BLOB_MASTER_URL + "application/pages/"

HOME = Page(
    name="Home",
    source_code_url=GITHUB_PAGE_URL + "home/home.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "home.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.home,
    author=authors.MARC_SKOV_MADSEN,
)
ABOUT = Page(
    name="About",
    source_code_url=GITHUB_PAGE_URL + "about/about.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "about.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.about,
    author=authors.MARC_SKOV_MADSEN,
)
ISSUES = Page(
    name="Issues",
    source_code_url=GITHUB_PAGE_URL + "issues/issues.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "issues.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.issues,
    author=authors.MARC_SKOV_MADSEN,
)
RESOURCES = Page(
    name="Resources",
    source_code_url=GITHUB_PAGE_URL + "resources/resources.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "resources.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.resources,
    author=authors.MARC_SKOV_MADSEN,
)
ASYNC_TASKS = Page(
    name="Async Tasks",
    source_code_url=GITHUB_PAGE_URL + "async_tasks/async_tasks.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "async_tasks.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.async_tasks,
    author=authors.JOCHEM_SMIT,
)
BOOTSTRAP_DASHBOARD = Page(
    name="Bootstrap Dashboard",
    source_code_url=GITHUB_PAGE_URL + "bootstrap_dashboard/main.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "bootstrap_dashboard.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.bootstrap_dashboard,
    author=authors.MARC_SKOV_MADSEN,
)
CUSTOM_BOKEH_MODEL = Page(
    name="Custom Bokeh Model",
    source_code_url=GITHUB_PAGE_URL + "custom_bokeh_model/custom.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "custom_bokeh_model.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.custom_bokeh_model,
    author=authors.MARC_SKOV_MADSEN,
)
DATA_EXPLORER = Page(
    name="DataExplorer - Loading...",
    source_code_url=GITHUB_PAGE_URL + "dataexplorer_loading/dataexplorer_loading.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "dataexplorer_loading.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.DataExplorer,
    author=authors.MARC_SKOV_MADSEN,
)
DETR = Page(
    name="DE:TR: Object Detection",
    source_code_url=GITHUB_PAGE_URL + "detr/detr.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "detr.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.detr,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
)
IMAGE_CLASSIFIER = Page(
    name="Image Classifier",
    source_code_url=GITHUB_PAGE_URL + "image_classifier/image_classifier.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "image_classifier.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.image_classifier,
    author=authors.MARC_SKOV_MADSEN,
)
KICKSTARTER_DASHBOARD = Page(
    name="Kickstarter Dashboard",
    source_code_url=GITHUB_PAGE_URL + "kickstarter_dashboard/main.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "kickstarter_dashboard.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.kickstarter_dashboard,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
)
OWID_CHOROPLETH_MAP = Page(
    name="Owid Choropleth Map",
    source_code_url=GITHUB_PAGE_URL + "owid_choropleth_map/main.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "owid_choropleth_map.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.owid_choropleth_map,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
)
PANDAS_PROFILING = Page(
    name="Pandas Profiling",
    source_code_url=GITHUB_PAGE_URL + "pandas_profiling_app/pandas_profiling_app.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "pandas_profiling_app.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.pandas_profiling_app,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=False,
)
PARAM_REFERENCE_EXAMPLE = Page(
    name="Param Reference Example",
    source_code_url=GITHUB_PAGE_URL + "param_reference_example/param_reference_example.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "param_reference_example.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.param_reference_example,
    author=authors.MARC_SKOV_MADSEN,
)
YAHOO_QUERY = Page(
    name="Yahoo Query",
    source_code_url=GITHUB_PAGE_URL + "yahooquery_app/yahooquery_app.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "yahooquery_app.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.yahooquery_app,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
)
TEST_BOOTSTRAP_ALERTS = Page(
    name="Test Bootstrap Alerts",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_bootstrap_alerts.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_bootstrap_alerts.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_bootstrap_alerts,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_BOOTSTRAP_CARD = Page(
    name="Test Bootstrap Card",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_bootstrap_card.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_bootstrap_card.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_bootstrap_card,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    restrict_max_width=False,
)
TEST_CODE = Page(
    name="Test Code",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_code.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_code.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_code,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_DATAFRAME = Page(
    name="Test DataFrame",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_dataframe.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_dataframe.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_dataframe,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_ECHARTS = Page(
    name="Test ECharts",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_echarts.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_echarts.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_echarts,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_DIVIDER = Page(
    name="Test Divider",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_divider.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_divider.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_divider,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_FONT_AWESOME = Page(
    name="Test FontAwesome",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_fontawesome.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_fontawesome.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_fontawesome,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_HEADINGS = Page(
    name="Test Headings",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_headings.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_headings.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_headings,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_MARKDOWN = Page(
    name="Test Markdown",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_markdown.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_markdown.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_markdown,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_MATERIAL = Page(
    name="Test Material Components",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_material.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_material_components.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.test_material,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_MODEL_VIEWER = Page(
    name="Test Model Viewer",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_model_viewer.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_model_viewer.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.test_model_viewer,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_PERSPECTIVE = Page(
    name="Test Perspective Viewer",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_perspective.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_perspective.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY,],
    component=pages.test_perspective,
    author=authors.MARC_SKOV_MADSEN,
    restrict_max_width=False,
)
TEST_PROGRESS_EXTENSION = Page(
    name="Test Progress Extension",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_progress_ext.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_progress_ext.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_progress_ext,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_SHARE_LINKS = Page(
    name="Test Share Links",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_share_links.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_share_links.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_share_links,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_SPINNERS = Page(
    name="Test Spinners",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_spinners.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_spinners.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_spinners,
    author=authors.MARC_SKOV_MADSEN,
)
TEST_WIRED = Page(
    name="Test Wired",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_wired.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_wired.png",
    tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS,],
    component=pages.test_wired,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
)

PAGES = [
    HOME,
    RESOURCES,
    ABOUT,
    ASYNC_TASKS,
    BOOTSTRAP_DASHBOARD,
    CUSTOM_BOKEH_MODEL,
    DATA_EXPLORER,
    DETR,
    IMAGE_CLASSIFIER,
    KICKSTARTER_DASHBOARD,
    OWID_CHOROPLETH_MAP,
    PANDAS_PROFILING,
    PARAM_REFERENCE_EXAMPLE,
    YAHOO_QUERY,
    TEST_BOOTSTRAP_ALERTS,
    TEST_BOOTSTRAP_CARD,
    TEST_CODE,
    TEST_DATAFRAME,
    TEST_DIVIDER,
    TEST_ECHARTS,
    TEST_FONT_AWESOME,
    TEST_HEADINGS,
    TEST_MARKDOWN,
    TEST_MATERIAL,
    TEST_MODEL_VIEWER,
    TEST_PERSPECTIVE,
    TEST_PROGRESS_EXTENSION,
    TEST_SHARE_LINKS,
    TEST_SPINNERS,
    TEST_WIRED,
    ISSUES,
]

NON_GALLERY_PAGES = [
    HOME,
    ABOUT,
    ISSUES,
    RESOURCES,
]

GALLERY_PAGES = [page for page in PAGES if page not in NON_GALLERY_PAGES]
