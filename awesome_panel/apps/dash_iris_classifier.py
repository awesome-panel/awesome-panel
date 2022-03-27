# pylint: disable=line-too-long
"""
A simple Machine Learning application. Can be compared to a similar Dash app from the
blog post [Deploy Machine Learning Model Using Dash and pipenv](https://towardsdatascience.com/deploy-machine-learning-model-using-dash-and-pipenv-c543569c33a6)
"""
# pylint: enable=line-too-long
import numpy as np
import panel as pn
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

from awesome_panel import config

# can be replaced by pn.extension
config.extension(url="dash_iris_classifier")


def get_model(Classifier=KNeighborsClassifier):  # pylint: disable=invalid-name
    """Returns model trained on iris dataset"""
    iris = datasets.load_iris()
    data = iris.data
    target = iris.target
    # Did not create XGB classifier as it would add 100MB dependency
    clf = Classifier()
    clf.fit(data, target)
    return clf


if not "dash_iris_classifier" in pn.state.cache:
    # We only train the model once and then reuse across users
    pn.state.cache["dash_iris_classifier"] = get_model()


def predict(sepal_length, sepal_width, petal_length, petal_width, model):
    """Returns prediction"""
    data = np.array(
        [[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]]
    )
    prediction = model.predict(data)[0]
    if prediction == 0:
        output = "Iris-Setosa"
    elif prediction == 1:
        output = "Iris-Versicolor"
    else:
        output = "Iris-Virginica"
    return f"The predicted Iris species is **{output}**."


def get_iris_explorer():
    """Returns a component for exploring iris predictions"""
    model = pn.state.cache["dash_iris_classifier"]

    sepal_length = pn.widgets.FloatSlider(value=5.8, start=4.0, end=8.0, name="Sepal Length (CM)")
    sepal_width = pn.widgets.FloatSlider(value=3.0, start=2.0, end=5.0, name="Sepal Width (CM)")
    petal_length = pn.widgets.FloatSlider(value=3.8, start=1.0, end=7.0, name="Petal Length (CM)")
    petal_width = pn.widgets.FloatSlider(value=1.2, start=0.1, end=3.0, name="Petal Width (CM)")

    settings = pn.Column(sepal_length, sepal_width, petal_length, petal_width, sizing_mode="fixed")

    ipredict = pn.bind(
        predict,
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width,
        model=model,
    )

    return pn.Row(settings, ipredict, align="end")


if __name__.startswith("bokeh"):
    get_iris_explorer().servable()
