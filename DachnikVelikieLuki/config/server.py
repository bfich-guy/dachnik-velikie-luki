from enum import Enum


class Directories(Enum):
    TEMPLATES = "templates"
    STATIC = "static"


class Mounts(Enum):
    STATIC = "/static"


class Endpoints(Enum):
    INDEX = "/"

    JARS = "/jars"
    LID_SEAMING_MACHINES = "/lid_seaming_machines"
    LIDS = "/lids"


class Templates(Enum):
    INDEX = "index.html"

    JARS = "goods/jars.html"
    LID_SEAMING_MACHINES = "goods/lid_seaming_machines.html"
    LIDS = "goods/lids.html"
    

class Prefix(Enum):
    INDEX = ""

    GOODS = "/goods"


class Tags(Enum):
    INDEX = ["Дачник"]

    JARS = ["Банки"]
    LID_SEAMING_MACHINES = ["Закаточные машины"]
    LIDS = ["Крышки"]


class ServerData(Enum):
    APP = "app:app"
    HOST = "127.0.0.1"
    PORT = 8000
    RELOAD = True
