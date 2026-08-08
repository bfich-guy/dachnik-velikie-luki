from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

screw_lids_router: APIRouter = APIRouter(
    prefix=Prefix.LIDS.value,
)

@screw_lids_router.get(Endpoints.REGULAR.value, response_class=HTMLResponse)
def screw_lids(request: Request):

    screw_lids_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.SCREW_LIDS.value,
        request=request,
    )
    return screw_lids_template
