import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

import numpy as np
import panel as pn
import param
from asyncio import wrap_future

class ProgressExtMod(pn.viewable.Viewer):
    """A custom component for easy progress reporting"""

    completed = param.Integer(default=0)
    bar_color = param.String(default="info")
    num_tasks = param.Integer(default=100, bounds=(1, None))

    # @param.depends('completed', 'num_tasks')
    @property
    def value(self) -> int:
        """Returns the progress value

        Returns:
            int: The progress value
        """
        return int(100 * (self.completed / self.num_tasks))

    def reset(self):
        """Resets the value and message"""
        # Please note the order matters as the Widgets updates two times. One for each change
        self.completed = 0

    def __panel__(self):
        return self.view

    @param.depends("completed", "bar_color")
    def view(self):
        """View the widget
        Returns:
            pn.viewable.Viewable: Add this to your app to see the progress reported
        """
        if self.value:
            return pn.widgets.Progress(
                active=True, value=self.value, align="center", sizing_mode="stretch_width"
            )
        return None

    @contextmanager
    def increment(self):
        """Increments the value
        
        Can be used as context manager or decorator
        
        Yields:
            None: Nothing is yielded
        """
        self.completed += 1
        yield
        if self.completed == self.num_tasks:
            self.reset()

executor = ThreadPoolExecutor(max_workers=2)  # pylint: disable=consider-using-with
progress = ProgressExtMod()


class AsyncComponent(pn.viewable.Viewer):
    """A component that demonstrates how to run a Blocking Background task asynchronously
    in Panel"""

    select = param.Selector(objects=range(10))
    slider = param.Number(2, bounds=(0, 10))
    
    run_blocking_task = param.Event(label="RUN")
    result = param.Number(0)
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self._layout = pn.Column(
            pn.pane.Markdown("## Blocking Task Running in Background"),
            pn.Param(
                self,
                parameters=["run_blocking_task", "result"],
                widgets={"result": {"disabled": True}, "run_blocking_task": {"button_type": "primary"}},
                show_name=False,
            ),
            progress,
            pn.pane.Markdown("## Other, Non-Blocked Tasks"),
            pn.Param(
                self,
                parameters=["select", "slider"],
                widgets={"text": {"disabled": True}},
                show_name=False,
            ),
            self.text
        )

    def __panel__(self):
        return self._layout

    @param.depends("slider", "select")
    def text(self):
        if self.select:
            select = self.select
        else:
            select = 0
        return f"{select} + {self.slider} = {select + self.slider}"

    @pn.depends("run_blocking_task", watch=True)
    async def _run_blocking_tasks(self, num_tasks=10):
        """Runs background tasks num_tasks times"""
        num_tasks = 20
        progress.num_tasks = num_tasks
        for _ in range(num_tasks):
            future = executor.submit(self._run_blocking_task)
            result = await wrap_future(future)
            self._update(result)

    @progress.increment()
    def _update(self, number):
        self.result += number

    @staticmethod
    def _run_blocking_task():
        time.sleep(np.random.randint(1, 2))
        return 5

if pn.state.served:
    pn.extension()
    
    component = AsyncComponent()
    pn.template.FastListTemplate(
        site="Awesome Panel", site_url="https://awesome-panel.org", title="Async Tasks", main=[component], main_layout=None, main_max_width="400px"
    ).servable()
