def _to_plot(data):
    gridstyle = {"xgrid_line_color": None}
    curve_opts = opts.Curve(  # pylint: disable=no-member
        line_width=4,
        responsive=True,
        color=get_color_cycle(),
    )
    group_by = []
    if len(data.ElementName.unique()) > 1:
        group_by.append("Element")
    if len(data.InstanceName.unique()) > 1:
        group_by.append("Instance")
    return (
        data.rename(columns={"ElementName": "Element", "InstanceName": "Instance"})
        .hvplot(x="Datetime", y="Value", by=group_by)
        .opts(
            curve_opts,
        )
        .opts(show_grid=True)
    )
