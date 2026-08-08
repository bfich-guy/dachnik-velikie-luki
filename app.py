import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from config.server import ServerData, Directories, Mounts
from utils import include_routers

from routers.index import index_router
from routers.about_us import about_us_router
from routers.products.jars import jars_router
from routers.products.seaming_machines import seaming_machines_router
from routers.products.lids import lids_router


app: FastAPI = FastAPI()
routers_list: list[APIRouter] = [
    index_router,
    about_us_router,
    jars_router,
    seaming_machines_router,
    lids_router,
]

app.mount(Mounts.STATIC.value, StaticFiles(directory=Directories.STATIC.value), name=Directories.STATIC.value)
include_routers(app=app, routers_list=routers_list)

server_is_launching_directly: bool = __name__ == "__main__"

if server_is_launching_directly:
    uvicorn.run(
        ServerData.APP.value, 
        host=ServerData.HOST.value,
        port=ServerData.PORT.value, 
        reload=ServerData.RELOAD.value,
        )
