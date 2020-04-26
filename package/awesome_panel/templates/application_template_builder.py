import param
import panel as pn
from awesome_panel.models import Application, Theme, MenuItem, SourceLink, SocialLink
from awesome_panel.components import PageComponent
from awesome_panel.templates.application_template import ApplicationTemplate
from . import MaterialTemplate

TEMPLATES = [MaterialTemplate]

THEMES = [Theme(name="Dark")]
TITLE = "Awesome Panel"
LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
URL = "https://awesome-panel.org"
PAGES = [pn.pane.Markdown("# Home"), pn.pane.Markdown("# Gallery")]
MENU_ITEMS = [MenuItem(name="Item 1")]
SOURCE_LINKS = [SourceLink(name="GitHub")]
SOCIAL_LINKS = [SocialLink(name="Twitter")]
APPLICATION = Application(
    title=TITLE,
    logo=LOGO,
    url=URL,
    templates=TEMPLATES,
    themes=THEMES,
    pages=PAGES,
    menu_items=MENU_ITEMS,
    source_links=SOURCE_LINKS,
    social_links=SOCIAL_LINKS,
)

class ApplicationTemplateBuilder(param.Parameterized):
    title = param.String("Application Title")
    url = param.String()
    logo = param.String()
    template = param.ClassSelector(
        default=MaterialTemplate, class_=ApplicationTemplate, is_instance=False
    )
    templates = param.List(TEMPLATES)
    pages = param.List()
    menu_items = param.List()
    source_links = param.List()
    social_links = param.List()

    def create(self):
        application = Application(
            title=self.title,
            url=self.url,
            logo=self.logo,
            template=self.template,
            templates=self.templates,
            pages=self.pages,
            menu_items=self.menu_items,
            source_links=self.source_links,
            social_links=self.social_links,
        )
        return self.template(application=application)
