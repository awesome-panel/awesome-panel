# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pandas as pd
import panel as pn
from bokeh.models import ColumnDataSource

from awesome_panel.express.components import PerspectiveViewer

pn.config.sizing_mode = "stretch_width"


def test_constructor(document, comm):
    # Given
    data = [
        {"x": 1, "y": "a", "z": True},
        {"x": 2, "y": "b", "z": False},
        {"x": 3, "y": "c", "z": True},
        {"x": 4, "y": "d", "z": False},
    ]
    dataframe = pd.DataFrame(data)
    component = PerspectiveViewer(data=dataframe)

    assert component.html == (
        '<perspective-viewer class="perspective-viewer-material-dark" '
        'style="height:100%;width:100%" plugin="datagrid"></perspective-viewer>'
    )
    assert component.data is dataframe
    assert component.column_data_source_orient == "records"
    assert component.column_data_source_load_function == "load"

    model = component.get_root(document, comm=comm)
    assert component._models[model.ref["id"]][0] is model
    assert type(model).__name__ == "WebComponent"
    assert isinstance(model.columnDataSource, ColumnDataSource)
    assert model.columnDataSourceOrient == "records"
    assert model.columnDataSourceLoadFunction == "load"


if __name__.startswith("bokeh"):
    PerspectiveViewer.config()
    SHOW_HTML = True
    data = [
        {"x": 1, "y": "a", "z": True},
        {"x": 2, "y": "b", "z": False},
        {"x": 3, "y": "c", "z": True},
        {"x": 4, "y": "d", "z": False},
    ]
    dataframe = pd.DataFrame(data)
    perspective = PerspectiveViewer(height=500, data=dataframe)

    def section(component, message=None, show_html=SHOW_HTML):
        title = "## " + str(type(component)).split(".")[4][:-2]

        parameters = list(component._child_parameters())
        if show_html:
            parameters = ["html"] + parameters

        if message:
            return (
                pn.pane.Markdown(title),
                component,
                pn.Param(component, parameters=parameters),
                pn.pane.Markdown(message),
                pn.layout.Divider(),
            )
        return (
            pn.pane.Markdown(title),
            component,
            pn.Param(component, parameters=parameters),
            pn.layout.Divider(),
        )

    pn.Column(*section(perspective)).servable()
