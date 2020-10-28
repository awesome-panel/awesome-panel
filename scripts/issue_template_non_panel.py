import holoviews as hv
import numpy as np
from panel.template import VanillaTemplate


def test_template_can_use_non_panels():
    header = "[Header Link](https://panel.holoviz.org)"
    sidebar = "[Menu Item](https://panel.holoviz.org)<br/>" * 5

    xs = np.linspace(0, np.pi * 4, 40)
    main = hv.Area((xs, np.sin(xs)))
    template = VanillaTemplate(title="My App")
    template.header.append(header)
    template.sidebar.append(sidebar)
    template.main.append(main)
    template.show()
