# run: locust -f 'tests\performance\locust_test.py'
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(3)
    def home(self):
        self.client.get("/")

    @task(1)
    def view_items(self):
        self.client.get("/holoviews-linked-brushing")

    def on_start(self):
        pass