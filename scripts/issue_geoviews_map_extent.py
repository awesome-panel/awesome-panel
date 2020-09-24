import traceback

import geopandas as gpd
import geoviews as gv
import holoviews as hv
import pandas as pd
import panel as pn
import param
from datashader.utils import lnglat_to_meters
from shapely.geometry import Point, box

gv.extension("bokeh", logo=False)
pn.extension()

# Used to make sure we only read the file once
FILE_STORE = {}


class Inputs(param.Parameterized):

    input_file = param.FileSelector(
        path=r".\sample_data\\*.csv", doc="A .csv file selector for input data"
    )
    x_field = param.Selector(doc="A field selector for longitude")
    y_field = param.Selector(doc="A field selector for latitude")
    id_field = param.Selector(doc="A field selector for the identifier")
    data = None

    def __init__(self, **params):
        super().__init__(**params)

        if self.param.input_file.default:
            self.input_file = self.param.input_file.default

        self._update_inputs()

    @param.depends("input_file", watch=True)
    def _update_inputs(self):
        if self.input_file in FILE_STORE:
            df = FILE_STORE[self.input_file].copy(deep=True)
        else:
            df = pd.read_csv(self.input_file)
            FILE_STORE[self.input_file] = df.copy(deep=True)

        numeric_cols = list(df.select_dtypes(include=["float64"]).columns)
        columns = [x for i, x in enumerate(df.columns) if x != "Unnamed: 0"]
        self.param.x_field.objects = numeric_cols
        if "lng" in numeric_cols:
            self.x_field = "lng"
        elif numeric_cols:
            self.x_field = numeric_cols[0]

        self.param.y_field.objects = numeric_cols
        if "lat" in numeric_cols:
            self.y_field = "lat"
        elif numeric_cols:
            self.y_field = numeric_cols[0]

        self.param.id_field.objects = columns
        if "comName" in columns:
            self.id_field = "comName"
        elif columns:
            self.id_field = columns[0]

        self.data = df


class Mapview(param.Parameterized):

    opts = dict(width=1200, height=750, xaxis=None, yaxis=None, show_grid=False)
    tiles = gv.tile_sources.CartoEco().apply.opts(**opts)
    extents = param.Parameter(default=(-168, -60, 168, 83), precedence=-1)
    tiles.extents = extents.default
    box_polygons = gv.Polygons([]).opts(fill_alpha=0.1)
    box_colours = ["red", "blue", "green", "orange", "purple"]
    box_stream = hv.streams.BoxEdit(
        source=box_polygons, num_objects=5, styles={"fill_color": box_colours}
    )
    template_df = pd.DataFrame({"x_meters": [], "y_meters": []}, columns=["x_meters", "y_meters"])
    dfstream = hv.streams.Buffer(template_df, index=False, length=10000)
    points = hv.DynamicMap(hv.Points, streams=[dfstream]).opts(
        size=5, color="green", fill_alpha=0.3, line_alpha=0.4
    )

    def show_map(self):
        return self.tiles * self.box_polygons * self.points


class Dashboard(param.Parameterized):

    input1 = Inputs()
    input2 = Inputs()
    input3 = Inputs()
    input4 = Inputs()
    input5 = Inputs()
    mapview = Mapview()

    run_analysis = param.Action(label="Run")
    summary = pd.DataFrame()

    def __init__(self, **params):
        super().__init__(**params)

        self.run_analysis = self._run_analysis
        self.summary = pd.DataFrame({"x": [1]})
        self.summary_pane = pn.widgets.DataFrame(
            self.summary, disabled=True, fit_columns=True, width=700
        )

    def project_to_meters(self, df, x, y):
        try:
            df.loc[:, "x_meters"], df.loc[:, "y_meters"] = lnglat_to_meters(df[x], df[y])
            geometry = [Point(xy) for xy in zip(df.x_meters, df.y_meters)]
            web_merc = {"init": "epsg:3857"}
            return gpd.GeoDataFrame(df, crs=web_merc, geometry=geometry)
        except:
            print(
                """Could not project specified coordinate fields to meters. Make sure the X Field and Y Field
                  values have been set correctly.\n"""
            )

    def convert_box_stream_data_to_geometry(self):
        try:
            box_data = self.mapview.box_stream.data
            try:
                num_boxes = len(box_data["x0"])
            except:
                num_boxes = 0

            boxes = []
            for i in range(0, num_boxes):
                x0 = box_data["x0"][i]
                y0 = box_data["y0"][i]
                x1 = box_data["x1"][i]
                y1 = box_data["y1"][i]
                boxes.append(box(x0, y0, x1, y1))
            if len(boxes) > 0:
                return boxes
        except:
            print("Could not convert boxes drawn on map into geometries.\n")

    def _run_analysis(self, *events):
        try:
            # clear previous results
            self.mapview.dfstream.clear()

            # Convert each input into a GeoDataFrame and project coordinates to meters
            datasets = []
            id_fields = []
            for i in [self.input1, self.input2, self.input3, self.input4, self.input5]:
                if isinstance(i.data, pd.core.frame.DataFrame):
                    gdf = self.project_to_meters(i.data, i.x_field, i.y_field)
                    datasets.append(gdf)
                    id_fields.append(i.id_field)

            # Convert boxes drawn on the map into Shapely geometries
            if len(datasets) > 0:
                boxes = []
                box_data = self.mapview.box_stream.data
                for i in range(0, len(box_data["x0"])):
                    x0 = box_data["x0"][i]
                    y0 = box_data["y0"][i]
                    x1 = box_data["x1"][i]
                    y1 = box_data["y1"][i]
                    boxes.append(box(x0, y0, x1, y1))

                # Do intersections of each box on each GeoDataFrame & send results to the map
                df_all_boxes = pd.DataFrame()
                df_final = pd.DataFrame()
                box_labels = []
                for i in range(0, len(datasets)):
                    for b in boxes:
                        box_label = self.mapview.box_colours[boxes.index(b)] + "_box"
                        box_labels.append(box_label)
                        datasets[i][box_label] = datasets[i].intersects(b)
                        selected = (
                            datasets[i].loc[datasets[i][box_label] == True].drop(columns="geometry")
                        )
                        self.mapview.dfstream.send(pd.DataFrame(selected[["x_meters", "y_meters"]]))
                        selected.rename(columns={id_fields[i]: "identifier"}, inplace=True)
                        df_all_boxes = pd.concat(
                            [df_all_boxes, selected[["identifier", box_label]]],
                            axis=0,
                            ignore_index=True,
                        )

                for ident in pd.unique(df_all_boxes["identifier"]):
                    dfx = df_all_boxes.loc[df_all_boxes["identifier"] == ident]
                    box_values = {"identifier": [ident]}
                    for bl in box_labels:
                        # returns true if any of the values are true
                        # else returns false
                        box_values[bl] = [dfx[bl].any()]
                    df_ident = pd.DataFrame.from_dict(box_values)
                    df_final = pd.concat([df_final, df_ident], axis=0)

                def summarize_boxes(row):
                    cols = list(row.axes[0])
                    s = []
                    for c in cols:
                        if "box" in c:
                            if row.values[cols.index(c)]:
                                s.append(c.split("_")[0])
                    return ",".join(s)

                summary = df_final.copy()
                try:
                    summary["Found_In"] = summary.apply(lambda row: summarize_boxes(row), axis=1)
                    self.summary = summary
                    self.summary_pane.value = self.summary
                except:
                    print("There was an error creating the final output summary table.\n")
            else:
                print("You must select at least one input dataset.\n")
        except Exception as ext:
            print(ext)
            print("Something went wrong in the run_analysis() function.\n")
            traceback.print_exc()

    def view(self):

        desc = """This is a demonstration dashboard with incomplete functionality. Its purpose
        is to sit here and look pretty. We can put graphics and stuff in here to
        make it look all fancy."""

        logo = ".\images\logo_panel_stacked_s.png"

        button_desc = """The <i>Run</i> button will execute the spatial intersection and generate
        a table of identifiers found within each box and in multiple boxes.<br><br>
        Push the <i>Run</i> button after configuring all inputs and drawing boxes on the map."""

        return pn.Row(
            pn.Column("## Description", desc, logo),
            pn.Column(
                "### Configure Inputs",
                pn.Tabs(
                    ("Input 1", self.input1),
                    ("Input 2", self.input2),
                    ("Input 3", self.input3),
                    ("Input 4", self.input4),
                    ("Input 5", self.input5),
                ),
                button_desc,
                self.param.run_analysis,
            ),
            pn.Tabs(
                ("Map View", pn.Column(self.mapview.show_map())),
                ("Results Table", self.summary_pane),
            ),
        )


d = Dashboard()
d.view().servable()
