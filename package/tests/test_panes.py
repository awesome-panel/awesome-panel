"""Test of _pane.core functionality"""
import pytest
import awesome_panel.express as pnx
import panel as pn


@pytest.mark.panel
def test_divider():
    """## test_divider

A manual test of the horizontal divider stretching to full width"""
    app = pn.Column(
        pn.pane.Markdown(test_divider.__doc__), pnx.Divider(), sizing_mode="stretch_width"
    )
    app.servable(test_divider.__name__)


@pytest.mark.panel
def test_code():
    """## test_code

A manual test of the Code pane. We expect to see nicely formatted python code"""
    code = """\
def my_add(a,b):
    return a+b
"""
    css = """
.codehilite .hll { background-color: #ffffcc }
.codehilite  { background: #f8f8f8; }
.codehilite .c { color: #408080; font-style: italic } /* Comment */
.codehilite .err { border: 1px solid #FF0000 } /* Error */
.codehilite .k { color: #008000; font-weight: bold } /* Keyword */
.codehilite .o { color: #666666 } /* Operator */
.codehilite .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.codehilite .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.codehilite .cp { color: #BC7A00 } /* Comment.Preproc */
.codehilite .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.codehilite .c1 { color: #408080; font-style: italic } /* Comment.Single */
.codehilite .cs { color: #408080; font-style: italic } /* Comment.Special */
.codehilite .gd { color: #A00000 } /* Generic.Deleted */
.codehilite .ge { font-style: italic } /* Generic.Emph */
.codehilite .gr { color: #FF0000 } /* Generic.Error */
.codehilite .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.codehilite .gi { color: #00A000 } /* Generic.Inserted */
.codehilite .go { color: #888888 } /* Generic.Output */
.codehilite .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.codehilite .gs { font-weight: bold } /* Generic.Strong */
.codehilite .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.codehilite .gt { color: #0044DD } /* Generic.Traceback */
.codehilite .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.codehilite .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.codehilite .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.codehilite .kp { color: #008000 } /* Keyword.Pseudo */
.codehilite .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.codehilite .kt { color: #B00040 } /* Keyword.Type */
.codehilite .m { color: #666666 } /* Literal.Number */
.codehilite .s { color: #BA2121 } /* Literal.String */
.codehilite .na { color: #7D9029 } /* Name.Attribute */
.codehilite .nb { color: #008000 } /* Name.Builtin */
.codehilite .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.codehilite .no { color: #880000 } /* Name.Constant */
.codehilite .nd { color: #AA22FF } /* Name.Decorator */
.codehilite .ni { color: #999999; font-weight: bold } /* Name.Entity */
.codehilite .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.codehilite .nf { color: #0000FF } /* Name.Function */
.codehilite .nl { color: #A0A000 } /* Name.Label */
.codehilite .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.codehilite .nt { color: #008000; font-weight: bold } /* Name.Tag */
.codehilite .nv { color: #19177C } /* Name.Variable */
.codehilite .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.codehilite .w { color: #bbbbbb } /* Text.Whitespace */
.codehilite .mb { color: #666666 } /* Literal.Number.Bin */
.codehilite .mf { color: #666666 } /* Literal.Number.Float */
.codehilite .mh { color: #666666 } /* Literal.Number.Hex */
.codehilite .mi { color: #666666 } /* Literal.Number.Integer */
.codehilite .mo { color: #666666 } /* Literal.Number.Oct */
.codehilite .sa { color: #BA2121 } /* Literal.String.Affix */
.codehilite .sb { color: #BA2121 } /* Literal.String.Backtick */
.codehilite .sc { color: #BA2121 } /* Literal.String.Char */
.codehilite .dl { color: #BA2121 } /* Literal.String.Delimiter */
.codehilite .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.codehilite .s2 { color: #BA2121 } /* Literal.String.Double */
.codehilite .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.codehilite .sh { color: #BA2121 } /* Literal.String.Heredoc */
.codehilite .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.codehilite .sx { color: #008000 } /* Literal.String.Other */
.codehilite .sr { color: #BB6688 } /* Literal.String.Regex */
.codehilite .s1 { color: #BA2121 } /* Literal.String.Single */
.codehilite .ss { color: #19177C } /* Literal.String.Symbol */
.codehilite .bp { color: #008000 } /* Name.Builtin.Pseudo */
.codehilite .fm { color: #0000FF } /* Name.Function.Magic */
.codehilite .vc { color: #19177C } /* Name.Variable.Class */
.codehilite .vg { color: #19177C } /* Name.Variable.Global */
.codehilite .vi { color: #19177C } /* Name.Variable.Instance */
.codehilite .vm { color: #19177C } /* Name.Variable.Magic */
.codehilite .il { color: #666666 } /* Literal.Number.Integer.Long */
"""

    pn.config.raw_css.append(css)
    app = pn.Column(
        pn.pane.Markdown(test_code.__doc__),
        pnx.Code(code, language="python"),
        sizing_mode="stretch_width",
    )
    app.servable(test_code.__name__)


@pytest.mark.panel
def test_info_alert():
    """Manual test of the InfoAlert Pane

    - Blue Div with normal and bold text
    """
    pn.config.raw_css.append(pnx.InfoAlert.raw_css)
    app = pn.Column(
        pn.pane.Markdown(test_info_alert.__doc__),
        pnx.InfoAlert("This is an **Info Alert**!"),
        sizing_mode="stretch_width",
    )

    app.servable(test_info_alert.__name__)


@pytest.mark.panel
def test_warning_alert():
    """Manual test of the WarningAlert Pane

    - Yellow Div with normal and bold text
    """
    pn.config.raw_css.append(pnx.WarningAlert.raw_css)
    app = pn.Column(
        pn.pane.Markdown(test_warning_alert.__doc__),
        pnx.WarningAlert("This is an **Warning Alert**!"),
        sizing_mode="stretch_width",
    )

    app.servable(test_warning_alert.__name__)


@pytest.mark.panel
def test_error_alert():
    """Manual test of the ErrorAlert Pane

    - Red Div with normal and bold text
    """
    pn.config.raw_css.append(pnx.ErrorAlert.raw_css)
    app = pn.Column(
        pn.pane.Markdown(test_error_alert.__doc__),
        pnx.ErrorAlert("This is an **Error Alert**!"),
        sizing_mode="stretch_width",
    )

    app.servable(test_error_alert.__name__)


@pytest.mark.panel
def test_info_alert_height_problem():
    """Manual test of the InfoAlert Heigh Error

    We saw that the height of InfoAlert Div was much greater than it needed to be.
    See https://github.com/holoviz/panel/issues/829
    """
    pn.config.raw_css.append(pnx.InfoAlert.raw_css)
    text = """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced."""
    app = pn.Column(
        pn.pane.Markdown(test_info_alert.__doc__), pnx.InfoAlert(text), sizing_mode="stretch_width",
    )

    app.servable(test_info_alert.__name__)


if __name__.startswith("bk"):
    test_divider()
    test_code()
    test_info_alert()
    test_warning_alert()
    test_error_alert()
    test_info_alert_height_problem()
