"""This module provides various modifies the Panel `get_server` function to enable the site to
serve .py and .ipynb files."""
# pylint: skip-file
from __future__ import absolute_import, division, unicode_literals

import pathlib
import signal
import sys
import uuid
from functools import partial

from bokeh.command.util import build_single_handler_application
from bokeh.server.server import Server
from panel.io.server import INDEX_HTML, ProxyFallbackHandler, _eval_panel, get_static_routes
from panel.io.state import state
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer


def get_server(
    panel,
    port=0,
    address=None,
    websocket_origin=None,
    loop=None,
    show=False,
    start=False,
    title=None,
    verbose=False,
    location=True,
    static_dirs={},
    oauth_provider=None,
    oauth_key=None,
    oauth_secret=None,
    oauth_extra_params={},
    cookie_secret=None,
    oauth_encryption_key=None,
    **kwargs,
):
    """
    Returns a Server instance with this panel attached as the root
    app.

    Arguments
    ---------
    panel: Viewable, function or {str: Viewable}
      A Panel object, a function returning a Panel object or a
      dictionary mapping from the URL slug to either.
    port: int (optional, default=0)
      Allows specifying a specific port
    address : str
      The address the server should listen on for HTTP requests.
    websocket_origin: str or list(str) (optional)
      A list of hosts that can connect to the websocket.

      This is typically required when embedding a server app in
      an external web site.

      If None, "localhost" is used.
    loop : tornado.ioloop.IOLoop (optional, default=IOLoop.current())
      The tornado IOLoop to run the Server on.
    show : boolean (optional, default=False)
      Whether to open the server in a new browser tab on start.
    start : boolean(optional, default=False)
      Whether to start the Server.
    title : str or {str: str} (optional, default=None)
      An HTML title for the application or a dictionary mapping
      from the URL slug to a customized title.
    verbose: boolean (optional, default=False)
      Whether to report the address and port.
    location : boolean or panel.io.location.Location
      Whether to create a Location component to observe and
      set the URL location.
    static_dirs: dict (optional, default={})
      A dictionary of routes and local paths to serve as static file
      directories on those routes.
    oauth_provider: str
      One of the available OAuth providers
    oauth_key: str (optional, default=None)
      The public OAuth identifier
    oauth_secret: str (optional, default=None)
      The client secret for the OAuth provider
    oauth_extra_params: dict (optional, default={})
      Additional information for the OAuth provider
    cookie_secret: str (optional, default=None)
      A random secret string to sign cookies (required for OAuth)
    oauth_encryption_key: str (optional, default=False)
      A random encryption key used for encrypting OAuth user
      information and access tokens.
    kwargs: dict
      Additional keyword arguments to pass to Server instance.

    Returns
    -------
    server : bokeh.server.server.Server
      Bokeh Server instance running this panel
    """
    server_id = kwargs.pop("server_id", uuid.uuid4().hex)
    kwargs["extra_patterns"] = extra_patterns = kwargs.get("extra_patterns", [])
    if isinstance(panel, dict):
        apps = {}
        for slug, app in panel.items():
            if isinstance(title, dict):
                try:
                    title_ = title[slug]
                except KeyError:
                    raise KeyError(
                        "Keys of the title dictionnary and of the apps "
                        f"dictionary must match. No {slug} key found in the "
                        "title dictionnary."
                    )
            else:
                title_ = title
            slug = slug if slug.startswith("/") else "/" + slug
            if "flask" in sys.modules:
                from flask import Flask

                if isinstance(app, Flask):
                    wsgi = WSGIContainer(app)
                    if slug == "/":
                        raise ValueError("Flask apps must be served on a subpath.")
                    if not slug.endswith("/"):
                        slug += "/"
                    extra_patterns.append(
                        ("^" + slug + ".*", ProxyFallbackHandler, dict(fallback=wsgi, proxy=slug))
                    )
                    continue
            if isinstance(app, pathlib.Path):
                app = str(app)
            if isinstance(app, str) and (app.endswith(".py") or app.endswith(".ipynb")):
                apps[slug] = build_single_handler_application(app)
            else:
                apps[slug] = partial(_eval_panel, app, server_id, title_, location)
    else:
        apps = {"/": partial(_eval_panel, panel, server_id, title, location)}

    extra_patterns += get_static_routes(static_dirs)

    opts = dict(kwargs)
    if loop:
        loop.make_current()
        opts["io_loop"] = loop
    elif opts.get("num_procs", 1) == 1:
        opts["io_loop"] = IOLoop.current()

    if "index" not in opts:
        opts["index"] = INDEX_HTML

    if address is not None:
        opts["address"] = address

    if websocket_origin:
        if not isinstance(websocket_origin, list):
            websocket_origin = [websocket_origin]
        opts["allow_websocket_origin"] = websocket_origin

    # Configure OAuth
    from panel.config import config

    if config.oauth_provider:
        from panel.auth import OAuthProvider

        opts["auth_provider"] = OAuthProvider()
    if oauth_provider:
        config.oauth_provider = oauth_provider
    if oauth_key:
        config.oauth_key = oauth_key
    if oauth_extra_params:
        config.oauth_extra_params = oauth_extra_params
    if cookie_secret:
        config.cookie_secret = cookie_secret
    opts["cookie_secret"] = config.cookie_secret

    server = Server(apps, port=port, **opts)
    if verbose:
        address = server.address or "localhost"
        print("Launching server at http://%s:%s" % (address, server.port))

    state._servers[server_id] = (server, panel, [])

    if show:

        def show_callback():
            server.show("/login" if config.oauth_provider else "/")

        server.io_loop.add_callback(show_callback)

    def sig_exit(*args, **kwargs):
        server.io_loop.add_callback_from_signal(do_stop)

    def do_stop(*args, **kwargs):
        server.io_loop.stop()

    try:
        signal.signal(signal.SIGINT, sig_exit)
    except ValueError:
        pass  # Can't use signal on a thread

    if start:
        server.start()
        try:
            server.io_loop.start()
        except RuntimeError:
            pass
    return server
