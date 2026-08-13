from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

automatic_seaming_machines_router = APIRouter(
    prefix=Prefix.SEAMING_MACHINES.value,
)

@automatic_seaming_machines_router.get(Endpoints.AUTOMATIC.value, response_class=HTMLResponse)
def automatic_seaming_machines(request: Request):

    automatic_seaming_machines_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.AUTOMATIC_SEAMING_MACHINES.value,
        request=request,
    )
    return automatic_seaming_machines_template
