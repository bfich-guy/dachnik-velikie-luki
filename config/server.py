from enum import Enum


class Directories(Enum):
    TEMPLATES = "templates"
    STATIC = "static"


class Mounts(Enum):
    STATIC = "/static"


class Endpoints(Enum):
    INDEX = "/"
    ABOUT_US = "/about_us"

    JARS = "/jars"
    SEAMING_MACHINES = "/seaming_machines"
    LIDS = "/lids"


class Templates(Enum):
    INDEX = "index.html"
    ABOUT_US = "about_us.html"

    JARS = "products/jars.html"
    SEAMING_MACHINES = "products/seaming_machines.html"
    LIDS = "products/lids.html"
    

class Prefix(Enum):
    INDEX = ""

    PRODUCTS = "/products"


class Tags(Enum):
    INDEX = ["Дачник"]

    JARS = ["Банки"]
    SEAMING_MACHINES = ["Закаточные машины"]
    LIDS = ["Крышки"]


class ServerData(Enum):
    APP = "app:app"
    HOST = "127.0.0.1"
    PORT = 8000
    RELOAD = True
