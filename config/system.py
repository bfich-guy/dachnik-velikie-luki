from enum import Enum


class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    PRODUCTS_IMAGES = "static/images/products"


class Files(Enum):
    ABOUT_US = "about_us"
    CATALOG = "catalog"
    FAQ = "faq"
    INDEX = "index"

    GENERATE_PRODUCTS_CATALOG = "generate_products_catalog"


class FileExtenstions(Enum):
    HTML = "html"
    PY = "py"
    PNG = "png"


class DotenvServerKeys(Enum):
    APP_NAME = "APP_NAME"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_POST"
    APP_RELOAD = "APP_RELOAD"

    DATABASE_FILE_PATH = "DATABASE_FILE_PATH"
    DATABASE_KEY = "DATABASE_KEY"


class Characters(Enum):
    EMPTY = ""

    DOT = "."
    MINUS = "-"


class DatabaseTables(Enum):
    PRODUCTS = "products"


class DatabaseFilePaths(Enum):
    DEFAULT = "database.db"
