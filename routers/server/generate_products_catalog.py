from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from config.server import Prefix, Endpoints, JSONKeys, UserInput
from utils.dachnik import generate_catalog, generate_dachnik_phrase


generate_products_catalog_router = APIRouter(prefix=Prefix.INDEX.value)

class ProductFilterSchema(BaseModel):
    product_type: str | None = Field(default=None, max_length=UserInput.MAX_INPUT_LENGTH.value)


@generate_products_catalog_router.post(Endpoints.GENERATE_PRODUCTS_CATALOG.value, response_class=JSONResponse)
async def generate_products_catalog(request: ProductFilterSchema) -> JSONResponse:

    product_type: str | None = request.product_type

    product_type_condition: str | None = "type = ?" if product_type is not None else None
    params: tuple | None = (product_type,) if product_type is not None else ()

    catalog_data_matrix: list[list[str]] = await generate_catalog(filter_condition=product_type_condition, params=params)
    total_searched_products: int = len(catalog_data_matrix)
    
    dachnik_phrase: str = ""
    product_type_exists: bool = isinstance(product_type, str)

    if product_type_exists:
        dachnik_phrase: str = generate_dachnik_phrase(
            product_type=product_type,
            product_amount=total_searched_products,
        )

    responce: dict = {
        JSONKeys.CATALOG_DATA_MATRIX.value: catalog_data_matrix,
        JSONKeys.DACHNIK_PHRASE.value: dachnik_phrase,
    }

    json_responce = JSONResponse(content=responce)
    return json_responce
