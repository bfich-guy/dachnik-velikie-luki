from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from config.system import Folders
from config.server import Mounts

from utils.server import include_routers

from routers.about_us import about_us_router
from routers.catalog import catalog_router
from routers.help import help_router
from routers.index import index_router
from routers.products import products_router

app = FastAPI()

origins_list: list[str] = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "https://dachnik-velikie-luki.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

routers_list: list[APIRouter] = [
    about_us_router,
    catalog_router,
    help_router,
    index_router,
    products_router,
]

include_routers(
    app=app, 
    routers_list=routers_list,
    )

app.mount(
    Mounts.STATIC.value, 
    StaticFiles(directory=Folders.STATIC.value), 
    name=Folders.STATIC.value,
    )
