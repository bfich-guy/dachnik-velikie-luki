import { productNamesDict, productsAttributesNamesDict } from "../config/products.js";
import { endpointDict } from "../config/server.js";
import { cssClassesDict } from "../config/styles.js";

import { isObjectNullOrUndefined, doListsHaveSameLength } from "./helpers.js";
import { getProductDescription } from "./parsers.js";


export function generateCatalog({
    productCatalogId,
}) {
    const productCatalog = document.getElementById(productCatalogId);
    const productsEndpoint = endpointDict["products"];

    fetch(productsEndpoint)
        .then(responce => responce.json())
        .then(data => {
            const productImagesFilesNamesList = data["products_images_files_names_list"];
            const productsDataList = data["products_data_list"];

            const listsMatrix = [productImagesFilesNamesList, productsDataList];
            const lengthsAreMismatched = !doListsHaveSameLength({listsMatrix: listsMatrix});

            if (lengthsAreMismatched) {
                return;
            }

            const productCardClass = cssClassesDict["productCard"];
            const productDescriptionTextClass = cssClassesDict["productDescriptionText"];
            const productImageClass = cssClassesDict["productImage"];

            const productsDataListLength = productsDataList.length;

            for (let index = 0; index < productsDataListLength; index++) {
                const productImageFileName = productImagesFilesNamesList[index];
                const rawProductData = productsDataList[index];
                const parsedProductData = getProductDescription({productData: rawProductData});

                const productWidget = document.createElement("div");
                const productImageWidget = document.createElement("div");
                const productDescriptionWidget = document.createElement("div");

                productWidget.classList.add(productCardClass);

                productImageWidget.innerHTML = `
                    <img class="${productImageClass}" src=/static/images/products/${productImageFileName}>
                `;

                productWidget.appendChild(productImageWidget);

                for (const [key, value] of Object.entries(rawProductData)) {
                    const parsedKey = productsAttributesNamesDict[key];
                    const parsedValue = parsedProductData[key];
                    const productDescriptionTextWidget = `
                        <span class=${key} data-value=${value}></span>
                        <p class=${productDescriptionTextClass}>${parsedKey}: ${parsedValue}</p>
                    `;

                    productDescriptionWidget.insertAdjacentHTML('beforeend', productDescriptionTextWidget);
                }

                productWidget.appendChild(productDescriptionWidget);
                productCatalog.insertAdjacentElement('beforeend', productWidget);
            }
        })
};


export function generateDachnikPhrase({
    productType,
    searchedProductsAmount,
}) {
    let dachnikPhrase = "";

    const noProductIsChosen = isObjectNullOrUndefined({object: productType});

    if (noProductIsChosen) {
        dachnikPhrase = "Что-что хотите? Я не слышу Вас за экраном. Откройте каталог и выберите товар. Обещаю, постараюсь найти! В моем ларьке много чего есть.";
        sessionStorage.setItem("dachnikPhrase", dachnikPhrase);
        return;
    }

    const productName = productNamesDict[productType];
    const productIsUnknown = isObjectNullOrUndefined({object: productName});

    if (productIsUnknown) {
        dachnikPhrase = "Ох-ё... Такой товар забугорский в глаза не видывал! Уж извиняйте, не продаем на данный момент, но он может появиться!";
        sessionStorage.setItem("dachnikPhrase", dachnikPhrase);
    }

    const integeredSearchedProductsAmount = parseInt(searchedProductsAmount);
    const noProductsFound = integeredSearchedProductsAmount <= 0;

    if (noProductsFound) {
        dachnikPhrase = "Я покопался в ларьке и старался найти хоть один нужный Вам товар, но у меня прямо сейчас его нет. Но я обещаю: он когда-то будет и вы однажды его купите!";
        sessionStorage.setItem("dachnikPhrase", dachnikPhrase);
    }

    const onlyOneProductSearched = integeredSearchedProductsAmount === 1;

    if (onlyOneProductSearched) {
        dachnikPhrase = `Держу в голове, что в последний раз Вы искали ${productName}. Я прочесал каждую полочку моего славного ларька и смог найти только ${searchedProductsAmount} такую вещицу!`;
        sessionStorage.setItem("dachnikPhrase", dachnikPhrase);
    } else {
        dachnikPhrase = `Держу в голове, что в последний раз Вы искали ${productName}. Я прочесал каждую полочку моего славного ларька и смог найти этого добра в количестве ${searchedProductsAmount} штук!`;
        sessionStorage.setItem("dachnikPhrase", dachnikPhrase);
    }

};
