## Custom CSS does not play nicely with Bokeh HTML, CSS and Javascipt

I've experienced numerous problems when using css.

I have a feeling that the Bokeh Javascript on elements does not take everything like images and inline css into account. But it's difficult for me to catch and understand.

For example I struggled with the below scrollbar until I found out it was because i had a `margin-bottom: 1rem;` in the css for the info box. When I removed that the problem was solved.

![Info Alert Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)