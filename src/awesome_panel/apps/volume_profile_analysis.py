"""This example app demonstrates how to use Panel and the HoloViews ecosystem to
analyze Volume Profiles as described in the [How to Analyze Volume Profiles With Python Blog Post]\
(https://medium.com/swlh/how-to-analyze-volume-profiles-with-python-3166bb10ff24)
by [Minh Ngyen](https://www.linkedin.com/in/minhnguyen001/)
"""
import pathlib
from datetime import timedelta

import holoviews as hv
import numpy as np
import pandas as pd
import panel as pn
import param
import yfinance as yf
from bokeh.models import HoverTool
from bokeh.models.formatters import NumeralTickFormatter
from diskcache import FanoutCache
from panel.io.loading import start_loading_spinner, stop_loading_spinner
from scipy import signal, stats

from awesome_panel import config

hv.extension("bokeh")


cache = FanoutCache(".cache")

ROOT = pathlib.Path(__file__).parent
DATA_PATH = ROOT / "bs_btcusd_ohlcv_1h_2020.csv.gz"
DATA_URL = (
    "https://cdn.shopify.com/s/files/1/1365/1139/files/bs_btcusd_ohlcv_1h_2020.csv.gz?v=1585597359"
)
ACCENT_COLOR = "#C01754"
# Source: https://mycolor.space/?hex=%23C01754&sub=1
COLOR_PALETTE = [ACCENT_COLOR, "#007813", "#0061E5"]
GENERIC_GRADIENT_PALETTE = [ACCENT_COLOR, "#A22E74", "#784184", "#4E4A81", "#314C70", "#2F4858"]
RED = "#c01754"
GREEN = "#007400"
GRAY = "#b0ab99"

CACHE_EXPIRY = 60 * 60 * 24  # seconds, i.e. one Day

# region DATA


@cache.memoize(name="shared", expire=CACHE_EXPIRY)
def _extract_raw_data(ticker="ORSTED.CO", period="6mo", interval="1d"):
    extractor = yf.Ticker(ticker)
    return extractor.history(period=period, interval=interval).reset_index()


def _transform_data(raw_data: pd.DataFrame):
    data = (
        raw_data[["Date", "Open", "High", "Low", "Close", "Volume"]]
        .copy(deep=True)
        .rename(
            columns={
                "Date": "time",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            }
        )
    )
    return data


# endregion DATA

# region UTILS


def set_toolbar_none(plot, _):
    """Removes the bokeh toolbar"""
    bokeh_plot = plot.state
    bokeh_plot.toolbar.logo = None
    bokeh_plot.toolbar_location = None


# endregion UTILS

# region CANDLESTICK


def create_candle_stick(data: pd.DataFrame) -> hv.Layout:
    """Creates a candle stick plot

    Args:
        data (pd.DataFrame): A dataframe with columns time, open, high, low, close and volume

    Returns:
        hv.Layout: A candle stick plot
    """

    data = data.copy(deep=True)
    t_delta = timedelta(hours=1)
    data["time_start"] = data.time - 9 * t_delta  # rectangles start
    data["time_end"] = data.time + 9 * t_delta  # rectangles end
    data["positive"] = ((data.close - data.open) > 0).astype(int)
    tooltips = [
        ("Time", "@{time}{%F}"),
        ("Open", "@open"),
        ("High", "@high"),
        ("Low", "@{price}"),
        ("Close", "@close"),
        ("Volume", "@volume{0,0}"),
    ]
    hover = HoverTool(tooltips=tooltips, formatters={"@{time}": "datetime"})
    candlestick = hv.Segments(data, kdims=["time", "low", "time", "high"]) * hv.Rectangles(
        data,
        kdims=["time_start", "open", "time_end", "close"],
        vdims=["positive", "high", "low", "time", "volume"],
    )
    candlestick = candlestick.redim(low="price")
    candlestick.opts(
        hv.opts.Rectangles(  # pylint: disable=no-member
            color="positive",
            cmap=[RED, GREEN],
            responsive=True,
            tools=["box_zoom", "pan", "wheel_zoom", "save", "reset", hover],
            default_tools=[],
            active_tools=["box_zoom"],
        ),
        hv.opts.Segments(  # pylint: disable=no-member
            color=GRAY,
            height=400,
            responsive=True,
            tools=["box_zoom", "pan", "reset"],
            default_tools=[],
            active_tools=["box_zoom"],
        ),
    )
    return candlestick


def _create_time_and_volume_histogram(data, time="time", volume="volume", color=GRAY, alpha=0.5):
    formatter = NumeralTickFormatter(format="0,0")
    hist_data = zip(data[time], data[volume])
    tooltips = [
        ("Time", "@{time}{%F}"),
        ("Volume", "@volume{0,0}"),
    ]
    hover = HoverTool(tooltips=tooltips, formatters={"@{time}": "datetime"})
    return (
        hv.Histogram(hist_data)
        .redim(Frequency="volume", x="time")
        .opts(
            yformatter=formatter,
            color=color,
            alpha=alpha,
            tools=["xbox_zoom", "reset", hover],
            default_tools=[],
            hooks=[set_toolbar_none],
            yticks=4,
        )
    )


def _create_price_and_volume_histogram(  # pylint: disable=too-many-arguments
    data, price="close", volume="volume", bins=150, color=GRAY, alpha=0.5
):
    formatter = NumeralTickFormatter(format="0,0")
    hist = np.histogram(data[price], bins=bins, weights=data[volume])
    hist_data = zip(hist[1], hist[0])
    tooltips = [
        ("Price", "@{price}"),
        ("Volume", "@volume{0,0}"),
    ]
    hover = HoverTool(tooltips=tooltips)
    return (
        hv.Histogram(hist_data)
        .redim(Frequency="volume", x="price")
        .opts(
            xformatter=formatter,
            color=color,
            alpha=alpha,
            tools=["ybox_zoom", "reset", hover],
            default_tools=[],
            invert_axes=True,
            hooks=[set_toolbar_none],
            xticks=2,
        )
    )


def create_candle_stick_with_histograms(data: pd.DataFrame) -> pn.GridSpec:
    """Returns a candle stick plot with volume distributions on the sides

    Args:
        data (pd.DataFrame): A dataframe with columns time, open, high, low, close and volume

    Returns:
        pn.GridSpec: A GridSpec containing the plots
    """
    gridspec = pn.GridSpec(sizing_mode="stretch_both", min_height=600, margin=0)
    if not data is None:
        volume_plot = _create_time_and_volume_histogram(data).opts(responsive=True)
        candle_stick_plot = create_candle_stick(data).opts(responsive=True)
        pav_plot = _create_price_and_volume_histogram(data).opts(responsive=True)
        gridspec[0:2, 0:8] = volume_plot
        gridspec[2:10, 0:8] = candle_stick_plot
        gridspec[2:10, 8:10] = pav_plot
    return gridspec


# endregion CANDLESTICK


# region SIGNAL ANALYSIS


def _calculate_vol_distribution_analysis(  # pylint: disable=too-many-arguments
    data, price="close", volume="volume", bins=150
):
    hist = np.histogram(data[price], bins=bins, weights=data[volume], density=True)
    return list(zip(hist[1], hist[0]))


def _create_normalized_price_and_volume_histogram(hist_data, color=ACCENT_COLOR, alpha=0.5):
    formatter = NumeralTickFormatter(format="0,0")
    tooltips = [
        ("Price", "@{Price}{0,0.000}"),
        ("Volume Density", "@{VolumeDensity}{0,0.000}"),
    ]
    hover = HoverTool(tooltips=tooltips)
    return (
        hv.Histogram(hist_data)
        .redim(Frequency="VolumeDensity", x="Price")
        .opts(
            xformatter=formatter,
            color=color,
            alpha=alpha,
            tools=["xbox_zoom", "reset", hover, "save"],
            default_tools=[],
            ylabel="Volume Density",
            # invert_axes=True,
            # hooks=[set_toolbar_none],
            # xticks=2,
        )
    )


def _kde_analysis(
    data,
    price="close",
    volume="volume",
    kde_factor=0.05,
    num_samples=500,
):
    kde = stats.gaussian_kde(data[price], weights=data[volume], bw_method=kde_factor)
    xrange = np.linspace(data[price].min(), data[price].max(), num_samples)
    ticks_per_sample = (xrange.max() - xrange.min()) / num_samples
    kdy = kde(xrange)
    return kde, xrange, ticks_per_sample, kdy


def _signal_analysis(xrange, kdy, min_prom_factor=0.3):
    width_range = 1
    min_prom = kdy.max() * min_prom_factor * 0.3
    peaks, peak_props = signal.find_peaks(kdy, prominence=min_prom, width=width_range)
    pkx = xrange[peaks]
    pky = kdy[peaks]
    return peaks, pkx, pky, peak_props


def _create_kde(
    xrange,
    kdy,
    color=ACCENT_COLOR,
):
    tooltips = [
        ("Price", "@{Price}{0,0.000}"),
        ("Volume Density", "@{VolumeDensity}{0,0.000}"),
    ]
    hover = HoverTool(tooltips=tooltips)
    # ticks_per_sample = (xr.max() - xr.min()) / num_samples
    return (
        hv.Curve(data={"x": xrange, "y": kdy})
        .opts(color=color, tools=[hover], default_tools=[], ylabel="Volume Density")
        .redim(y="VolumeDensity", x="Price")
    )


def _create_kde_peaks(
    pkx,
    pky,
    color=GREEN,
):
    return (
        hv.Scatter(data={"x": pkx, "y": pky})
        .opts(color=color, size=8, default_tools=[])
        .redim(y="Volume Density", x="Price")
    )


def _create_promince_plot(pkx, pky, peak_props, color=GREEN):
    line_x = pkx
    line_y0 = pky
    line_y1 = pky - peak_props["prominences"]
    lines = []
    for xxx, yy0, yy1 in zip(line_x, line_y0, line_y1):
        data = {
            "x": [xxx, xxx],
            "y": [yy0, yy1],
        }
        plot = hv.Curve(data).opts(color=color, line_width=4, default_tools=[])
        lines.append(plot)
    return hv.Overlay(lines)


def _create_width_plot(xrange, ticks_per_sample, peak_props, color=GREEN):
    left_ips = peak_props["left_ips"]
    right_ips = peak_props["right_ips"]
    width_x0 = xrange.min() + (left_ips * ticks_per_sample)
    width_x1 = xrange.min() + (right_ips * ticks_per_sample)
    width_y = peak_props["width_heights"]
    lines = []
    for xx0, xx1, yyy in zip(width_x0, width_x1, width_y):
        data = {
            "x": [xx0, xx1],
            "y": [yyy, yyy],
        }
        plot = hv.Curve(data).opts(color=color, line_width=4, default_tools=[])
        lines.append(plot)
    return hv.Overlay(lines)


def _create_signal_analysis_plot(  # pylint: disable=too-many-arguments
    hist_data,
    xrange,
    ticks_per_sample,
    kdy,
    pkx,
    pky,
    peak_props,
    add_peak_and_prominence=True,
):
    plots = [
        _create_normalized_price_and_volume_histogram(hist_data).opts(responsive=True),
        _create_kde(xrange, kdy).opts(responsive=True),
        _create_kde_peaks(pkx, pky).opts(responsive=True),
    ]
    if add_peak_and_prominence:
        plots.append(_create_promince_plot(pkx, pky, peak_props).opts(responsive=True))
        plots.append(_create_width_plot(xrange, ticks_per_sample, peak_props).opts(responsive=True))
    return hv.Overlay(plots)


# endregion SIGNAL ANALYSIS

# endregion DISTRIBUTION

# region SECTIONS


class BaseSection(param.Parameterized):
    """Abstract Class for Section of App"""

    data = param.DataFrame()
    loading = param.Boolean(default=False)
    view = param.ClassSelector(class_=pn.Column)

    def __init__(self, **params):
        super().__init__(**params)

        self._init_view()
        self._update_view()
        self.param.watch(self._update_view, "data")

    def _init_view(self):
        raise NotImplementedError()

    def _update_view(self, *events):
        raise NotImplementedError()

    @pn.depends("loading", watch=True)
    def _update_loading(self):
        if self.loading:
            start_loading_spinner(self.view)
        else:
            stop_loading_spinner(self.view)


class LoadDataSection(BaseSection):
    """Section describing the loading of data"""

    ticker = param.ObjectSelector("ORSTED.CO", objects=["MSFT", "ORSTED.CO"])
    period = param.Integer(default=6, bounds=(1, 12), step=1, label="Period (months)")
    interval = param.ObjectSelector(default="1d", objects=["1d"], label="Interval", constant=True)

    def _init_view(self):
        info_head = """We can use the [`yfinance`](https://pypi.org/project/yfinance/) package to
load the data and [DiskCache](http://www.grantjenks.com/docs/diskcache/tutorial.html) to cache the
data for one day."""
        if self.data is None:
            self._load_data()

        self._dataframe_panel = pn.pane.DataFrame(
            self.data.sort_values(by="time", ascending=False).head(), index=False
        )
        self._total_rows_panel = pn.pane.Markdown(f"Total rows: {len(self.data)}")
        self.view = pn.Column(
            pn.pane.Markdown("## Data Load"),
            pn.pane.Markdown(info_head),
            pn.Param(self, parameters=["ticker", "period"], show_name=False),
            self._dataframe_panel,
            self._total_rows_panel,
        )

    @pn.depends("ticker", "period", "interval", watch=True)
    def _load_data(self):
        self.loading = True
        if self.period > 1:
            self.param.interval.constant = True
            self.interval = "1d"
        else:
            self.param.interval.constant = False

        raw_data = _extract_raw_data(
            ticker=self.ticker, period=f"{self.period}mo", interval=self.interval
        )
        data = _transform_data(raw_data)
        self.data = data
        self.loading = False

    def _update_view(self, *events):
        if not self.data is None:
            self._dataframe_panel.object = self.data.sort_values("time").head()
            self._total_rows_panel.object = f"Total rows: {len(self.data)}"


class CandleStickSection(BaseSection):
    """Section with CandleStick analysis tool"""

    def _init_view(self):
        info = """## Candle Stick Plot

We can use a [*candlestick chart*](https://en.wikipedia.org/wiki/Candlestick_chart) to visualize the
Open, High, Low, Close price data and histograms to visualize the Volume.

Technically we use HoloViews [`Segments`]\
(https://holoviews.org/reference/elements/bokeh/Segments.html), [`Rectangles`]\
(https://holoviews.org/reference/elements/bokeh/Rectangles.html) and [`Histogram`]\
(https://holoviews.org/reference/elements/bokeh/Histogram.html) to create the plots and Panel
[`GridSpec`](https://panel.holoviz.org/reference/layouts/GridSpec.html) to lay them
out.
"""
        self.view = pn.Column(
            pn.pane.Markdown(info),
            pn.GridSpec(sizing_mode="stretch_both", margin=0),
            sizing_mode="stretch_both",
        )

    def _update_view(self, *events):
        if not self.data is None:
            self.view[1] = create_candle_stick_with_histograms(self.data)


class SignalAnalysisSection(BaseSection):
    """Section with Signal Processing analysis tool"""

    bins = param.Integer(default=50, bounds=(10, 200), step=10, label="Bins")
    kde_factor = param.Number(default=0.1, bounds=(0.01, 0.5), step=0.01, label="KDE Factor")
    min_prom_factor = param.Number(
        default=0.3, bounds=(0.01, 1.0), step=0.01, label="Prominence Factor"
    )
    add_peak_and_prominence = param.Boolean(default=False, label="Show Peak Prominence and Width")

    def _init_view(self):
        # pylint: disable=line-too-long
        info_distribution = """## Signal Processing

We can use [Signal Processing](https://en.wikipedia.org/wiki/Signal_processing) to better
understand the relation between Price and Volume.

Technically we use [`np.histogram`]\
(https://numpy.org/doc/stable/reference/generated/numpy.histogram.html) and [`holoviews.Histogram`]\
(https://holoviews.org/reference/elements/bokeh/Histogram.html) to create a *normed histogram*.

We use [`scipy.stats.gaussian_kde`]\
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html]) to find an
estimate of the [*probability density function*]\
(https://en.wikipedia.org/wiki/Probability_density_function)
and [`holoviews.Curve`](https://holoviews.org/reference/elements/bokeh/Curve.html) to visualize it.

We use [`scipy.signal.find_peaks`]\
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html?highlight=find_peaks#scipy.signal.find_peaks)
to find the *peaks* and their *prominence* and *width*. We use [`holoviews.Scatter`]\
(https://holoviews.org/reference/elements/matplotlib/Scatter.html) and [`holoviews.Point`]\
(https://holoviews.org/reference/elements/matplotlib/Points.html) to visualize it."""
        self._plot_panel = pn.pane.HoloViews(sizing_mode="stretch_both")
        self.view = pn.Column(
            pn.pane.Markdown(info_distribution),
            pn.Param(
                self,
                parameters=["bins", "kde_factor", "min_prom_factor", "add_peak_and_prominence"],
                show_name=False,
            ),
            self._plot_panel,
            sizing_mode="stretch_both",
        )

    @pn.depends("kde_factor", "min_prom_factor", "bins", "add_peak_and_prominence", watch=True)
    def _update_view2(self, *_):
        self._update_view()

    def _update_view(self, *_):
        hist_data = _calculate_vol_distribution_analysis(self.data, bins=self.bins)
        _, xrange, ticks_per_sample, kdy = _kde_analysis(self.data, kde_factor=self.kde_factor)
        _, pkx, pky, peak_props = _signal_analysis(xrange, kdy, self.min_prom_factor)
        plot = (
            _create_signal_analysis_plot(
                hist_data,
                xrange,
                ticks_per_sample,
                kdy,
                pkx,
                pky,
                peak_props,
                self.add_peak_and_prominence,
            )
            .redim(volume="Volume density")
            .opts(responsive=True, min_height=500)
        )
        self._plot_panel.object = plot


# endregion SECTIONS


def view() -> pn.Column:
    """Returns the app

    Returns:
        FastListTemplate: The app layed out in a nice template
    """
    load_data_section = LoadDataSection()
    candle_stick_and_volume_section = CandleStickSection(data=load_data_section.data)
    signal_analysis_section = SignalAnalysisSection(data=load_data_section.data)

    @pn.depends(load_data_section.param.data, watch=True)
    def _update_data(data):
        candle_stick_and_volume_section.data = data
        signal_analysis_section.data = data

    @pn.depends(loading=load_data_section.param.loading, watch=True)
    def _update_loading(loading):
        candle_stick_and_volume_section.loading = loading
        signal_analysis_section.loading = loading

    return pn.Column(
        load_data_section.view, candle_stick_and_volume_section.view, signal_analysis_section.view
    )


if __name__.startswith("bokeh"):
    config.extension(url="volume_profile_analysis", accent_color=ACCENT_COLOR)

    for component in view():
        component.servable()
