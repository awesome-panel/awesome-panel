"""When creating awesome analytics apps you sometimes wants to run jobs in the background or provide
streaming analytics to your users.

Panel also supports these use cases as its running on top of the asynchronous web server Tornado.

Below we show case how to start a background thread that updates a progressbar while
the rest of the application remains responsive.

This example is based on the discussion [Can I load data asynchronously in Panel?]\
(https://discourse.holoviz.org/t/can-i-load-data-asynchronously-in-panel/452).

If you really deep dive into this, then you can study
[tornado.ioloop.IOLoop](https://www.tornadoweb.org/en/stable/ioloop.html),
[concurrent.futures.ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor),
[Panel.io.server.unlocked](https://panel.holoviz.org/api/panel.io.html#panel.io.server.unlocked)"""

# **Authors:**
# [Jochem Smit](https://github.com/Jhsmit), [Marc Skov Madsen](https://github.com/MarcSkovMadsen)

# **Code:**
# [Code](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/\
# application/pages/async_tasks/async_tasks.py
# )

# **Resources:**
# [tornado.ioloop.IOLoop](https://www.tornadoweb.org/en/stable/ioloop.html),
# [concurrent.futures.ThreadPoolExecutor]\
# (https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor),
# [Panel.io.server.unlocked](https://panel.holoviz.org/api/panel.io.html#panel.io.server.unlocked)

# **Tags:**
# [Panel](https://panel.holoviz.org/), Async

import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

import numpy as np
import panel as pn
import param
from application.config import site
from panel.io.server import unlocked
from panel.template import VanillaTemplate
from tornado.ioloop import IOLoop

TITLE = "Async Tasks"


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


executor = ThreadPoolExecutor(max_workers=2)
progress = ProgressExtMod()


class AsyncApp(param.Parameterized):
    """An App that demonstrates how to setup use an asynchronous background task in Panel"""

    select = param.Selector(objects=range(10))
    slider = param.Number(2, bounds=(0, 10))
    text = param.String()

    do_stuff = param.Action(lambda self: self.do_calc())
    result = param.Number(0)
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        pn.config.sizing_mode = "stretch_width"

        intro_section = site.get_intro_section(TITLE)
        start_async_section = pn.Column(
            pn.pane.Markdown("## Starts async background tasks"),
            pn.Param(
                self,
                parameters=["do_stuff", "result"],
                widgets={"result": {"disabled": True}, "do_stuff": {"button_type": "success"}},
                show_name=False,
            ),
            progress.view,
        )
        working_section = pn.Column(
            pn.pane.Markdown("## Works while background tasks are running"),
            pn.Param(
                self,
                parameters=["select", "slider", "text"],
                widgets={"text": {"disabled": True}},
                show_name=False,
            ),
        )
        main = [intro_section, start_async_section, working_section]

        self.view = site.get_template(
            main=main,
            main_max_width = "700px",
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

@site.register(
    url="async-tasks",
    name=TITLE,
    author="Jochem Smit",
    description=__doc__,
    thumbnail_url="async_tasks.png",
    documentation_url="",
    code_url="async_tasks",
    gif_url="async_tasks.gif",
    mp4_url="async_tasks.mp4",
    tags=[
        "Code",
        "App In Gallery",
    ],
)
def view() -> pn.Column:
    """A view of the AsyncApp.

    Used by awesome-panel.org to display the app as a page in the application.

    Returns:
        pn.Column: The view of the AsyncApp
    """
    return AsyncApp().view


if __name__.startswith("bokeh"):
    view().servable()  # pylint: disable=no-value-for-parameter
