# Issues Experienced During Development of this Project

Let me start out by saying that I think that **Panel is very, very powerfull and usefull**.

But there still are some rough edges its nice to know about. By discussing them here I hope to give you an impression of the current issues and rough edges of developing a multipage application in Panel.

I also hope the issues will get attention by the community (including me) and be solved to lower the friction of create awesome analytical apps in Panel.

You can find an overview of all my open and closed issues + feature requests via

- [Open Issues](https://github.com/holoviz/panel/issues?q=author%3AMarcSkovMadsen+is%3Aopen).
- [Closed Issues](https://github.com/holoviz/panel/issues?q=author%3AMarcSkovMadsen+is%3Aclosed)
- [Open PRs](https://github.com/holoviz/panel/pulls/MarcSkovMadsen)
- [Closed PRs](https://github.com/holoviz/panel/pulls?q=is%3Apr+author%3AMarcSkovMadsen+is%3Aclosed)

## The Bokeh Layout Engine is not always your friend

- The Bokeh layout engine can work against you when you try to create advanced layouts. Things do not perform or render as expected.

To circumvent these issues my most important learning is to **KEEP IT SIMPLE STUPID!**. Read my small tips and tricks for creating performance Panel apps [here](https://awesome-panel.readthedocs.io/en/latest/performance.html)

## Markdown is not always well supported

See

- A simple layout with a column and 2 markdown panes displays on top of each other [Issue 835](https://github.com/holoviz/panel/issues/835).
    - If there is a large image in the markdown the page is not rendered correctly. The Bokeh layout engine does not get the height and width correctly.
- Wide Images can overflow. Would be nice if `max-width: 100%` was set by default.

## Rough edges for being a first mover

I believe I experience some rough edges for being one of the first to create a multipage app in Panel with markdown (with images and code). For example

For examle sometimes I get error messages like this

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

![Info Alert Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/src/pages/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)

But I also struggle with it on this Limitations page. It's like the big image just above confuses the rendering. The workaround is to set `img {max-width: 100%}` in the css.

## Font Awesome Icons Cannot Easily be Used

Icons like fontawesome icons are not supported in Buttons.

I needed Buttons with Icons for my navigation which cannot use the Bootstrap `<a class="nav-link" href="#">`.

I cannot navigate in my single page app using urls. That is not supported

I could develop a multi page app that Panel serves via urls. But then I would loose my application state when navigating between pages.

BUT. I FOUND A WAY TO IMPLEMENT IT MY SELF.

## Hot reload is slow and slows down development-test cycle

See [issue 849](https://github.com/holoviz/panel/issues/849). I've developed the Awesome Panel Designer to circumvent this. See [Awesome Panel Designer](https://discourse.holoviz.org/t/awesome-panel-designer/643).)

## There is no Browser Location widget

There is no functionality or Widget in Panel to use the Browser and  URLs like `example.com/page1/?year=1976` for navigation, bookmarking and sharing links.

I would like to be able to keep the server app state in sync with the client app state via the browser url. I.e.

- If the user/ client navigates to a url my app state should be updated using the full url including parameters
- If I change my app state the parameters of my state should be available in the browser url for bookmarking and sharing.

The Location component has been merged into master but not yet released. See [PR 1150](https://github.com/holoviz/panel/pull/1150).

<br/><br/><br/>