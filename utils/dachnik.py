from typing import Any
from dotenv import load_dotenv
from os import getenv
from json import loads

from config.system import DotenvServerKeys, Characters, DatabaseTables, DatabaseFilePaths
from config.dachnik import ProductTypes, ProductNames, ProductExtraDataKeys, DachnikPhrases, MeasurementUnits, ConversionFactors, product_type_map

from utils.database import read_database_table


load_dotenv()


def generate_dachnik_phrase(
    *,
    product_type: str,
    product_type_map: dict[str, str] = product_type_map,
    product_amount: int
) -> str:

    dachnik_phrase: str = Characters.EMPTY.value

    try:
        product_name: str = product_type_map[product_type]
        dachnik_phrase: str = f"{DachnikPhrases.SEARCHED_PRODUCT.value[0]}{product_name}{DachnikPhrases.SEARCHED_PRODUCT.value[1]}{product_amount}{DachnikPhrases.SEARCHED_PRODUCT.value[2]}"
    except KeyError:
        dachnik_phrase: str = DachnikPhrases.UNKNOWN_PRODUCT_TYPE.value

    return dachnik_phrase


def generate_product_description(
    *, 
    product_data_tuple: tuple[Any, ...],
) -> str:

    product_type: str = product_data_tuple[1]
    product_extra_data: dict[str, Any] = loads(product_data_tuple[3])

    product_description_map: dict[str, str] = {
        ProductTypes.JAR_REGULAR.value: f"{ProductNames.JAR_REGULAR.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value} {product_extra_data.get(ProductExtraDataKeys.VOLUME.value, 0) / ConversionFactors.MILLILITER_TO_LITER.value}{MeasurementUnits.LITER.value}",
        ProductTypes.JAR_SCREW.value: f"{ProductNames.JAR_SCREW.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value} {product_extra_data.get(ProductExtraDataKeys.VOLUME.value, 0) / ConversionFactors.MILLILITER_TO_LITER.value}{MeasurementUnits.LITER.value}",

        ProductTypes.LID_REGULAR.value: f"{ProductNames.LID_REGULAR.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value} {product_extra_data.get(ProductExtraDataKeys.AMOUNT.value, 0)}{MeasurementUnits.AMOUNT.value}",
        ProductTypes.LID_SCREW.value: f"{ProductNames.LID_SCREW.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value} {product_extra_data.get(ProductExtraDataKeys.AMOUNT.value, 0)}{MeasurementUnits.AMOUNT.value}",

        ProductTypes.SEAMINGMACHINE_AUTO.value: f"{ProductNames.SEAMINGMACHINE_AUTO.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value}",
        ProductTypes.SEAMINGMACHINE_SEMIAUTO.value: f"{ProductNames.SEAMINGMACHINE_SEMIAUTO.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value}",
        ProductTypes.SEAMINGMACHINE_SPIRAL.value: f"{ProductNames.SEAMINGMACHINE_SPIRAL.value} {product_extra_data.get(ProductExtraDataKeys.DIAMETER.value, 0)}{MeasurementUnits.MILLIMETER.value}",
    }

    product_description: str = product_description_map.get(product_type, DachnikPhrases.UNKNOWN_PRODUCT_DESCRIPTION.value)
    return product_description


async def generate_catalog(*, filter_condition: str | None = None, params: tuple | None = ()) -> list[list[str]]:
    catalog_data_matrix: list[list[str]] = []

    products_data_matrix: list[tuple[Any, ...]] = await read_database_table(
        file_path=getenv(DotenvServerKeys.DATABASE_FILE_PATH.value, DatabaseFilePaths.DEFAULT.value),
        table_name=DatabaseTables.PRODUCTS.value,
        condition=filter_condition,
        params=params,
    )

    for product_data_tuple in products_data_matrix:
        product_image_path: str = product_data_tuple[2]
        product_description: str = generate_product_description(product_data_tuple=product_data_tuple)

        catalog_data_list: list[str] = [product_image_path, product_description]
        catalog_data_matrix.append(catalog_data_list)

    return catalog_data_matrix
