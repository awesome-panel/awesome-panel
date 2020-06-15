from awesome_panel.styler.app import InfoCard
import panel as pn

# from awesome_panel.styler.app import AppBar InfoCard, PrettyContainer, SettingsContainer


@pytest.fixture
def info_card():
    return InfoCard(value=62000, text="Downloads", background="white", color="black")


def test_info_card(info_card):
    assert isinstance(info_card, pn.Row)
    assert info_card.sizing_mode == "stretch_width"
    assert info_card.value == 62000
    assert info_card.text == "Downloads"
