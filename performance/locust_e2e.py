# run: locust -f performance/locust_e2e.py
from locust import HttpUser, between, task


def to_str(app):
    name = app.name.lower().replace(" ", "_").replace(":", "_").replace(".", "_")
    return f"""
@task(1)
def {name}(self):
    self.client.get("/{app.url}")
"""


def print_tasks():
    from awesome_panel import config

    for app in config.APPLICATIONS:
        print(to_str(app))


# print_tasks()


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def about(self):
        self.client.get("/about")

    @task(1)
    def async_tasks(self):
        self.client.get("/async_tasks")

    @task(1)
    def community_gallery(self):
        self.client.get("/awesome_list")

    @task(1)
    def bootstrap_alerts(self):
        self.client.get("/bootstrap_alerts")

    @task(1)
    def bootstrap_card(self):
        self.client.get("/bootstrap_card")

    @task(1)
    def bootstrap_dashboard(self):
        self.client.get("/bootstrap_dashboard")

    @task(1)
    def caching_example(self):
        self.client.get("/caching_example")

    @task(1)
    def classic_dashboard(self):
        self.client.get("/classic_dashboard")

    @task(1)
    def data_explorer_loading(self):
        self.client.get("/data_explorer_loading")

    @task(1)
    def dataframe_formatting(self):
        self.client.get("/dataframe_formatting")

    @task(1)
    def dependent_widgets(self):
        self.client.get("/dependent_widgets")

    @task(1)
    def de_tr__object_detection(self):
        self.client.get("/detr")

    @task(1)
    def echarts(self):
        self.client.get("/echarts")

    @task(1)
    def fastgridtemplate(self):
        self.client.get("/fast_grid_template")

    @task(1)
    def fileinput_area(self):
        self.client.get("/fileinput_area")

    @task(1)
    def app_gallery(self):
        self.client.get("/gallery")

    @task(1)
    def google_map_viewer(self):
        self.client.get("/google_map_viewer")

    @task(1)
    def highcharts_network(self):
        self.client.get("/highcharts_network")

    @task(1)
    def holoviews_linked_brushing(self):
        self.client.get("/holoviews_linked_brushing")

    @task(1)
    def home(self):
        self.client.get("/home")

    @task(1)
    def image_classifier(self):
        self.client.get("/image_classifier")

    @task(1)
    def js_actions(self):
        self.client.get("/js_actions")

    @task(1)
    def altair(self):
        self.client.get("/lib_altair")

    @task(1)
    def bokeh(self):
        self.client.get("/lib_bokeh")

    @task(1)
    def datashader(self):
        self.client.get("/lib_datashader")

    @task(1)
    def deck_gl(self):
        self.client.get("/lib_deckgl")

    @task(1)
    def echarts(self):
        self.client.get("/lib_echarts")

    @task(1)
    def folium(self):
        self.client.get("/lib_folium")

    @task(1)
    def holoviews(self):
        self.client.get("/lib_holoviews")

    @task(1)
    def hvplot(self):
        self.client.get("/lib_hvplot")

    @task(1)
    def ipysheet(self):
        self.client.get("/lib_ipysheet")

    @task(1)
    def matplotlib(self):
        self.client.get("/lib_matplotlib")

    @task(1)
    def plotly(self):
        self.client.get("/lib_plotly")

    @task(1)
    def plotnine(self):
        self.client.get("/lib_plotnine")

    @task(1)
    def pydeck(self):
        self.client.get("/lib_pydeck")

    @task(1)
    def pyecharts(self):
        self.client.get("/lib_pyecharts")

    # @task(1)
    # def pyvista(self):
    #     self.client.get("/lib_pyvista")

    @task(1)
    def seaborn(self):
        self.client.get("/lib_seaborn")

    @task(1)
    def vega(self):
        self.client.get("/lib_vega")

    # @task(1)
    # def vtk(self):
    #     self.client.get("/lib_vtk")

    @task(1)
    def kickstarter_dashboard(self):
        self.client.get("/kickstarter_dashboard")

    @task(1)
    def loading_spinners(self):
        self.client.get("/loading_spinners")

    @task(1)
    def model_viewer(self):
        self.client.get("/model_viewer")

    @task(1)
    def ngl_viewer(self):
        self.client.get("/ngl_viewer")

    @task(1)
    def pandas_profiling(self):
        self.client.get("/pandas_profiling_app")

    @task(1)
    def component_explorer(self):
        self.client.get("/component_explorer")

    @task(1)
    def param_reference(self):
        self.client.get("/param_reference")

    @task(1)
    def perspective_viewer(self):
        self.client.get("/perspective")

    @task(1)
    def progress_extension(self):
        self.client.get("/progress_extension")

    @task(1)
    def leaflet_component_using_reactivehtml(self):
        self.client.get("/reactive_leaflet")

    @task(1)
    def share_on_social_buttons(self):
        self.client.get("/share_on_social_buttons")

    @task(1)
    def shoelace(self):
        self.client.get("/shoelace")

    @task(1)
    def soccer_analytics_dashboard(self):
        self.client.get("/soccer_analytics_dashboard")

    @task(1)
    def streaming_indicators(self):
        self.client.get("/streaming_indicators")

    @task(1)
    def streaming_plots(self):
        self.client.get("/streaming_plots")

    @task(1)
    def tabulator(self):
        self.client.get("/tabulator")

    @task(1)
    def text_to_speech(self):
        self.client.get("/text_to_speech")

    @task(1)
    def volume_profile_analysis(self):
        self.client.get("/volume_profile_analysis")

    def on_start(self):
        pass
