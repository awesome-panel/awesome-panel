"""In this module we define and register all Pages in the application

Please note that all pages in the list

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/
application/gallery
"""
from awesome_panel.application.models import Page

from application import pages

# from application.pages import bootstrap_dashboard, custom_bokeh_model
from application.config import authors, tags
from application.config.settings import GITHUB_BLOB_MASTER_URL, THUMBNAILS_ROOT

GITHUB_PAGE_URL = GITHUB_BLOB_MASTER_URL + "application/pages/"

HOME = Page(
    name="Home",
    source_code_url=GITHUB_PAGE_URL + "home/home.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "home.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.home,
    author=authors.MARC_SKOV_MADSEN,
    url="",
)
ABOUT = Page(
    name="About",
    source_code_url=GITHUB_PAGE_URL + "about/about.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "about.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.about,
    author=authors.MARC_SKOV_MADSEN,
    url="about",
)
ISSUES = Page(
    name="Issues",
    source_code_url=GITHUB_PAGE_URL + "issues/issues.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "issues.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.issues,
    author=authors.MARC_SKOV_MADSEN,
    url="issues",
)
RESOURCES = Page(
    name="Resources",
    source_code_url=GITHUB_PAGE_URL + "resources/resources.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "resources.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.resources,
    author=authors.MARC_SKOV_MADSEN,
    url="resources",
)
# ASYNC_TASKS = Page(
#     name="Async Tasks",
#     source_code_url=GITHUB_PAGE_URL + "async_tasks/async_tasks.py",
#     thumbnail_png_url=THUMBNAILS_ROOT + "async_tasks.png",
#     tags=[
#         tags.CODE,
#         tags.APP_IN_GALLERY,
#     ],
#     component=pages.async_tasks,
#     author=authors.JOCHEM_SMIT,
#     url="async-tasks",
# )
BOOTSTRAP_DASHBOARD = Page(
    name="Bootstrap Dashboard",
    source_code_url=GITHUB_PAGE_URL + "bootstrap_dashboard/main.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "bootstrap_dashboard.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.bootstrap_dashboard,
    author=authors.MARC_SKOV_MADSEN,
    url="bootstrap-dashboard",
)
CUSTOM_BOKEH_MODEL = Page(
    name="Custom Bokeh Model",
    source_code_url=GITHUB_PAGE_URL + "custom_bokeh_model/custom.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "custom_bokeh_model.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.custom_bokeh_model,
    author=authors.MARC_SKOV_MADSEN,
    url="custom-bokeh-model",
)
DASHBOARD = Page(
    name="Classic Dashboard",
    source_code_url=GITHUB_PAGE_URL + "dashboard/dashboard.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "dashboard.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.dashboard,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    url="classic-dashboard",
)
DATA_EXPLORER = Page(
    name="DataExplorer - Loading...",
    source_code_url=GITHUB_PAGE_URL + "dataexplorer_loading/dataexplorer_loading.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "dataexplorer_loading.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.dataexplorer_loading,
    author=authors.MARC_SKOV_MADSEN,
    url="data-explorer-loading",
)
DETR = Page(
    name="DE:TR: Object Detection",
    source_code_url=GITHUB_PAGE_URL + "detr/detr.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "detr.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.detr,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    url="detr",
)
IMAGE_CLASSIFIER = Page(
    name="Image Classifier",
    source_code_url=GITHUB_PAGE_URL + "image_classifier/image_classifier.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "image_classifier.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.image_classifier,
    author=authors.MARC_SKOV_MADSEN,
    url="image-classifier",
)
JS_ACTIONS = Page(
    name="JS Actions",
    source_code_url=GITHUB_PAGE_URL + "js_actions/js_actions.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "js_actions.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.js_actions,
    author=authors.MARC_SKOV_MADSEN,
    url="js-actions",
)
KICKSTARTER_DASHBOARD = Page(
    name="Kickstarter Dashboard",
    source_code_url=GITHUB_PAGE_URL + "kickstarter_dashboard/main.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "kickstarter_dashboard.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.kickstarter_dashboard,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    url="kick-starter-dashboard",
)
OWID_CHOROPLETH_MAP = Page(
    name="Owid Choropleth Map",
    source_code_url=GITHUB_PAGE_URL + "owid_choropleth_map/main.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "owid_choropleth_map.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.owid_choropleth_map,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    url="owid-choropleth",
)
PANDAS_PROFILING = Page(
    name="Pandas Profiling",
    source_code_url=GITHUB_PAGE_URL + "pandas_profiling_app/pandas_profiling_app.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "pandas_profiling_app.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.pandas_profiling_app,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=False,
    url="pandas-profiling",
)
PARAM_REFERENCE_EXAMPLE = Page(
    name="Param Reference Example",
    source_code_url=GITHUB_PAGE_URL + "param_reference_example/param_reference_example.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "param_reference_example.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.param_reference_example,
    author=authors.MARC_SKOV_MADSEN,
    url="param-reference",
)
YAHOO_QUERY = Page(
    name="Yahoo Query",
    source_code_url=GITHUB_PAGE_URL + "yahooquery_app/yahooquery_app.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "yahooquery_app.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.yahooquery_app,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    url="yahoo-query",
)
TEST_BOOTSTRAP_ALERTS = Page(
    name="Test Bootstrap Alerts",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_bootstrap_alerts.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_bootstrap_alerts.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_bootstrap_alerts,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-alert",
)
TEST_BOOTSTRAP_CARD = Page(
    name="Test Bootstrap Card",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_bootstrap_card.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_bootstrap_card.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_bootstrap_card,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    width=False,
    url="ext-card",
)
TEST_CODE = Page(
    name="Test Code",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_code.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_code.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_code,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-code",
)
TEST_DATAFRAME = Page(
    name="Test DataFrame",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_dataframe.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_dataframe.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_dataframe,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-dataframe",
)
TEST_ECHARTS = Page(
    name="Test ECharts",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_echarts.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_echarts.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_echarts,
    author=authors.MARC_SKOV_MADSEN,
    url="echarts",
)
TEST_MATERIAL = Page(
    name="Test Material Components",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_material.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_material_components.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.test_material,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-material",
)
TEST_MODEL_VIEWER = Page(
    name="Test Model Viewer",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_model_viewer.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_model_viewer.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.test_model_viewer,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-model-viewer",
)
TEST_PERSPECTIVE = Page(
    name="Test Perspective Viewer",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_perspective.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_perspective.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
    ],
    component=pages.test_perspective,
    author=authors.MARC_SKOV_MADSEN,
    restrict_max_width=False,
    url="ext-perspective",
)
TEST_PROGRESS_EXTENSION = Page(
    name="Test Progress Extension",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_progress_ext.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_progress_ext.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_progress_ext,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-progress",
)
TEST_SHARE_LINKS = Page(
    name="Test Social Links",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_share_links.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_share_links.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_share_links,
    author=authors.MARC_SKOV_MADSEN,
    url="ext-social-links",
)
TEST_WIRED = Page(
    name="Test Wired",
    source_code_url=GITHUB_PAGE_URL + "awesome_panel_express_tests/test_wired.py",
    thumbnail_png_url=THUMBNAILS_ROOT + "test_wired.png",
    tags=[
        tags.CODE,
        tags.APP_IN_GALLERY,
        tags.AWESOMEPANEL_EXPRESS,
    ],
    component=pages.test_wired,
    author=authors.MARC_SKOV_MADSEN,
    show_loading_page=True,
    url="ext-wired",
)

PAGES = [
    HOME,
    RESOURCES,
    ABOUT,
    BOOTSTRAP_DASHBOARD,
    CUSTOM_BOKEH_MODEL,
    DASHBOARD,
    DATA_EXPLORER,
    DETR,
    IMAGE_CLASSIFIER,
    JS_ACTIONS,
    KICKSTARTER_DASHBOARD,
    OWID_CHOROPLETH_MAP,
    PANDAS_PROFILING,
    PARAM_REFERENCE_EXAMPLE,
    YAHOO_QUERY,
    TEST_BOOTSTRAP_ALERTS,
    TEST_BOOTSTRAP_CARD,
    TEST_CODE,
    TEST_DATAFRAME,
    TEST_ECHARTS,
    TEST_MATERIAL,
    TEST_MODEL_VIEWER,
    TEST_PERSPECTIVE,
    TEST_PROGRESS_EXTENSION,
    TEST_SHARE_LINKS,
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

URLS = {page.url: getattr(page.component, "view") for page in NON_GALLERY_PAGES + GALLERY_PAGES}
