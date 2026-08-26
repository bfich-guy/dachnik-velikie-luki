import { descryptBase64InWidget } from "../utils.js";


document.addEventListener("DOMContentLoaded", () => {
    const dachnikStoreAddressWigdet = document.getElementById("dachnik-store-address");
    const dachnikOwnerNumberWigdet = document.getElementById("dachnik-owner-number");
    const dachnikDeveloperNumberWigdet = document.getElementById("dachnik-developer-number");

    const widgetsList = [dachnikStoreAddressWigdet, dachnikOwnerNumberWigdet, dachnikDeveloperNumberWigdet];

    for (let widget of widgetsList) {
        descryptBase64InWidget({widget: widget});
    }
});
