from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Tags, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

seaming_machines_router: APIRouter = APIRouter(
    prefix=Prefix.PRODUCTS.value,
    tags=[Tags.SEAMING_MACHINES],
)

@seaming_machines_router.get(Endpoints.SEAMING_MACHINES.value, response_class=HTMLResponse)
def seaming_machines(request: Request):

    seaming_machines_Jinja2Template: HTMLResponse = templates.TemplateResponse(
        name=Templates.SEAMING_MACHINES.value,
        request=request,
    )
    return seaming_machines_Jinja2Template
