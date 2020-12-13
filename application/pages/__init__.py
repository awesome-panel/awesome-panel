"""Exports the different page components to show in the application"""
from application.pages import panel_component_explorer
from application.pages.about import about
from application.pages.async_tasks import async_tasks
from application.pages.awesome_panel_express_tests import (
    test_bootstrap_alerts,
    test_bootstrap_card,
    test_code,
    test_dataframe,
    test_echarts,
    test_material,
    test_model_viewer,
    test_perspective,
    test_progress_ext,
    test_share_links,
    test_wired,
)
from application.pages.bootstrap_dashboard import bootstrap_dashboard
from application.pages.custom_bokeh_model import custom_bokeh_model
from application.pages.dashboard import dashboard
from application.pages.dataexplorer_loading import dataexplorer_loading
from application.pages.detr import detr
from application.pages.discourse import (
    discourse_1478_dependent_widgets,
    discourse_1533_template_with_map,
)
from application.pages.fast import fast_grid_template_app
from application.pages.fast_gallery import fast_gallery
from application.pages.home import home
from application.pages.image_classifier import image_classifier
from application.pages.issues import issues
from application.pages.js_actions import js_actions
from application.pages.kickstarter_dashboard import kickstarter_dashboard
from application.pages import holoviews_linked_brushing
from application.pages.loading_spinners import loading_spinners
from application.pages import ngl_molecule_viewer
from application.pages.owid_choropleth_map import owid_choropleth_map
from application.pages.pandas_profiling_app import pandas_profiling_app
from application.pages.param_reference_example import param_reference_example
from application.pages.resources import resources
from application.pages.shoelace import shoelace
from application.pages.streaming_plots import streaming_plots
from application.pages.styling import fileinput_area
from application.pages.yahooquery_app import yahooquery_app
