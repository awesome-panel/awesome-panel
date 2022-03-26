"""Demo of the AwesomeButton from the awesome-panel-extensions package"""
import panel as pn
from awesome_panel_extensions.models.icon import Icon
from awesome_panel_extensions.widgets.button import AwesomeButton

from awesome_panel import config

pn.config.js_files[
    "fontawesome"
] = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/js/all.min.js"

config.extension(url="awesome_button")

# Source: https://fast.design/
github = Icon(
    name="Github",
    value="""<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-github" viewBox="0 0 19 20"><path d="M6.71154 17.0776C2.09615 18.4906 2.09615 14.7226 0.25 14.2517L6.71154 17.0776ZM13.1731 19.9036V16.2581C13.2077 15.8089 13.1482 15.3574 12.9986 14.9335C12.849 14.5096 12.6127 14.123 12.3054 13.7995C15.2038 13.4698 18.25 12.3489 18.25 7.20563C18.2498 5.89046 17.754 4.62572 16.8654 3.67319C17.2862 2.52257 17.2564 1.25074 16.7823 0.121918C16.7823 0.121918 15.6931 -0.207776 13.1731 1.51605C11.0574 0.930913 8.82722 0.930913 6.71154 1.51605C4.19154 -0.207776 3.10231 0.121918 3.10231 0.121918C2.62819 1.25074 2.59844 2.52257 3.01923 3.67319C2.12396 4.63279 1.62771 5.90895 1.63462 7.23389C1.63462 12.3394 4.68077 13.4604 7.57923 13.8278C7.27554 14.148 7.04132 14.5299 6.89182 14.9486C6.74233 15.3674 6.6809 15.8135 6.71154 16.2581V19.9036"></path></svg>""", # pylint: disable=line-too-long
    fill_color="#E1477E",
    spin_duration=2000,
)

rotating_icon_button = AwesomeButton(name="Click Me", icon=github, button_type="success")

# Source: https://fontawesome.com/icons/hand-holding-water?style=solid
FA_HAND_HOLDING_WATER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M288 256c53 0 96-42.1 96-94 0-40-57.1-120.7-83.2-155.6-6.4-8.5-19.2-8.5-25.6 0C249.1 41.3 192 122 192 162c0 51.9 43 94 96 94zm277.3 72.1c-11.8-10.7-30.2-10-42.6 0L430.3 402c-11.3 9.1-25.4 14-40 14H272c-8.8 0-16-7.2-16-16s7.2-16 16-16h78.3c15.9 0 30.7-10.9 33.3-26.6 3.3-20-12.1-37.4-31.6-37.4H192c-27 0-53.1 9.3-74.1 26.3L71.4 384H16c-8.8 0-16 7.2-16 16v96c0 8.8 7.2 16 16 16h356.8c14.5 0 28.6-4.9 40-14L564 377c15.2-12.1 16.4-35.3 1.3-48.9z"/></svg>""" # pylint: disable=line-too-long
masking_button = AwesomeButton(
    name="",
    icon=Icon(name="Masking Example", value=FA_HAND_HOLDING_WATER, size=8.0),
    button_type="primary",
)

snowboarding = Icon(
    name="Car",
    value="""<i class="fas fa-snowboarding fa-10x fa-rotate-90"></i>""",
)

snowboarding_button = AwesomeButton(icon=snowboarding, height=200)

envelope_with_counter = Icon(
    name="Envelope",
)

counter_button = AwesomeButton(
    icon=envelope_with_counter,
    width=65,
    height=65,
    sizing_mode="fixed",
    css_classes=["bk-btn-light"],
)


def _update_counter(clicks):
    envelope_with_counter.value = f"""
<span class="fa-layers fa-fw fa-4x">
    <i class="fas fa-envelope"></i>
    <span class="fa-layers-counter" style="background:Tomato">{clicks}</span>
</span>
"""


pn.bind(_update_counter, clicks=counter_button.param.clicks, watch=True)
_update_counter(0)


pn.Row(
    pn.Column(rotating_icon_button.param.clicks, rotating_icon_button),
    pn.Column(masking_button.param.clicks, masking_button),
    pn.Column(snowboarding_button.param.clicks, snowboarding_button),
    pn.Column(counter_button.param.clicks, counter_button),
).servable()
