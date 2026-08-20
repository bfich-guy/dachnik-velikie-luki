import { buttonIdDict, productCatalogId } from "../config/server.js";

import { searchProduct } from "../utils/searchers.js";
import { generateDachnikPhrase } from "../utils/generators.js";


const searchButtonId = buttonIdDict["search"];
const searchButtonWidget = document.getElementById(searchButtonId);
const dachnikPhraseWidget = document.getElementById("dachnik-phrase");

searchButtonWidget.addEventListener("click", () => {
    searchProduct({
        targetProductType: sessionStorage.getItem("productType"),
        productCatalogId: productCatalogId,
    });

    const productType = sessionStorage.getItem("productType");
    const searchedProductsAmount = sessionStorage.getItem("searchedProductsAmount");

    generateDachnikPhrase({
        productType: productType,
        searchedProductsAmount: searchedProductsAmount,
    });

    dachnikPhraseWidget.textContent = sessionStorage.getItem("dachnikPhrase");
});
