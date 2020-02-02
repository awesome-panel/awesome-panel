import textwrap

import panel as pn
from panel.pane import Markdown

wrap = textwrap


def view():
    output = """We test that

    - A "Header is shown"
    - The background is blue
    - The sizing_mode is "stretch_width" by default. DOES NOT WORK CURRENTLY
    """

    output1 = """We test that

    - A "Header is shown"
    - The background is blue
    - The sizing_mode is "stretch_width" by default. DOES NOT WORK CURRENTLY

    ```python
    def my_func(a):
        a +=1
    ```
    """

    output2 = """
    We test that

    - A "Header is shown"
    - The background is blue
    - The sizing_mode is "stretch_width" by default. DOES NOT WORK CURRENTLY

    ```python
    def my_func(a):
        a +=1
    ```
    """

    output3 = """\
    We test that

    - A "Header is shown"
    - The background is blue
    - The sizing_mode is "stretch_width" by default. DOES NOT WORK CURRENTLY

    ```python
    def my_func(a):
        a +=1
    ```
    """
    return pn.Column(
        pn.pane.Markdown(output),
        pn.layout.Divider(),
        pn.pane.Markdown(output1),
        pn.layout.Divider(),
        pn.pane.Markdown(output2),
        pn.layout.Divider(),
        pn.pane.Markdown(output3),
    )


view().servable()
