from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders
from config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)

about_us_router = APIRouter(
    prefix=Prefix.INDEX.value,
)

@about_us_router.get(Endpoints.ABOUT_US.value, response_class=HTMLResponse)
def about_us(request: Request):

    about_us_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.ABOUT_US.value,
        request=request,
    )
    return about_us_template
