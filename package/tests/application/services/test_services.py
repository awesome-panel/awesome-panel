from awesome_panel.application.services import (
    Services,
    ProgressService,
    PageService,
    MessageService,
    ThemeService
)

def test_can_construct():
    services = Services()
    assert isinstance(services, Services)
    assert isinstance(services.progress_service, ProgressService)
    assert isinstance(services.page_service, PageService)
    assert isinstance(services.message_service, MessageService)
    assert isinstance(services.theme_service, ThemeService)

def test_can_construct_fixture(services, progress_service, page_service, message_service, theme_service):
    assert isinstance(services, Services)
    assert services.progress_service == progress_service
    assert services.page_service == page_service
    assert services.message_service == message_service
    assert services.theme_service == theme_service

