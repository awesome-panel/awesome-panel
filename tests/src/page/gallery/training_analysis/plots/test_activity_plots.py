"""Test of the activity_plot module"""
# pylint: disable=redefined-outer-name,protected-access
import pandas as pd

from src.pages.gallery.training_analysis.plots import activity_plot


def test_activity_data_plots_none():
    """The plot_layout function can handle None as input"""
    assert activity_plot.activity_plots(None) is None


def test_activity_data_plots_empty():
    """The plot_layout function can handle an empty DataFrame as input"""
    assert activity_plot.activity_plots(pd.DataFrame()) is None


def test_map_plot_none():
    """The plot_map function can handle None as input"""
    assert activity_plot.map_plot(None) is None


def test_map_plot_empty():
    """The plot_map function can handle an empty DataFrame as input"""
    assert activity_plot.map_plot(pd.DataFrame()) is None
