from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Tags, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

lid_seaming_machines_router: APIRouter = APIRouter(
    prefix=Prefix.GOODS.value,
    tags=[Tags.LID_SEAMING_MACHINES],
)

@lid_seaming_machines_router.get(Endpoints.LID_SEAMING_MACHINES.value, response_class=HTMLResponse)
def lid_seaming_machines(request: Request):

    lid_seaming_machines_Jinja2Template: HTMLResponse = templates.TemplateResponse(
        name=Templates.LID_SEAMING_MACHINES.value,
        request=request,
    )
    return lid_seaming_machines_Jinja2Template
