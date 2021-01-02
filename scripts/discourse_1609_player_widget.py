import panel as pn
import param

data_dict = {
    "sub-01": [("run1", 100), ("run2", 100), ("run3", 60)],
    "sub-02": [("run1", 200), ("run2", 100), ("run3", 50)],
    "sub-03": [("run1", 100), ("run2", 400)],
}
subject_list = list(data_dict.keys())

subject_select = pn.widgets.Select(
    name="Select Subject", options=subject_list, value=subject_list[0]
)
run_select = pn.widgets.Select(
    name="Select Run",
    options=[
        data_dict[subject_select.value][i][0]
        for i in range(0, len(data_dict[subject_select.value]))
    ],
)


def get_num_tp(sbj, run):
    for item in data_dict[sbj]:
        if item[0] == run:
            return item[1]
    return 0


player = pn.widgets.Player(
    name="Player",
    start=0,
    end=get_num_tp(subject_select.value, run_select.value),
    value=1,
    loop_policy="loop",
    width=800,
    step=1,
)


@pn.depends(subject_select, watch=True)
def update_run(subject):
    run_select.options = [item[0] for item in data_dict[subject]]


@pn.depends(subject_select, run_select, watch=True)
def update_player(subject, run):
    end_value = get_num_tp(subject, run)
    player.value = min(player.value, end_value)
    player.end = end_value


@pn.depends(player)
def print_player_value(value):
    value = str(value)
    markdown = pn.pane.Markdown(value)
    return markdown


pn.Column(pn.Row(subject_select, run_select), player, print_player_value).servable()


data_dict2 = {
    "sub-01": {"run1": 100, "run2": 100, "run3": 60},
    "sub-02": {"run1": 200, "run2": 100, "run3": 50},
    "sub-03": {"run1": 100, "run2": 400},
}