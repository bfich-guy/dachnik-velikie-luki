import { productNamesDict } from "../config/products.js";


function getNumberFromString({
    string,
}) {
    const digits = "0123456789";
    const digitsList = [];

    for (let character of string) {
        const characterIsDigit = digits.includes(character);
        
        if (characterIsDigit) {
            digitsList.push(character);
        }
    }

    const stringifiedNumber = digitsList.join("");
    const number = Number(stringifiedNumber);
    return number;
    
}


export function descryptBase64InWidget({ widget }) {
    const enscryptedData = widget.getAttribute("data-value");
    const binString = atob(enscryptedData);
    const bytes = Uint8Array.from(binString, (m) => m.codePointAt(0));
    const descryptedData = new TextDecoder("utf-8").decode(bytes);
    widget.textContent = descryptedData;
}


export function getProductDescription({
    productData,
}) {
    const productDescription = {};

    for (const [key, value] of Object.entries(productData)) {
        const keyIsType = key === "type";
        const keyIsVolume = key === "volume";
        const keyIsDiameter = key === "diameter";

        if (keyIsType) {
            const type = productNamesDict[value];
            productDescription[key] = type;
        } else if (keyIsVolume) {
            const volume = (getNumberFromString({string: value}) / 1000).toString() + " л.";
            productDescription[key] = volume;
        } else if (keyIsDiameter) {
            const diameter = (getNumberFromString({string: value})).toString() + " мм.";
            productDescription[key] = diameter;
        } else {
            productDescription[key] = value;
        }
    }

    return productDescription;
}
