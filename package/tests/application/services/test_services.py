from awesome_panel.application.services import (
    Services,
    ProgressService,
    PageService,
    MessageService,
    ThemeService
)

def test_can_construct(services):
    assert isinstance(services, Services)
    assert isinstance(services.progress_service, ProgressService)
    assert isinstance(services.page_service, PageService)
    assert isinstance(services.message_service, MessageService)
    assert isinstance(services.theme_service, ThemeService)