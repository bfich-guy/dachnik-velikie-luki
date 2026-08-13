from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

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
