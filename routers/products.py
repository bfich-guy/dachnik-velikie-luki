from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders, FileExtenstions
from config.server import Prefix, Endpoints, JSONKeys

from utils.system import get_files_names_list


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)

products_router = APIRouter(
    prefix=Prefix.INDEX.value,
)

@products_router.get(Endpoints.PRODUCTS.value, response_class=JSONResponse)
def products():

    products_images_files_names_list: list[str] = get_files_names_list(
        extenstion=FileExtenstions.PNG.value, 
        folder_path=Folders.PRODUCTS_IMAGES.value,
        )

    print(products_images_files_names_list)

    products_json_response: dict[str, list[str]] = {JSONKeys.PRODUCTS_IMAGES_FILES_NAMES_LIST.value: products_images_files_names_list}
    return products_json_response
