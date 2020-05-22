import panel as pn

pn.config.sizing_mode = "stretch_width"

MAX_WIDTH = 1140

spacer = pn.Spacer(height=10, background="blue", margin=0)
main_content = pn.Column(
    "Example 3 " * 100,
    sizing_mode="stretch_width",
    max_width=MAX_WIDTH,
    background="green",
    align="center",  # WHY I SHOULD set align="center" here and not on main_area confused me
)
main_area = pn.Column(
    spacer,  # TRICK: WONT WORK WITHOUT. YOU CAN SET HEIGHT TO 0 TO NOT TAKE UP HEIGHT
    main_content,
    sizing_mode="stretch_both",
    background="lightgray",
)

main_area.servable()
