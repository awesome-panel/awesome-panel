import param
from .progress_service import ProgressService
from .page_service import PageService
from .message_service import MessageService
from .theme_service import ThemeService

class Services(param.Parameterized):
    progress_service = param.ClassSelector(class_=ProgressService, allow_None=False)
    page_service = param.ClassSelector(class_=PageService, allow_None=False)
    progress_service = param.ClassSelector(class_=ProgressService, allow_None=False)
    theme_service = param.ClassSelector(class_=ThemeService, allow_None=False)

    def __init__(self, **params):
        if "progress_service" not in params:
            params["progress_service"]=ProgressService()
        if "page_service" not in params:
            params["page_service"]=PageService()
        if "message_service" not in params:
            params["message_service"]=MessageService()
        if "theme_service" not in params:
            params["theme_service"]=ThemeService()

        super().__init__(**params)