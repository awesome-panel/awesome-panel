# Sharing Panel Extensions

You can share your awesome Panel extension(s) in the following ways

- Share working code examples with screenshots on [HoloViz Discourse](https://discourse.holoviz.org/).
- Contribute as a notebook to the [Panel Gallery](https://panel.holoviz.org/gallery/index.html).
- Contribute as code to the [Panel Repository](https://github.com/holoviz/panel).
- Distribute as a Python package PyPi, Conda or similar.
- Share as a blog post on [Medium](https://medium.com/) or similar
- Share as a repository on GitHub or similar.
- Share on social media like [Twitter](https://twitter.com/home), [LinkedIn](https://www.linkedin.com/feed/) or similar.
- Contribute it to the Gallery at [awesome-panel.org](https://awesome-panel.org) or the [awesome-panel-extensions](https://github.com/MarcSkovMadsen/awesome-panel-extensions) package.

You contributions matter. Thanks. 👍

## Distributing Your Extension on PyPi

Sharing one or more extensions as a package on [PyPi](https://pypi.org/) requires packaging your Python project as you would do for any other Python project.

The [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) guide describes this.

You can also study the [Awesome Panel Extensions Repository](https://github.com/marcskovmadsen/awesome-panel-extensions) to see how a specific Panel Extensions Package is set up. You can find the `awesome-panel-extensions` package on PyPi [here](https://pypi.org/project/awesome-panel-extensions/).

If your extension contains Bokeh extensions, you have to make sure your bokeh `bokeh.ext.json` and your build `dist`files are shipped with your package.

- In [setup.py](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/setup.py) you need to set `include_package_data=True` to enable the use of a `Manifest.in` file.
- Your [Manifest.in](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/Manifest.in) file then needs to include something like

```bash
include awesome_panel_extensions/*.json
include awesome_panel_extensions/index.ts
include awesome_panel_extensions/bokeh_extensions/*.ts
graft awesome_panel_extensions/dist
```

## Contributing Your Extension to Panel

It's as easy as suggesting it as a Feature Request or providing it as a Pull request on the [Panel Github site](https://github.com/holoviz/panel).

For more information on getting started as **Panel Developer** see the [Panel Developer Guide](https://panel.holoviz.org/developer_guide/index.html).