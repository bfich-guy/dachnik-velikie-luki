import { productAttributesKeysList, productsAttributesRussianTranslationsDict, productNamesDict } from "../config/products.js";
import { endpointDict } from "../config/server.js";
import { cssClassesDict } from "../config/styles.js";

import { getProductInfo } from "../utils/parsers.js";


export function generateCatalog({
    productCatalogId,
    productAttributesKeysList,
}) {
    const productCatalog = document.getElementById(productCatalogId);
    const productsEndpoint = endpointDict["products"];

    fetch(productsEndpoint)
        .then(responce => responce.json())
        .then(data => {
            const productImagesFilesNamesList = data["products_images_files_names_list"];

            const productImageClass = cssClassesDict["productImage"];
            const productCardClass = cssClassesDict["productCard"];
            const productTypeClass = cssClassesDict["productType"];
            const productVolumeClass = cssClassesDict["productVolume"];
            const productDiameterClass = cssClassesDict["productDiameter"];
            const productDescriptionTextClass = cssClassesDict["productDescriptionText"];

            for (let productImageFileName of productImagesFilesNamesList) {

                const productCardWidget = document.createElement("div");
                productCardWidget.classList.add(productCardClass);
                const productInfoDict = getProductInfo({productName: productImageFileName});

                productCardWidget.innerHTML = `<img class="${productImageClass}", src="/static/images/products/${productImageFileName}">`;

                for (let productAttributeKey of productAttributesKeysList) {
                    const productAttributeValue = productInfoDict[productAttributeKey];
                    const productDOMAttribute = `<span class="${"product-" + productAttributeKey}" data-value="${productAttributeValue}"></span>`;
                    productCardWidget.insertAdjacentHTML('beforeend', productDOMAttribute);
                }
                
                productCatalog.appendChild(productCardWidget);
            }
        })
};


