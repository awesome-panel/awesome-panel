"""Example"""
import hvplot.pandas
import pandas as pd

df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
plot = df.hvplot(x="x", y="y")
