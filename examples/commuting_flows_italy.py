"""
Source: https://awesome-panel.org/resources/commuting_flows_italian_regions/
"""
import holoviews as hv
import numpy as np
import pandas as pd
import panel as pn
from bokeh.models import HoverTool
from shapely.geometry import LineString

# Load the bokeh extension
hv.extension("bokeh")

# Set the sizing mode
pn.extension(sizing_mode="stretch_width")

# Dashboard title
DASH_TITLE = "Commuting flows between Italian Regions"

# Default colors for the dashboard
ACCENT = "#2f4f4f"
INCOMING_COLOR = "rgba(0, 108, 151, 0.75)"
OUTGOING_COLOR = "rgba(199, 81, 51, 0.75)"
INTERNAL_COLOR = "rgba(47, 79, 79, 0.55)"

# Default colors for indicators
DEFAULT_COLOR = "white"
TITLE_SIZE = "18pt"
FONT_SIZE = "20pt"

# Min/Max node size
MIN_PT_SIZE = 7
MAX_PT_SIZE = 10

# Min/Max curve width
MIN_LW = 1
MAX_LW = 10

# Dataframes dtypes
ITA_REGIONS_DTYPES = {
    "cod_reg": "uint8",
    "den_reg": "object",
    "x": "object",
    "y": "object",
}

NODES_DTYPES = {
    "cod_reg": "uint8",
    "x": "float64",
    "y": "float64",
}

EDGES_DTYPES = {
    "motivo": "object",
    "interno": "bool",
    "flussi": "uint32",
    "reg_o": "uint8",
    "reg_d": "uint8",
    "x_o": "float64",
    "y_o": "float64",
    "x_d": "float64",
    "y_d": "float64",
}

# Dictionary that maps region code to its name
ITA_REGIONS = {
    1: "Piemonte",
    2: "Valle d'Aosta/Vallée d'Aoste",
    3: "Lombardia",
    4: "Trentino-Alto Adige/Südtirol",
    5: "Veneto",
    6: "Friuli-Venezia Giulia",
    7: "Liguria",
    8: "Emilia-Romagna",
    9: "Toscana",
    10: "Umbria",
    11: "Marche",
    12: "Lazio",
    13: "Abruzzo",
    14: "Molise",
    15: "Campania",
    16: "Puglia",
    17: "Basilicata",
    18: "Calabria",
    19: "Sicilia",
    20: "Sardegna",
}

# Dictionary of options (Label/option) for commuting purpose
COMMUTING_PURPOSE = {
    "Work": "Lavoro",
    "Study": "Studio",
    "Total": "Totale",
}

# Dashboard description
DASH_DESCR = f"""
<div>
  <hr />
  <p>A Panel dashboard showing <b style="color:{INCOMING_COLOR};">incoming</b>
    and <b style="color:{OUTGOING_COLOR};">outgoing</b> commuting flows
    for work and study between Italian Regions.</p>
  <p>The width of the curves reflects the magnitude of the flows.</p>
  <p>
    <a href="https://www.istat.it/it/archivio/139381" target="_blank">Commuting data</a> from the
    15th Population and Housing Census (Istat, 2011).
  </p>
  <p>
    <a href="https://www.istat.it/it/archivio/222527" target="_blank">Administrative boundaries</a> from
    ISTAT.
  </p>
  <hr />
</div>
"""

CSS_FIX = """
:host(.outline) .bk-btn.bk-btn-primary.bk-active, :host(.outline) .bk-btn.bk-btn-primary:active {
    color: var(--foreground-on-accent-rest) !important;
}
"""

if not CSS_FIX in pn.config.raw_css:
    pn.config.raw_css.append(CSS_FIX)


def get_incoming_numind(edges, region_code, comm_purpose):
    """
    Returns the total incoming commuters to the selected Region.
    """

    # Get the value of incoming commuters
    if comm_purpose == "Totale":
        query = f"reg_d == {region_code} & interno == 0"
    else:
        query = f"(reg_d == {region_code} & motivo == '{comm_purpose}' & interno == 0)"

    flows = edges.query(query)["flussi"].sum()

    return pn.indicators.Number(
        name="Incoming",
        value=flows,
        default_color=DEFAULT_COLOR,
        styles={"background": INCOMING_COLOR, "padding": "5px 10px 5px 10px", "border-radius": "5px"},
        title_size=TITLE_SIZE,
        font_size=FONT_SIZE,
        sizing_mode="stretch_width",
        align="center",
        css_classes=["center_number"],
    )


def get_outgoing_numind(edges, region_code, comm_purpose):
    """
    Returns the outgoing commuters from
    the selected Region.
    """

    # Get the value of outgoing commuters
    if comm_purpose == "Totale":
        query = f"reg_o == {region_code} & interno == 0"
    else:
        query = f"(reg_o == {region_code} & motivo == '{comm_purpose}' & interno == 0)"

    flows = edges.query(query)["flussi"].sum()

    return pn.indicators.Number(
        name="Outgoing",
        value=flows,
        default_color=DEFAULT_COLOR,
        styles={"background": OUTGOING_COLOR, "padding": "5px 10px 5px 10px", "border-radius": "5px"},
        title_size=TITLE_SIZE,
        font_size=FONT_SIZE,
        sizing_mode="stretch_width",
        align="center",
        css_classes=["center_number"],
    )


def get_internal_numind(edges, region_code, comm_purpose):
    """
    Returns the number of internal commuters of
    the selected Region.
    """

    # Get the value of internal commuters
    if comm_purpose == "Totale":
        query = f"reg_o == {region_code} & interno == 1"
    else:
        query = f"(reg_o == {region_code} & motivo == '{comm_purpose}' & interno == 1)"

    flows = edges.query(query)["flussi"].sum()

    return pn.indicators.Number(
        name="Internal mobility",
        value=flows,
        default_color=DEFAULT_COLOR,
        styles={"background": INTERNAL_COLOR, "padding": "5px 10px 5px 10px", "border-radius": "5px"},
        title_size=TITLE_SIZE,
        font_size=FONT_SIZE,
        sizing_mode="stretch_width",
        align="center",
        css_classes=["center_number"],
    )


def filter_edges(edges, region_code, comm_purpose):
    """
    This function filters the rows of the edges for
    the selected Region and commuting purpose.
    """

    if comm_purpose == "Totale":
        query = f"(reg_o == {region_code} & interno == 0) |"
        query += f" (reg_d == {region_code} & interno == 0)"
    else:
        query = f"(reg_o == {region_code} & motivo == '{comm_purpose}' & interno == 0) |"
        query += f" (reg_d == {region_code} & motivo == '{comm_purpose}' & interno == 0)"
    return edges.query(query)


def get_nodes(nodes, edges, region_code, comm_purpose):
    """
    Get the graph's nodes for the selected Region and commuting purpose
    """

    # Filter the edges by Region and commuting purpose
    filt_edges = filter_edges(edges, region_code, comm_purpose)

    # Find the unique values of region codes
    region_codes = np.unique(filt_edges[["reg_o", "reg_d"]].values)

    # Filter the nodes
    nodes = nodes[nodes["cod_reg"].isin(region_codes)]

    # Reoder the columns for hv.Graph
    nodes = nodes[["x", "y", "cod_reg"]]

    # Assign the node size
    nodes["size"] = np.where(
        nodes["cod_reg"] == region_code, MAX_PT_SIZE, MIN_PT_SIZE
    )

    # Assigns a marker to the nodes
    nodes["marker"] = np.where(
        nodes["cod_reg"] == region_code, "square", "circle"
    )

    return nodes


def get_bezier_curve(x_o, y_o, x_d, y_d, steps=25):
    """
    Draw a Bézier curve defined by a start point, endpoint and a control points
    Source: https://stackoverflow.com/questions/69804595/trying-to-make-a-bezier-curve-on-pygame-library
    """

    # Generate the O/D linestring
    od_line = LineString([(x_o, y_o), (x_d, y_d)])

    # Calculate the offset distance of the control point
    offset_distance = od_line.length / 2

    # Create a line parallel to the original at the offset distance
    offset_pline = od_line.parallel_offset(offset_distance, "left")

    # Get the XY coodinates of the control point
    ctrl_x = offset_pline.centroid.x
    ctrl_y = offset_pline.centroid.y

    # Calculate the XY coordinates of the Bézier curve
    t = np.array([i * 1 / steps for i in range(0, steps + 1)])
    x_coords = x_o * (1 - t) ** 2 + 2 * (1 - t) * t * ctrl_x + x_d * t**2
    y_coords = y_o * (1 - t) ** 2 + 2 * (1 - t) * t * ctrl_y + y_d * t**2

    return (x_coords, y_coords)


def get_edge_width(flow, min_flow, max_flow):
    """
    This function calculates the width of the curves
    according to the magnitude of the flow.
    """

    return MIN_LW + np.power(flow - min_flow, 0.57) * (
        MAX_LW - MIN_LW
    ) / np.power(max_flow - min_flow, 0.57)


def get_edges(nodes, edges, region_code, comm_purpose):
    """
    Get the graph's edges for the selected Region and commuting purpose
    """

    # Filter the edges by Region and commuting purpose
    filt_edges = filter_edges(edges, region_code, comm_purpose).copy()

    # Aggregate the flows by Region of origin and destination
    if comm_purpose == "Totale":
        filt_edges = (
            filt_edges.groupby(["reg_o", "reg_d"])
            .agg(
                motivo=("motivo", "first"),
                interno=("interno", "first"),
                flussi=("flussi", "sum"),
            )
            .reset_index()
        )

    # Assign Region names
    filt_edges.loc[:,"den_reg_o"] = filt_edges["reg_o"].map(ITA_REGIONS)
    filt_edges.loc[:,"den_reg_d"] = filt_edges["reg_d"].map(ITA_REGIONS)

    # Add xy coordinates of origin
    filt_edges = filt_edges.merge(
        nodes.add_suffix("_o"), left_on="reg_o", right_on="cod_reg_o"
    )

    # Add xy coordinates of destination
    filt_edges = filt_edges.merge(
        nodes.add_suffix("_d"), left_on="reg_d", right_on="cod_reg_d"
    )

    # Get the Bézier curve
    filt_edges["curve"] = filt_edges.apply(
        lambda row: get_bezier_curve(
            row["x_o"], row["y_o"], row["x_d"], row["y_d"]
        ),
        axis=1,
    )

    # Get the minimum/maximum flow
    min_flow = filt_edges["flussi"].min()
    max_flow = filt_edges["flussi"].max()

    # Calculate the curve width
    filt_edges["width"] = filt_edges.apply(
        lambda row: get_edge_width(
            row["flussi"],
            min_flow,
            max_flow,
        ),
        axis=1,
    )

    # Assigns the color to the incoming/outgoing edges
    filt_edges["color"] = np.where(
        filt_edges["reg_d"] == region_code, INCOMING_COLOR, OUTGOING_COLOR
    )

    filt_edges = filt_edges.sort_values(by="flussi")

    return filt_edges


def get_flow_map(nodes, edges, region_admin_bounds, region_code, comm_purpose):
    """
    Returns a Graph showing incoming and outgoing commuting flows
    for the selected Region and commuting purpose.
    """

    def hook(plot, element):
        """
        Custom hook for disabling x/y tick lines/labels
        """
        plot.state.xaxis.major_tick_line_color = None
        plot.state.xaxis.minor_tick_line_color = None
        plot.state.xaxis.major_label_text_font_size = "0pt"
        plot.state.yaxis.major_tick_line_color = None
        plot.state.yaxis.minor_tick_line_color = None
        plot.state.yaxis.major_label_text_font_size = "0pt"

    # Define a custom Hover tool
    flow_map_hover = HoverTool(
        tooltips=[
            ("Origin", "@den_reg_o"),
            ("Destination", "@den_reg_d"),
            ("Commuters", "@flussi"),
        ]
    )

    # Get the Nodes of the selected Region and commuting purpose
    region_graph_nodes = get_nodes(nodes, edges, region_code, comm_purpose)

    # Get the Edges of the selected Region and commuting purpose
    region_graph_edges = get_edges(nodes, edges, region_code, comm_purpose)

    # Get the list of Bézier curves
    curves = region_graph_edges["curve"].to_list()

    # Get the administrative boundary of the selected Region
    region_admin_bound = region_admin_bounds[
        (region_admin_bounds["cod_reg"] == region_code)
    ].to_dict("records")

    # Draw the administrative boundary using hv.Path
    region_admin_bound_path = hv.Path(region_admin_bound)
    region_admin_bound_path.opts(color=ACCENT, line_width=1.0)

    # Build a Graph from Edges, Nodes and Bézier curves
    region_flow_graph = hv.Graph(
        (region_graph_edges.drop("curve", axis=1), region_graph_nodes, curves)
    )

    # Additional plot options
    region_flow_graph.opts(
        title="Incoming and outgoing commuting flows",
        xlabel="",
        ylabel="",
        node_color="white",
        node_hover_fill_color="magenta",
        node_line_color=ACCENT,
        node_size="size",
        node_marker="marker",
        edge_color="color",
        edge_hover_line_color="magenta",
        edge_line_width="width",
        inspection_policy="edges",
        tools=[flow_map_hover],
        hooks=[hook],
        frame_height=500,
    )

    # Compose the flow map
    flow_map = (
        hv.element.tiles.CartoLight()
        * region_admin_bound_path
        * region_flow_graph
    )

    return flow_map


# Load the edges as a Dataframe
@pn.cache
def get_edges_df():
    return pd.read_json(
        "https://raw.githubusercontent.com/ivandorte/panel-commuting-istat/main/data/edges.json",
        orient="split",
        dtype=EDGES_DTYPES,
    )
edges_df = get_edges_df()

# Load the nodes as a Dataframe
@pn.cache
def get_nodes_df():
    return pd.read_json(
        "https://raw.githubusercontent.com/ivandorte/panel-commuting-istat/main/data/nodes.json",
        orient="split",
        dtype=NODES_DTYPES,
    )

nodes_df = get_nodes_df()

# Load the italian regions as a Dataframe
@pn.cache
def get_region_admin_bounds_df():
    return pd.read_json(
        "https://raw.githubusercontent.com/ivandorte/panel-commuting-istat/main/data/italian_regions.json",
        orient="split",
        dtype=ITA_REGIONS_DTYPES,
    )
region_admin_bounds_df = get_region_admin_bounds_df()

# Region selector
region_options = dict(map(reversed, ITA_REGIONS.items()))
region_options = dict(sorted(region_options.items()))

region_select = pn.widgets.Select(
    name="Region:",
    options=region_options,
    sizing_mode="stretch_width",
)

# Toggle buttons to select the commuting purpose
purpose_select = pn.widgets.ToggleGroup(
    name="",
    options=COMMUTING_PURPOSE,
    behavior="radio",
    sizing_mode="stretch_width",
    button_type="primary", button_style="outline"
)

# Description pane
descr_pane = pn.pane.HTML(DASH_DESCR, styles={"text-align": "left"})

# Numeric indicator for incoming flows
incoming_numind_bind = pn.bind(
    get_incoming_numind,
    edges=edges_df,
    region_code=region_select,
    comm_purpose=purpose_select,
)

# Numeric indicator for outgoing flows
outgoing_numind_bind = pn.bind(
    get_outgoing_numind,
    edges=edges_df,
    region_code=region_select,
    comm_purpose=purpose_select,
)

# Numeric indicator for internal flows
internal_numind_bind = pn.bind(
    get_internal_numind,
    edges=edges_df,
    region_code=region_select,
    comm_purpose=purpose_select,
)

# Flow map
flowmap_bind = pn.bind(
    get_flow_map,
    nodes=nodes_df,
    edges=edges_df,
    region_admin_bounds=region_admin_bounds_df,
    region_code=region_select,
    comm_purpose=purpose_select,
)

# Compose the layout
layout = pn.Row(
    pn.Column(
        region_select,
        purpose_select,
        pn.Row(incoming_numind_bind, outgoing_numind_bind),
        internal_numind_bind,
        descr_pane,
        width=350,
    ),
    flowmap_bind,
)

pn.template.FastListTemplate(
    site="",
    logo="https://raw.githubusercontent.com/ivandorte/panel-commuting-istat/main/icons/home_work.svg",
    title=DASH_TITLE,
    theme="default",
    theme_toggle=False,
    accent=ACCENT,
    neutral_color="white",
    main=[layout],
    main_max_width="1000px",
).servable()