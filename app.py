import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from config.system import ServerData
from config.server import Directories, Mounts

from utils.server import include_routers

from routers.index import index_router
from routers.about_us import about_us_router
from routers.help import help_router
from routers.products.jars.regular import regular_jars_router
from routers.products.jars.screw import screw_jars_router
from routers.products.lids.regular import regular_lids_router
from routers.products.lids.screw import screw_lids_router
from routers.products.seamingmachines.automatic import automatic_seaming_machines_router
from routers.products.seamingmachines.semiautomatic import semiautomatic_seaming_machines_router
from routers.products.seamingmachines.spiral import spiral_seaming_machines_router


app = FastAPI()
routers_list: list[APIRouter] = [
    index_router,
    about_us_router,
    help_router,
    regular_jars_router,
    screw_jars_router,
    regular_lids_router,
    screw_lids_router,
    automatic_seaming_machines_router,
    semiautomatic_seaming_machines_router,
    spiral_seaming_machines_router,
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
