import { productsCatalogId, dachnikPhraseId, endpoints, fetchQuery, JSONKeys, checkboxProductMap} from "./config.js";


export function generateCatalog({
    generateProductsCatalogEndpoint=endpoints["generateProductsCatalog"],
    productType=null,
}) {
    fetch(generateProductsCatalogEndpoint, {
        method: fetchQuery["methods"]["POST"],
        headers: fetchQuery["headers"]["json"],
        body: JSON.stringify({
            [JSONKeys["productType"]]: productType,
        })
    })
    .then(responce => responce.json())
    .then(data => {
        const catalogDataMatrix = data[JSONKeys["catalogDataMatrix"]];
        const dachnikPhrase = data[JSONKeys["dachnikPhrase"]];

        const dachnikPhraseWidget = document.getElementById(dachnikPhraseId);
        const productCatalogWidget = document.getElementById(productsCatalogId);

        const thereIsNoDachnikPhrase = dachnikPhrase === "";

        if (thereIsNoDachnikPhrase) {
            dachnikPhraseWidget.textContent = "Привет, я - Дачник. Я знаю каждый товар в своем ларьке Скажите мне, какой товар хотите, и я найду его для вас. Чтобы это сделать, воспользуйтесь каталогом ниже.";
        } else {
            dachnikPhraseWidget.textContent = dachnikPhrase;
        }

        for (let catalogDataList of catalogDataMatrix) {
            const imagePath = catalogDataList[0];
            const productDescriptionText = catalogDataList[1];

            const productCardWidget = document.createElement("div");
            const productImageWidget = document.createElement("div");
            const productDescriptionTextWidget = document.createElement("div");

            productCardWidget.classList.add("product-card");

            productImageWidget.innerHTML = `
                <img class="product-image" src=${imagePath}>
            `;
            productDescriptionTextWidget.innerHTML = `
                <p class="product-description-text">${productDescriptionText}</p>
            `;

            productCardWidget.appendChild(productImageWidget);
            productCardWidget.appendChild(productDescriptionTextWidget);

            productCatalogWidget.appendChild(productCardWidget);
        }
    });
};


export function addCheckboxListener({}) {
    const productCatalogWidget = document.getElementById(productsCatalogId);

    for (const [checkboxId, productType] of Object.entries(checkboxProductMap)) {
        const checkboxWidget = document.getElementById(checkboxId);

        checkboxWidget.addEventListener("change", () => {
            const checkboxWidgetIsChecked = checkboxWidget.checked;

            if (checkboxWidgetIsChecked) {
                productCatalogWidget.innerHTML = ``;
                generateCatalog({
                    productType: productType,
                });
            } else {
                productCatalogWidget.innerHTML = ``;
                generateCatalog({});
            }
        });
    }
};


export function descryptBase64InWidget({ widget }) {
    const enscryptedData = widget.getAttribute("data-value");
    const binString = atob(enscryptedData);
    const bytes = Uint8Array.from(binString, (m) => m.codePointAt(0));
    const descryptedData = new TextDecoder("utf-8").decode(bytes);
    widget.textContent = descryptedData;
};
