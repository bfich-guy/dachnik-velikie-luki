from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

semiautomatic_seaming_machines_router = APIRouter(
    prefix=Prefix.SEAMING_MACHINES.value,
)

@semiautomatic_seaming_machines_router.get(Endpoints.SEMIAUTOMATIC.value, response_class=HTMLResponse)
def semiautomatic_seaming_machines(request: Request):

    semiautomatic_seaming_machines_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.SEMIAUTOMATIC_SEAMING_MACHINES.value,
        request=request,
    )
    return semiautomatic_seaming_machines_template
