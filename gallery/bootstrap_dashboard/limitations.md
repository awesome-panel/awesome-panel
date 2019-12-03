# Current Limitations

## Bootstrap CSS and Javascript does not play nicely with Bokeh HTML, CSS and Javascript

It's difficult to use a framework like Bootstrap together with Panel which builds on Bokeh. I gave up on it and switched to pure Panel with custom CSS.

- The javascript handling responsive layouts in Bootstrap and Bokeh does not play well.
    - For example the Bootstrap sidebar automatically adjusts it's width if I change the window size but the Bokeh Buttons do not respond to this change.
- It's difficult to wrap Panel Panes and Widgets into Bootstrap components like cards as "component templating" is not supported. See [Issue 810](https://github.com/holoviz/panel/issues/810)

## Font Awesome Icons Cannot Easily be Used

Icons like fontawesome icons are not supporteded out of the box.

I needed this for my navigation which cannot use the Bootstrap `<a class="nav-link" href="#">`. But I cannot navigate in my app using urls.

## Plotly Plots are not Responsive

- Plotly is not yet responsive in Panel. See [Issue 822](https://github.com/holoviz/panel/issues/822)

## Plotly Plots create other issues

I have a plotly view where the code is close to a copy paste of the holoviews view. But it raises the below errors

```bash
2019-12-03 09:34:57,514 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:57,517 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,055 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,058 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,061 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,065 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,070 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,073 Cannot apply patch to 1291 which is not in the document anymore
```

## Panels, Panes and Widgets are not full width, responsive by default

Panes and Widgets are not configured to be responsive by default. I always have to set `sizing_policy="stretch_width"`. This is just overhead and friction.

## Custom CSS does not play nicely with Bokeh HTML, CSS and Javascipt

I've experienced numerous problems when using css.

I have a feeling that the Bokeh Javascript on elements does not take everything like images and inline css into account. But it's difficult for me to catch and understand.

For example I struggled with the below scrollbar until I found out it was because i had a `margin-bottom: 1rem;` in the css for the info box. When I removed that the problem was solved.

![Info Alert Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)

But I also struggle with it on this Limitations page. It's like the big image just above confuses the rendering.

![Limitations Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/limitations_page_scrollbar_problem.png?raw=true)

## I Could not get independt scrollbars working

I would have liked the sidebar and content sections to have independent vertical scrollbars that only show up if needed. I could not get that working. I guess it's just my CSS skills that are too poor.
