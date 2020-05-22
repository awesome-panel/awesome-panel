import datetime

# from application.pages.apps.spread_tracker.models import RiskRewardCalculation
# from application.pages.apps.spread_tracker.plots import SpreadPlot
# from application.pages.apps.spread_tracker.services import SpreadService
# from application.pages.apps.spread_tracker.views import RiskRewardCalculationView, SpreadView
import pathlib
from typing import Optional

import pandas as pd
import panel as pn
import param

HISTORICAL_SPREADS_PATH = pathlib.Path(__file__).parent / "spreads.csv"

DEFAULT_MARKET = "ttf"
MARKETS = ["ttf", "germany"]
DEFAULT_PRODUCT = "baseload"
PRODUCTS = ["baseload", "peakload"]
DEFAULT_PERIOD = "q1"
PERIODS = ["q1", "q2", "q3", "q4"]
THIS_YEAR = datetime.datetime.now().year
DEFAULT_YEAR = THIS_YEAR
YEARS = list(range(2010, THIS_YEAR + 5))

DEFAULT_RISK_REWARD_AGGREGATION = "sum"
RISK_REWARD_AGGREGATIONS = ["mean", "sum"]

DAYS_TO_DELIVERY_MAX = 500
DAYS_TO_DELIVERY_MIN = 1
DAYS_TO_DELIVERY_BOUNDS = (DAYS_TO_DELIVERY_MIN, DAYS_TO_DELIVERY_MAX)
DEFAULT_DAYS_TO_DELIVERY_START = 300
DEFAULT_DAYS_TO_DELIVERY_END = 10


class RiskRewardCalculation(param.Parameterized):
    """A model of a Risk Reward Calculation"""

    days_to_delivery_start: int = param.Integer(
        DEFAULT_DAYS_TO_DELIVERY_START, bounds=DAYS_TO_DELIVERY_BOUNDS
    )
    days_to_delivery_end: int = param.Integer(
        DEFAULT_DAYS_TO_DELIVERY_END, bounds=DAYS_TO_DELIVERY_BOUNDS
    )
    aggregation: str = param.ObjectSelector(
        default=DEFAULT_RISK_REWARD_AGGREGATION, objects=RISK_REWARD_AGGREGATIONS
    )

    spreads: pd.DataFrame = param.DataFrame()

    analysis = param.DataFrame()
    payoff_up = param.Number()
    payoff_down = param.Number()
    risk_reward = param.Number()

    @param.depends(
        "days_to_delivery_start", "days_to_delivery_end", "aggregation", "spreads", watch=True,
    )
    def _update(self):
        print("_update")
        spreads_filter = (self.spreads["days_to_delivery"] == self.days_to_delivery_start) | (
            self.spreads["days_to_delivery"] == self.days_to_delivery_end
        )
        spreads_on_days_to_delivery = self.spreads[spreads_filter]

        analysis = spreads_on_days_to_delivery.pivot(
            columns="days_to_delivery", values="value", index="spread",
        )
        analysis["change"] = (
            analysis[self.days_to_delivery_end] - analysis[self.days_to_delivery_start]
        )
        analysis = analysis.dropna()

        up_filter = analysis["change"] > 0
        down_filter = analysis["change"] < 0
        up_data = analysis[up_filter]
        down_data = analysis[down_filter]

        if self.aggregation == "mean":
            payoff_up = up_data.change.mean()
            payoff_down = down_data.change.mean()
        elif self.aggregation == "sum":
            payoff_up = up_data.change.sum()
            payoff_down = down_data.change.sum()

        if payoff_up and payoff_down:
            risk_reward = -payoff_up / payoff_down
        else:
            payoff_up = 0.0
            payoff_down = 0.0
            risk_reward = 0.0

        print(analysis.round(1).index)
        self.analysis = analysis.round(1)
        self.payoff_up = round(payoff_up, 1)
        self.payoff_down = round(payoff_down, 1)
        self.risk_reward = round(risk_reward, 1)


class RiskRewardCalculationComponent(param.Parameterized):
    risk_reward_calculation: RiskRewardCalculation = param.Parameter(RiskRewardCalculation())

    def __init__(self, risk_reward_calculation: Optional[RiskRewardCalculation] = None, **params):
        if risk_reward_calculation:
            self.risk_reward_calculation = risk_reward_calculation
        else:
            self.risk_reward_calculation = RiskRewardCalculation()
        super().__init__(**params)

    def _risk_reward_settings_view(self):
        return pn.Param(
            self.risk_reward_calculation,
            parameters=["days_to_delivery_start", "days_to_delivery_end", "aggregation"],
            default_layout=pn.Row,
            sizing_mode="stretch_width",
            show_name=False,
        )

    def _risk_reward_results_view(self):
        return pn.Param(
            self.risk_reward_calculation,
            parameters=["payoff_up", "payoff_down", "risk_reward",],
            default_layout=pn.Row,
            sizing_mode="stretch_width",
            show_name=False,
        )

    def _risk_reward_analysis_view(self):
        return pn.Param(
            self.risk_reward_calculation,
            parameters=["analysis",],
            sizing_mode="stretch_width",
            show_name=False,
        )

    def view(self):
        return pn.Column(
            "## Risk Reward Calculation",
            self._risk_reward_settings_view,
            "### Analysis",
            self._risk_reward_analysis_view,
            "### Results",
            self._risk_reward_results_view,
        )


# class RiskRewardComponent(param.Parameterized):
#     spread = param.Parameter(Spread())
#     historical_spreads = param.DataFrame()

#     risk_reward_calculation_component = param.Parameter(RiskRewardCalculationComponent())

#     @param.depends(
#         "spread",
#         "spread.leg1",
#         "spread.leg1.market",
#         "spread.leg1.product",
#         "spread.leg1.period",
#         "spread.leg1.year",
#         "spread.leg2",
#         "spread.leg2.market",
#         "spread.leg2.product",
#         "spread.leg2.period",
#         "spread.leg2.year",
#         watch=True,
#     )
#     def _set_historical_spreads(self):
#         self.historical_spreads = SpreadService.get_historical_spreads(self.spread)
#         self.risk_reward_calculation_component.risk_reward_calculation.spreads = self.historical_spreads

#     @param.depends("spread")
#     def spreads_update_view(self):
#         return SpreadView.update_view(self.spread)

#     @param.depends("historical_spreads")
#     def historical_spreads_plot(self):
#         print("plotting")
#         if self.spread.leg1 == self.spread.leg2:
#             return pn.pane.Markdown("**The two legs are identical!**")
#         if self.historical_spreads is None or self.historical_spreads.empty:
#             return pn.pane.Markdown("**No historical data is available!**")
#         else:
#             return SpreadPlot.days_to_delivery_plot(self.historical_spreads)

#     def view(self):
#         return pn.Column(
#             self.spreads_update_view,
#             self.historical_spreads_plot,
#             self.risk_reward_calculation_component.view,
#         )


def historical_spreads():
    return pd.read_csv(HISTORICAL_SPREADS_PATH, parse_dates=["date"])


component = RiskRewardCalculationComponent()
component.risk_reward_calculation.spreads = historical_spreads()
component.view().servable()
