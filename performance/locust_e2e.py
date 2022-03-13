# run: locust -f performance/locust_e2e.py
from locust import HttpUser, between, task


def to_str(app):
    name = app.name.lower().replace(" ", "_").replace(":", "_")
    return f"""
@task(1)
def {name}(self):
    self.client.get("/{app.url}")
"""


def print_tasks():
    from application_old import pages
    from awesome_panel_extensions.site import site

    for app in site.applications:
        print(to_str(app))


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def holoviews_linked_brushing(self):
        self.client.get("/holoviews-linked-brushing")

    @task(1)
    def ngl_molecule_viewer(self):
        self.client.get("/ngl-molecule-viewer")

    @task(1)
    def component_explorer(self):
        self.client.get("/panel-component-explorer")

    @task(1)
    def about(self):
        self.client.get("/about")

    @task(1)
    def async_tasks(self):
        self.client.get("/async-tasks")

    @task(1)
    def bootstrap_alerts(self):
        self.client.get("/bootstrap-alerts")

    @task(1)
    def bootstrap_card(self):
        self.client.get("/bootstrap-card")

    @task(1)
    def code_pane(self):
        self.client.get("/code-pane")

    @task(1)
    def dataframe_formatting(self):
        self.client.get("/dataframe-formatting")

    @task(1)
    def echarts(self):
        self.client.get("/echarts")

    @task(1)
    def material_components(self):
        self.client.get("/material-components")

    @task(1)
    def model_viewer(self):
        self.client.get("/model-viewer")

    @task(1)
    def perspective_viewer(self):
        self.client.get("/perspective")

    @task(1)
    def progress_extension(self):
        self.client.get("/progress-extension")

    @task(1)
    def share_on_social_buttons(self):
        self.client.get("/share-on-social-buttons")

    @task(1)
    def bootstrap_dashboard(self):
        self.client.get("/bootstrap-dashboard")

    @task(1)
    def caching_example(self):
        self.client.get("/caching-example")

    @task(1)
    def custom_bokeh_model(self):
        self.client.get("/custom-bokeh-model")

    @task(1)
    def classic_dashboard(self):
        self.client.get("/classic-dashboard")

    @task(1)
    def data_explorer_loading(self):
        self.client.get("/data-explorer-loading")

    @task(1)
    def de_tr_object_detection(self):
        self.client.get("/detr")

    @task(1)
    def dependent_widgets(self):
        self.client.get("/dependent-widgets")

    @task(1)
    def google_map_viewer(self):
        self.client.get("/google-map-viewer")

    @task(1)
    def fast_grid_template(self):
        self.client.get("/fast-grid-template")

    @task(1)
    def gallery(self):
        self.client.get("/gallery")

    @task(1)
    def awesome_panel(self):
        self.client.get("/")

    @task(1)
    def image_classifier(self):
        self.client.get("/image-classifier")

    @task(1)
    def js_actions(self):
        self.client.get("/js-actions")

    @task(1)
    def kickstarter_dashboard(self):
        self.client.get("/kick-starter-dashboard")

    @task(1)
    def loading_spinners(self):
        self.client.get("/loading-spinners")

    @task(1)
    def pandas_profiling(self):
        self.client.get("/pandas-profiling")

    @task(1)
    def param_reference_example(self):
        self.client.get("/param-reference")

    @task(1)
    def awesome_list(self):
        self.client.get("/awesome-list")

    @task(1)
    def shoelace(self):
        self.client.get("/shoelace")

    @task(1)
    def streaming_dashboard(self):
        self.client.get("/streaming-dashboard")

    @task(1)
    def streaming_plots(self):
        self.client.get("/streaming-plots")

    @task(1)
    def fileinput_area(self):
        self.client.get("/fileinput-area")

    @task(1)
    def volume_profile_analysis(self):
        self.client.get("/volume-profile-analysis")

    @task(1)
    def highcharts_network(self):
        self.client.get("/highcharts-network")

    # @task(1)
    # def yahoo_query(self):
    #     self.client.get("/yahoo-query")

    def on_start(self):
        pass
