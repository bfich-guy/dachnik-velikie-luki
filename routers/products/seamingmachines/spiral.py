from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

spiral_seaming_machines_router: APIRouter = APIRouter(
    prefix=Prefix.SEAMING_MACHINES.value,
)

@spiral_seaming_machines_router.get(Endpoints.SEMIAUTOMATIC.value, response_class=HTMLResponse)
def spiral_seaming_machines(request: Request):

    spiral_seaming_machines_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.SPIRAL_SEAMING_MACHINES.value,
        request=request,
    )
    return spiral_seaming_machines_template
