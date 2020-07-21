The Awesome Panel Extensions Guide
==================================

This guide provides material for developing, testing and deploying
**your own Awesome Panel Extensions**.

Overview
--------

The table below summarizes the types of extensions that Panel supports.

+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| Extension Type            | Communication | Datasets | Wrap External JS library | Skill level* (You can do it 💪)                      |
+===========================+===============+==========+==========================+======================================================+
| Inheritence Extension     |               |          |                          |                                                      |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| \- HTML Extension         | One way       | Small    | Yes                      | Basic HTML, CSS and/ or JS                           |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| \- Composed Extension     | Bidirectional | Large    | Normally No              | Panel                                                |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| \- WebComponent Extension | Bidirectional | Large    | Yes                      | Basic HTML, CSS and/ or JS                           |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| Bokeh Extension           | Bidirectional | Large    | Yes                      | JS and Typescript                                    |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+
| IPyWidget Extension       | Bidirectional | Large    | Yes                      | IPyWidget, JS                                        |
+---------------------------+---------------+----------+--------------------------+------------------------------------------------------+

**Inheritence Extensions** are extensions that are created by inheriting
from an existing layout, pane or widget.

- An important sub category of Inheritence Extensions are called **HTML Extensions**. These extensions are created by inheriting from the ``HTML`` pane. You can use HTML, CSS and/ or JS to create amazing extensions to Panel. These extensions cannot communicate from the browser (Javascript) back to the server (Python).

- Another important sub category of inheritence extensions is called **Composed Extensions**. These extensions are created by composing existing Panel components in a layout.

- An upcoming, important sub category of Inheritance Extensions are called **Web Component Extensions**. They are essentially a more advanced `HTML` pane that supports bidirectional communication. They will provide you with the super powers of the Bokeh Extensions below for 80% of your use cases. But they require a minimum of javascript skills and are faster to develop.

**Bokeh Extensions** on the other hand supports efficient, bidirectional
communication from server (Python) to the browser (Javascript) and back.
It also gives you access to all the super powers of modern front end
framework languages (js or typescript), tooling and frameworks like
React, Vue and Angular. The layouts, panes and widgets that ships with
Panel are Bokeh extensions.

**IPyWidgets Extensions**. The `upcoming`_ IPyWidget Pane enables users
to use IPyWidgets in Panel. Therefore a developer might develop a Panel
extension as an IPyWidget. This might come at a performance
cost in relation to bundle size and general performance. If this matters
in practice is yet to be confirmed.

For more see

.. toctree::
   :maxdepth: 1
   :caption: Examples and Resources

   Bokeh Extensions <bokeh-extensions.md>
   Composed Extensions <composed-extensions.md>
   HTML Extensions <html-extensions.md>
   Sharing <sharing.md>


.. _upcoming: https://github.com/holoviz/panel/blob/master/panel/pane/ipywidget.py