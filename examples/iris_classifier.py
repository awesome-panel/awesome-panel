# pylint: disable=line-too-long
"""
See https://awesome-panel.org/resources/bootstrap_dashboard/
"""
# pylint: enable=line-too-long
import numpy as np
import panel as pn
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

@pn.cache
def get_model(Classifier=KNeighborsClassifier):  # pylint: disable=invalid-name
    """Returns model trained on iris dataset"""
    iris = datasets.load_iris()
    data = iris.data  # pylint: disable=no-member
    target = iris.target  # pylint: disable=no-member
    # Did not create XGB classifier as it would add 100MB dependency
    clf = Classifier()
    clf.fit(data, target)
    return clf


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
    model=get_model()

    sepal_length = pn.widgets.FloatSlider(value=5.8, start=4.0, end=8.0, name="Sepal Length (cm)")
    sepal_width = pn.widgets.FloatSlider(value=3.0, start=2.0, end=5.0, name="Sepal Width (cm)")
    petal_length = pn.widgets.FloatSlider(value=3.8, start=1.0, end=7.0, name="Petal Length (cm)")
    petal_width = pn.widgets.FloatSlider(value=1.2, start=0.1, end=3.0, name="Petal Width (cm)")

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


if pn.state.served:
    pn.extension()
    
    pn.template.MaterialTemplate(
        title="Predict Iris Flower Species with Scikit Learn", main=[get_iris_explorer()]
    ).servable()
