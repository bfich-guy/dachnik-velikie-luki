function getValueFromWidget({
    widget,
}) {
    const value = widget.dataset.value;
    return value;
}


export function getProductInfo({
    productName,
}) {
    const productTokensList = productName.split("-");
    const productTokensListLength = productTokensList.length;

    let productInfoKeysList = [];
    let productInfoValuesList = [];

    let productInfoDict = {}

    for (let index = 0; index < productTokensListLength; index++) {
        const productTokensListElement = productTokensList[index];

        const productTokensListElementIsKey = index % 2 === 0;
        const productTokensListElementIsValue = index % 2 === 1;

        if (productTokensListElementIsKey) {
            productInfoKeysList.push(productTokensListElement);
        } else if (productTokensListElementIsValue) {
            productInfoValuesList.push(productTokensListElement);
        }
    }
    
    const productInfoValuesListLength = productInfoValuesList.length;
    
    for (let index = 0; index < productInfoValuesListLength; index++) {
        const key = productInfoKeysList[index];
        const value = productInfoValuesList[index];

        productInfoDict[key] = value;
    }

    return productInfoDict;
}