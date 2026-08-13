from enum import Enum

from config.system import Directories, Files, FileExtenstion


class Mounts(Enum):
    STATIC = f"/{Directories.STATIC.value}"    


class Prefix(Enum):
    INDEX = f""
    PRODUCTS = f"/{Directories.PRODUCTS.value}"

    JARS = f"/{Directories.PRODUCTS.value}/{Directories.JARS.value}"
    LIDS = f"/{Directories.PRODUCTS.value}/{Directories.LIDS.value}"
    SEAMING_MACHINES = f"/{Directories.PRODUCTS.value}/{Directories.SEAMING_MACHINES.value}"


class Endpoints(Enum):
    INDEX = f"/"
    ABOUT_US = f"/{Files.ABOUT_US.value}"
    HELP = f"/{Files.HELP.value}"

    REGULAR = f"/{Files.REGULAR.value}"
    SCREW = f"/{Files.SCREW.value}"
    AUTOMATIC = f"/{Files.AUTOMATIC.value}"
    SEMIAUTOMATIC = f"/{Files.SEMIAUTOMATIC.value}"
    SPIRAL = f"/{Files.SPIRAL.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstion.HTML.value}"
    ABOUT_US = f"{Files.ABOUT_US.value}.{FileExtenstion.HTML.value}"
    HELP = f"{Files.HELP.value}.{FileExtenstion.HTML.value}"

    REGULAR_JARS = f"{Directories.PRODUCTS.value}/{Directories.JARS.value}/{Files.REGULAR.value}.{FileExtenstion.HTML.value}"
    SCREW_JARS = f"{Directories.PRODUCTS.value}/{Directories.JARS.value}/{Files.SCREW.value}.{FileExtenstion.HTML.value}"

    REGULAR_LIDS = f"{Directories.PRODUCTS.value}/{Directories.LIDS.value}/{Files.REGULAR.value}.{FileExtenstion.HTML.value}"
    SCREW_LIDS = f"{Directories.PRODUCTS.value}/{Directories.LIDS.value}/{Files.SCREW.value}.{FileExtenstion.HTML.value}"

    AUTOMATIC_SEAMING_MACHINES = f"{Directories.PRODUCTS.value}/{Directories.SEAMING_MACHINES.value}/{Files.AUTOMATIC.value}.{FileExtenstion.HTML.value}"
    SEMIAUTOMATIC_SEAMING_MACHINES = f"{Directories.PRODUCTS.value}/{Directories.SEAMING_MACHINES.value}/{Files.SEMIAUTOMATIC.value}.{FileExtenstion.HTML.value}"
    SPIRAL_SEAMING_MACHINES = f"{Directories.PRODUCTS.value}/{Directories.SEAMING_MACHINES.value}/{Files.SPIRAL.value}.{FileExtenstion.HTML.value}"
