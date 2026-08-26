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
    FAQ = f"/{Files.FAQ.value}"

    GENERATE_PRODUCTS_CATALOG = f"/{Files.GENERATE_PRODUCTS_CATALOG.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstions.HTML.value}"
    ABOUT_US = f"{Files.ABOUT_US.value}.{FileExtenstions.HTML.value}"
    CATALOG = f"{Files.CATALOG.value}.{FileExtenstions.HTML.value}"
    FAQ = f"{Files.FAQ.value}.{FileExtenstions.HTML.value}"


class JSONKeys(Enum):
    CATALOG_DATA_MATRIX = "catalog_data_matrix"
    DACHNIK_PHRASE = "dachnik_phrase"


class UserInput(Enum):
    MAX_INPUT_LENGTH = 32
