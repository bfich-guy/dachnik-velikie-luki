from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders
from config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)

index_router = APIRouter(
    prefix=Prefix.INDEX.value,
)

@index_router.get(Endpoints.INDEX.value, response_class=HTMLResponse)
def index(request: Request):

    index_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.INDEX.value,
        request=request,
    )
    return index_template
