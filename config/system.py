from enum import Enum


class Directories(Enum):
    TEMPLATES = "templates"
    STATIC = "static"
    
    PRODUCTS = "products"
    JARS = "jars"
    LIDS = "lids"
    SEAMING_MACHINES = "seamingmachines"


class Files(Enum):
    INDEX = "index"
    ABOUT_US = "about_us"

    REGULAR = "regular"
    SCREW = "screw"
    AUTOMATIC = "automatic"
    SEMIAUTOMATIC = "semiautomatic"
    SPIRAL = "spiral"


class FileExtenstion(Enum):
    HTML = "html"
    PY = "py"


class ServerData(Enum):
    APP = "app:app"
    HOST = "127.0.0.1"
    PORT = 8000
    RELOAD = True
