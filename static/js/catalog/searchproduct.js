import { buttonIdDict, productCatalogId } from "../config/server.js";

import { searchProduct } from "../utils/searchers.js";


const searchButtonId = buttonIdDict["search"];
const searchButtonWidget = document.getElementById(searchButtonId);

searchButtonWidget.addEventListener("click", () => {
    searchProduct({
        targetProductType: sessionStorage.getItem("productType"),
        productCatalogId: productCatalogId,
    });
});
