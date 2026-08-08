from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

screw_jars_router: APIRouter = APIRouter(
    prefix=Prefix.JARS.value,
)

@screw_jars_router.get(Endpoints.SCREW.value, response_class=HTMLResponse)
def screw_jars(request: Request):

    screw_jars_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.SCREW_JARS.value,
        request=request,
    )
    return screw_jars_template
