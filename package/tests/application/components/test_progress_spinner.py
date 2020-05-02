from awesome_panel.application.services import ProgressService

def test_can_construct(progress_spinner):
    assert isinstance(progress_spinner.progress_service, ProgressService)

    assert isinstance(progress_spinner.spinner_static_url, str)
    assert progress_spinner.spinner_static_url

    assert isinstance(progress_spinner.spinning_url, str)
    assert progress_spinner.spinning_url

    assert progress_spinner.object == progress_spinner.spinner_static_url



def test_can_spin(progress_spinner):
    # When
    progress_spinner.progress.mark_active()
    assert progress_spinner.object == progress_spinner.spinning_url

    # When
    progress_spinner.progress.reset()
    assert progress_spinner.object == progress_spinner.spinner_static_url