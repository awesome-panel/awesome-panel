import matplotlib.pyplot as plt
import pandas as pd
import panel as pn
import param
import seaborn as sns
from panel.interact import interact


def MyCustomWidget(data):
    def _update_plot_pane(column):
        plt.close()
        # Note:
        # - I get exception if plt.close is below ax line. See https://github.com/holoviz/panel/issues/1482
        # - The plot does not change if I remove plot.close() fully.

        ax = sns.distplot(df[self.column])
        self._plot_pane.object = ax.figure

    return interact()

df = pd.DataFrame(data={"x": [1, 2, 3, 4, 5, 6, 7], "y": [1, 2, 2, 4, 5, 9, 7]})
MyCustomWidget(df).servable()
