# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
"""In this module we provide functionality to serve the Site

We provide some basic settings for `panel.serve` below. They might need tweeking to support your
use case.

For more info refer to the [README](README.md) and the section on Deployment.
"""
import os
import platform

import panel as pn

from src.shared import config, modifications

modifications.apply()


def serve():
    """Serves the site

    Use the configuration files together with the
    [BOKEH environment variables]\
    (https://docs.bokeh.org/en/latest/docs/reference/settings.html#bokeh-settings) to configure
    your site and how its served.
    """
    address = os.getenv("BOKEH_ADDRESS", "localhost")
    if platform.system() == "Windows":
        pn.serve(
            config.routes,
            port=5007,
            dev=False,
            title=config.site_name,
            address=address,
            static_dirs=config.static_dirs,
        )
    else:
        pn.serve(
            config.routes,
            port=5007,
            dev=False,
            title=config.site_name,
            address=address,
            num_procs=4,
            static_dirs=config.static_dirs,
        )


if __name__ == "__main__":
    serve()
