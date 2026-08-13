from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

help_router = APIRouter(
    prefix=Prefix.INDEX.value,
)

@help_router.get(Endpoints.HELP.value, response_class=HTMLResponse)
def help(request: Request):

    help_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.HELP.value,
        request=request,
    )
    return help_template
