from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

regular_lids_router = APIRouter(
    prefix=Prefix.LIDS.value,
)

@regular_lids_router.get(Endpoints.REGULAR.value, response_class=HTMLResponse)
def regular_lids(request: Request):

    regular_lids_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.REGULAR_LIDS.value,
        request=request,
    )
    return regular_lids_template
