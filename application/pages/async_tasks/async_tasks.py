"""When creating awesome analytics apps you sometimes wants to run jobs in the background or provide
streaming analytics to your users.

Panel also supports these use cases as its running on top of the asynchronous web server Tornado.

Below we show case how to start a background thread that updates a progressbar while
the rest of the application remains responsive.

This example is based on the discussion [Can I load data asynchronously in Panel?]\
(https://discourse.holoviz.org/t/can-i-load-data-asynchronously-in-panel/452).

If you really deep dive into this, then you can study
[tornado.ioloop.IOLoop](https://www.tornadoweb.org/en/stable/ioloop.html),
[concurrent.futures.ThreadPoolExecutor]\
(https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor),
[Panel.io.server.unlocked](https://panel.holoviz.org/api/panel.io.html#panel.io.server.unlocked)"""

import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

import numpy as np
import panel as pn
import param
from panel.io.server import unlocked
from tornado.ioloop import IOLoop

from awesome_panel_extensions.site import site

APPLICATION = site.create_application(
    url="async-tasks",
    name="Async Tasks",
    author="Jochem Smit",
    description="Demonstrates the use of asynchronous, background processes with Panel",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/async_tasks.png",
    resources={
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/async_tasks/async_tasks.py",
        "gif": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/async_tasks.gif",
        "mp4": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/async_tasks.mp4",
    },
    tags=[
        "Async",
    ],
)


class ProgressExtMod(param.Parameterized):
    """
    adaptation of: https://github.com/MarcSkovMadsen/awesome-panel/blob/master/\
package/awesome_panel/express/widgets/progress_ext.py
    """

    completed = param.Integer(default=0)
    bar_color = param.String(default="info")
    num_tasks = param.Integer(default=100, bounds=(1, None))

    # @param.depends('completed', 'num_tasks')
    @property
    def value(self) -> int:
        """Returs the progress value

        Returns:
            int: The progress value
        """
        return int(100 * (self.completed / self.num_tasks))

    def reset(self):
        """Resets the value and message"""
        # Please note the order matters as the Widgets updates two times. One for each change
        self.completed = 0

    @param.depends("completed", "message", "bar_color")
    def view(self):
        """View the widget
        Returns:
            pn.viewable.Viewable: Add this to your app to see the progress reported
        """
        if self.value:
            return pn.widgets.Progress(active=True, value=self.value, align="center")
        return None

    @contextmanager
    def increment(self):
        """Increment the value
        Can be used as context manager or decorator?
        Yields:
            None: Nothing is yielded
        """
        self.completed += 1
        yield
        if self.completed == self.num_tasks:
            self.reset()


executor = ThreadPoolExecutor(max_workers=2)  # pylint: disable=consider-using-with
progress = ProgressExtMod()


class AsyncApp(param.Parameterized):
    """An App that demonstrates how to setup use an asynchronous background task in Panel"""

    select = param.Selector(objects=range(10))
    slider = param.Number(2, bounds=(0, 10))
    text = param.String()

    do_stuff = param.Action(lambda self: self.do_calc(), label="START")
    result = param.Number(0)
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        pn.config.sizing_mode = "stretch_width"

        app = pn.Column(
            pn.pane.Markdown("## Background Task"),
            pn.Param(
                self,
                parameters=["do_stuff", "result"],
                widgets={"result": {"disabled": True}, "do_stuff": {"button_type": "primary"}},
                show_name=False,
            ),
            progress.view,
            pn.pane.Markdown("## Other Tasks"),
            pn.Param(
                self,
                parameters=["select", "slider", "text"],
                widgets={"text": {"disabled": True}},
                show_name=False,
            ),
        )
        main = [APPLICATION.intro_section(), app]

        self.view = pn.template.FastListTemplate(
            main=main,
            main_max_width="700px",
        )

    @param.depends("slider", "select", watch=True)
    def _on_slider_change(self):
        # This functions does some other python code which we want to keep responsive
        if self.select:
            select = self.select
        else:
            select = 0
        self.text = str(self.slider + select)

    def do_calc(self, num_tasks=10):
        """Runs background tasks num_tasks times"""
        num_tasks = 20
        progress.num_tasks = num_tasks
        loop = IOLoop.current()
        for _ in range(num_tasks):
            future = executor.submit(self._blocking_task)
            loop.add_future(future, self._update)

    @progress.increment()
    def _update(self, future):
        number = future.result()
        with unlocked():
            self.result += number

    @staticmethod
    def _blocking_task():
        time.sleep(np.random.randint(1, 2))
        return 5


@site.add(APPLICATION)
def view() -> pn.Column:
    """A view of the AsyncApp.

    Used by awesome-panel.org to display the app as a page in the application.

    Returns:
        pn.Column: The view of the AsyncApp
    """
    return AsyncApp().view


if __name__.startswith("bokeh"):
    view().servable()  # pylint: disable=no-value-for-parameter
