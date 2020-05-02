def test_can_construct(progress):
    assert progress.value == 0
    assert progress.value_max == 100
    assert progress.message == ""
    assert progress.active_count == 0
    assert progress.active == False
