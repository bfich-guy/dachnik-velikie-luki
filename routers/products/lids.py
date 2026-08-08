from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.server import Prefix, Tags, Directories, Endpoints, Templates


templates = Jinja2Templates(directory=Directories.TEMPLATES.value)

lids_router: APIRouter = APIRouter(
    prefix=Prefix.PRODUCTS.value,
    tags=[Tags.LIDS],
)

@lids_router.get(Endpoints.LIDS.value, response_class=HTMLResponse)
def lids(request: Request):

    lids_Jinja2Template: HTMLResponse = templates.TemplateResponse(
        name=Templates.LIDS.value,
        request=request,
    )
    return lids_Jinja2Template
