The Awesome Panel Extensions Guide
==================================

Maybe your code base has started to grow and you start to think about how you can refactor your it into smaller reusable components or extensions. For example like this user who asks `How to create a self-contained custom Panel? <https://discourse.holoviz.org/t/how-to-create-a-self-contained-custom-panel/985>`_.

Maybe you have started wondering how you can share your extensions with your team? Or maybe even with the Panel community?

Or maybe you are a part of an open source project or company wondering how you can give Panel users easy access to your package, tool or solution in order to increase the usage?

This guide answers your questions. It provides material for developing, testing and deploying
**your own Awesome Panel Extensions**.

Overview
--------

The table below summarizes the types of extensions that Panel supports.

+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| Extension Type            | Communication | Datasets | Wrap External JS library | Skill level* (You can do it 💪)                      |
+===========================+===============+==========+==========================+======================================================+
| Inheritence Extension     |               |          |                          |                                                      |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| \- Pane                   |               |          |                          |                                                      |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| * HTML                    | One way       | Small    | Yes                      | Basic HTML, CSS and/ or JS                           |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| * Markdown                | One way       | Small    | Yes                      | Markdown                                             |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| * WebComponent            | Bidirectional | Large    | Yes                      | Basic HTML, CSS and/ or JS                           |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| * Templates               |               |          |                          | Jinja, Basic HTML, CSS and/ or JS                    |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| \- Layout                 | Bidirectional | Large    | Normally No              | Panel                                                |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| View Extension            |               |          |                          | Same as Inheritance Extensions                       |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| Bokeh Extension           | Bidirectional | Large    | Yes                      | JS and Typescript                                    |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| IPyWidget Extension       | Bidirectional | Large    | Yes                      | IPyWidget, JS                                        |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+

**Inheritence Extensions** are extensions that are created by inheriting
from an existing layout, pane or widget. Please note that the extension created is often a widget even though its created by inheriting from a layout or pane. Inheritance Extensions are a bit more difficult to develop than View extensions because you need to be a bit more carefull when you inherit. See the detailed guides for more info.

- An important sub category of Inheritence Extensions is called **HTML Extensions**. You create these when you inherit from the `HTML` pane. You can use HTML, CSS and/ or JS to create amazing extensions to Panel. Often the resulting extension works as a widget and not as a pane. The **HTML extensions** cannot communicate from the browser (Javascript) back to the server (Python). The extension developed is often a widget and not a pane.

- Another important sub category of inheritence extensions is called **Layout Extensions**. These extensions are created by inheriting from a Layout and filling it with panes, layouts and widgets. The extension developed is often a widget and not a layout.

- An upcoming, important category of Inheritance Extensions are called **Web Component Extensions**. The `WebComponent` is essentially a `HTML` pane that supports bidirectional communication. It will provide you with the super powers of the Bokeh Extensions below for 80% of your use cases. But they require a minimum of javascript skills and are faster to develop.

**View Extensions** are developed almost in the same way as **Inheritance Extensions**. Their api is different though. You use `ViewExtension().view` to view a View Extension. View extensions are less quirky to develop and a bit more quirky to use compared to Inheritance Extensions.

**Bokeh Extensions** supports efficient, bidirectional
communication from server (Python) to the browser (Javascript) and back.
It also gives you access to develop using all the super powers of modern front end
framework languages (js or typescript), tooling and frameworks (React, Vue and Angular). The layouts, panes and widgets that ships with Panel are Bokeh extensions.

**IPyWidgets Extensions**. The `upcoming`_ IPyWidget Pane enables users
to use IPyWidgets in Panel. Therefore a developer might develop a Panel
extension as an IPyWidget. This might come at a performance
cost in relation to bundle size and general performance. If this matters
in practice is yet to be confirmed.

.. toctree::
   :maxdepth: 1
   :caption: Detailed Guides and Resources

   HTML Extensions <html-extensions.md>
   Markdown Extensions <markdown-extensions.md>
   Layout Extensions <layout-extensions.md>
   WebComponent Extensions <webcomponent-extensions.md>
   View Extensions <view-extensions.md>
   Bokeh Extensions <bokeh-extensions.md>
   Sharing Extensions <sharing.md>
   Other <other.md>

.. _upcoming: https://github.com/holoviz/panel/blob/master/panel/pane/ipywidget.py