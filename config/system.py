from enum import Enum


class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    PRODUCTS_IMAGES = "static/images/products"


class Files(Enum):
    ABOUT_US = "about_us"
    CATALOG = "catalog"
    HELP = "help"
    INDEX = "index"

    PRODUCTS = "products"


class FileExtenstions(Enum):
    HTML = "html"
    PY = "py"
    PNG = "png"


class DotenvServerKeys(Enum):
    APP_NAME = "APP_NAME"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_POST"
    APP_RELOAD = "APP_RELOAD"


class Characters(Enum):
    DOT = "."
    MINUS = "-"
