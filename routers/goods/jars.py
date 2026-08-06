from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Tags, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

jars_router: APIRouter = APIRouter(
    prefix=Prefix.GOODS.value,
    tags=[Tags.JARS],
)

@jars_router.get(Endpoints.JARS.value, response_class=HTMLResponse)
def jars(request: Request):

    jars_Jinja2Template: HTMLResponse = templates.TemplateResponse(
        name=Templates.JARS.value,
        request=request,
    )
    return jars_Jinja2Template
