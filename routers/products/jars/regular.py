from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

regular_jars_router = APIRouter(
    prefix=Prefix.JARS.value,
)

@regular_jars_router.get(Endpoints.REGULAR.value, response_class=HTMLResponse)
def regular_jars(request: Request):

    regular_jars_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.REGULAR_JARS.value,
        request=request,
    )
    return regular_jars_template
