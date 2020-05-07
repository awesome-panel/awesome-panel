from awesome_panel.application.models import *
from awesome_panel.application.services import *
from awesome_panel.application.components import *

application = Application(
    title="App Title"
)
home_page = Page(name="Home")

page_2 = Page(name="Page 2",)

pages = [home_page, page_2]

page_service = PageService(pages=pages, page=home_page, default_page=home_page,)
print(page_service.pages)
page_navigation_view = PageNavigationComponent(page_service=page_service, application=application)

page_navigation_view.servable()
