# Current Limitations

- It's difficult to use a framework like Bootstrap together with Panel which builds on Bokeh.
    - The javascript handling responsive layouts in Bootstrap and Bokeh does not play well.
        - For example the Bootstrap sidebar automatically adjusts it's width if I change the window size but the Bokeh Buttons do not respond to this change.
    - It's difficult to wrap Panel Panes and Widgets into Bootstrap components like cards as "component templating" is not supported. See [Issue 810](https://github.com/holoviz/panel/issues/810)
- I cannot get fontawesome icons into the buttons. I needed this for my navigation which cannot use the Bootstrap `<a class="nav-link" href="#">`.
I cannot use it because I cannot navigate by links in my app.
    - Plotly is not yet responsive in Panel. See [Issue 822](https://github.com/holoviz/panel/issues/822)
    - Panes and Widgets are not configured to be responsive by default. I always have to set `sizing_policy="stretch_width"`.

## CSS Issues

I've experienced numerous problems when using css.

I have a feeling that the Bokeh Javascript on elements does not take everything like images and inline css into account. But it's difficult for me to catch and understand.

For example I struggled with the below scrollbar until I found out it was because i had a `margin-bottom: 1rem;` in the css for the info box. When I removed that the problem was solved.

![Info Alert Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)