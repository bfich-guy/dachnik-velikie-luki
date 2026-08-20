from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders, FileExtenstions
from config.server import Prefix, Endpoints, JSONKeys

from utils.system import get_files_names_list, get_dictionaries_list_from_strings_list


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
products_router = APIRouter(prefix=Prefix.INDEX.value)

@products_router.get(Endpoints.PRODUCTS.value, response_class=JSONResponse)
def products():

    products_images_files_names_list: list[str] = get_files_names_list(
        extenstion=FileExtenstions.PNG.value, 
        folder_path=Folders.PRODUCTS_IMAGES.value,
        )

    products_data_list: list[dict] = get_dictionaries_list_from_strings_list(strings_list=products_images_files_names_list)

    products_json_response: dict = {
        JSONKeys.PRODUCTS_IMAGES_FILES_NAMES_LIST.value: products_images_files_names_list,
        JSONKeys.PRODUCTS_DATA_LIST.value: products_data_list,
        }
    
    return products_json_response
