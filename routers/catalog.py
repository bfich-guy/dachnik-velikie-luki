from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders
from config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
catalog_router = APIRouter(prefix=Prefix.INDEX.value)

@catalog_router.get(Endpoints.CATALOG.value, response_class=HTMLResponse)
def catalog(request: Request) -> HTMLResponse:

    catalog_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.CATALOG.value,
        request=request,
    )
    return catalog_template
