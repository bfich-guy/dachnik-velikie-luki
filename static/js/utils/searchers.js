import { productNamesDict } from "../config/products.js";
import { cssClassesDict } from "../config/styles.js";


export function searchProduct({
    targetProductType,
    productCatalogId,
}) {
    const productCatalog = document.getElementById(productCatalogId);
    const productCardDoesNotExist = !productCatalog
    
    if (productCardDoesNotExist) {
        return;
    }
    
    const productCardsList = productCatalog.children;
    const productTypeClass = cssClassesDict["productType"];

    let searchedProductsAmount = 0;

    for (let productCard of productCardsList) {
        const productType = productCard.getElementsByClassName(productTypeClass)[0].dataset.value;
        const productIsSearched = targetProductType === productType;

        if (productIsSearched) {
            productCard.style.display = "flex";
            searchedProductsAmount += 1;
        } else {
            productCard.style.display = "none";
        }
    }

    sessionStorage.setItem("searchedProductsAmount", searchedProductsAmount);
};
