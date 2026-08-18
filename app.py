import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

from config.system import DotenvServerKeys, Folders, ServerData
from config.server import Mounts

from utils.server import include_routers

from routers.about_us import about_us_router
from routers.catalog import catalog_router
from routers.help import help_router
from routers.index import index_router
from routers.products import products_router


load_dotenv()

app = FastAPI()
routers_list: list[APIRouter] = [
    about_us_router,
    catalog_router,
    help_router,
    index_router,
    products_router,
]

app.mount(Mounts.STATIC.value, StaticFiles(directory=Folders.STATIC.value), name=Folders.STATIC.value)
include_routers(app=app, routers_list=routers_list)

server_is_launching_directly: bool = __name__ == "__main__"

if server_is_launching_directly:
    uvicorn.run(
        os.getenv(DotenvServerKeys.APP_NAME.value, ServerData.APP_NAME.value), 
        host=os.getenv(DotenvServerKeys.APP_HOST.value, ServerData.APP_HOST.value),
        port=int(os.getenv(DotenvServerKeys.APP_PORT.value, ServerData.APP_PORT.value)), 
        reload=os.getenv(DotenvServerKeys.APP_RELOAD.value, str(ServerData.APP_RELOAD.value)) == "True",
        )
