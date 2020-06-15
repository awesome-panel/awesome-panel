from awesome_panel.styler.stylers.app_styler import InfoCardStyler

@pytest.fixture
def info_card_styler():
    return InfoCardStyler()

def test_can_construct_info_card_styler(info_card_styler):
    assert info_card_styler.background == "#000000"
    assert info_card_styler.color == "#ffffff"
    assert info_card_styler.css == 