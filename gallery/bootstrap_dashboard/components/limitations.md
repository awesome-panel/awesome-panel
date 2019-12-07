# Limitations of Panel

Let me start out by saying that I think that Panel is already very powerfull. But I have experienced som limitations and rough edges.

## Community and Documentation is difficult to use

See GitHub issues

- Create Discuss Forum to foster community discussions and knowledge sharing on Panel. [Issue 831](https://github.com/holoviz/panel/issues/831)
- Change search functionality at [https://panel.pyviz.org/](https://panel.pyviz.org/) to return Panel specific results. [Issue 832](https://github.com/holoviz/panel/issues/832)
- Please add more structure, search, navigation and content to Panel Documentation. [Issue 833](https://github.com/holoviz/panel/issues/833)
- Make Panel help text readable on Windows in Command Prompt and Git bash. [Issue 836](https://github.com/holoviz/panel/issues/836)
- Please add the wonderfull help text to the docstrings to get context help in editor. [Issue 837](https://github.com/holoviz/panel/issues/837)

## Markdown is not well supported

See

- Support rendering of indented markdown. [Issue 828](https://github.com/holoviz/panel/issues/828).
- A simple layout with a column and 2 markdown panes displays on top of each other [Issue 835](https://github.com/holoviz/panel/issues/835).
    - If there is a large image in the markdown the page is not rendered correctly. The Bokeh layout engine does not get the height and width correctly.
- No Code syntax highlighting. [Issue 391](https://github.com/holoviz/panel/issues/391)
- Wide Images can overflow. Would be nice if `max-width: 100%` was set by default.
- Cannot get full width widthout lots of empty space at bottom. [Issue 848](https://github.com/holoviz/panel/issues/848)

## Plotly Plots are not well supported

- Plotly is not yet responsive in Panel. See [Issue 822](https://github.com/holoviz/panel/issues/822)

## Hot reload is slow and slows down development-test cycle

See [issue 849](https://github.com/holoviz/panel/issues/849)

## Panels, Panes and Widgets are not full width, responsive by default

Panes and Widgets are not configured to be full width, responsive by default. I always have to set `sizing_policy="stretch_width"`. This is just overhead and friction.

## Rough edges for being a first mover

I believe I experience some rough edges for being one of the first to create a multipage app in Panel with markdown (with images and code). For example

- DataFrame widget raises exception if two columns have the same names. See [Issue 821](https://github.com/holoviz/panel/issues/821).
- Sizing_mode="stretch_width" does not work for DataFrame panes. See [Issue 823](https://github.com/holoviz/panel/issues/823)
- Cannot dynamically add and remove panes [Issue 838](https://github.com/holoviz/panel/issues/838)
- Images does not support src urls and alt texts [Issue 841](https://github.com/holoviz/panel/issues/841)
- Plotly does not show when dynamically adding and removing pages without adding plotly extension. See [Issue 840](https://github.com/holoviz/panel/issues/840)

and I sometimes get error messages like this

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

I've been told I can ignore these as they don't matter.

## Bootstrap CSS and Javascript does not play nicely with Bokeh HTML, CSS and Javascript

It's difficult to use a framework like Bootstrap together with Panel which builds on Bokeh. I gave up on it and switched to pure Panel with custom CSS.

- The javascript handling responsive layouts in Bootstrap and Bokeh does not play well.
    - For example the Bootstrap sidebar automatically adjusts it's width if I change the window size but the Bokeh Buttons do not respond to this change.
- It's difficult to wrap Panel Panes and Widgets into Bootstrap components like cards as "component templating" is not supported. See [Issue 810](https://github.com/holoviz/panel/issues/810)

## Custom CSS does not play nicely with Bokeh HTML, CSS and Javascript

I've experienced numerous problems when using css.

I have a feeling that the Bokeh Javascript on elements does not take everything like images and inline css into account. But it's difficult for me to catch and understand.

For example I struggled with the below scrollbar until I found out it was because i had a `margin-bottom: 1rem;` in the css for the info box. When I removed that the problem was solved.

![Info Alert Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)

But I also struggle with it on this Limitations page. It's like the big image just above confuses the rendering. The workaround is to set `img {max-width: 100%}` in the css.

## Font Awesome Icons Cannot Easily be Used

Icons like fontawesome icons are not supported in Buttons.

I needed Buttons with Icons for my navigation which cannot use the Bootstrap `<a class="nav-link" href="#">`.

I cannot navigate in my single page app using urls. That is not supported

I could develop a multi page app that Panel serves via urls. But then I would loose my application state when navigating between pages.

BUT. I FOUND A WAY TO IMPLEMENT IT MY SELF.

## There is no Browser URL widget

There is not functionality or Widget in Panel to use the Browser and  URLs like `example.com/page1/?year=1976` for navigation, bookmarking and sharing links. See [issue 811](https://github.com/holoviz/panel/issues/811).

I would like to be able to keep the server app state in sync with the client app state via the browser url. I.e.

- If the user/ client navigates to a url my app state should be updated using the full url including parameters
- If I change my app state the parameters of my state should be available in the browser url for bookmarking and sharing.

## I Could not get independt scrollbars working

I would have liked the sidebar and content sections to have independent vertical scrollbars that only show up if needed. I could not get that working. I guess it's just my CSS skills that are too poor.