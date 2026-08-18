from enum import Enum

from config.system import Folders, Files, FileExtenstions


class Mounts(Enum):
    STATIC = f"/{Folders.STATIC.value}"    


class Prefix(Enum):
    INDEX = f""


class Endpoints(Enum):
    INDEX = f"/"
    ABOUT_US = f"/{Files.ABOUT_US.value}"
    CATALOG = f"/{Files.CATALOG.value}"
    HELP = f"/{Files.HELP.value}"

    PRODUCTS = f"/{Files.PRODUCTS.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstions.HTML.value}"
    ABOUT_US = f"{Files.ABOUT_US.value}.{FileExtenstions.HTML.value}"
    CATALOG = f"{Files.CATALOG.value}.{FileExtenstions.HTML.value}"
    HELP = f"{Files.HELP.value}.{FileExtenstions.HTML.value}"


class JSONKeys(Enum):
    PRODUCTS_IMAGES_FILES_NAMES_LIST = "products_images_files_names_list"
