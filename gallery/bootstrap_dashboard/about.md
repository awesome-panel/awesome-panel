# About

The purpose of this app is to demonstrate that a Dashboard Layout very similar to the [bootstrap dashboard template](https://getbootstrap.com/docs/4.3/examples/dashboard/) from [getboostrap.com](https://getbootstrap.com/) can be implemented in [Panel](https://panel.pyviz.org/).

![GetBootstrap Dashboard Template](https://getbootstrap.com/docs/4.4/assets/img/examples/dashboard.png)

## Current Limitations

- It's difficult to use a framework like Bootstrap together with the framework of Panel which builds on Bokeh.
  - The javascript handling responsive layouts in Bootstrap and Bokeh does not play well.
    - For example the Bootstrap sidebar automatically adjusts it's width if I change the window size but the Bokeh Buttons do not respond to this change.
  - It's difficult to wrap Panel Panes and Widgets into Bootstrap components like cards as "component templating" is not supported. See [Issue 810](https://github.com/holoviz/panel/issues/810)
- I cannot get fontawesome icons into the buttons. I needed this for my navigation which cannot use the Bootstrap `<a class="nav-link" href="#">`.
I cannot use it because I cannot navigate by links in my app.
- Plotly is not yet responsive in Panel. See [Issue 822](https://github.com/holoviz/panel/issues/822)
- Panes and Widgets are not configured to be responsive by default. I always have to set `sizing_policy="stretch_width"`.