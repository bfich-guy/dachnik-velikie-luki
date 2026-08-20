import { isObjectNullOrUndefined } from "../utils/helpers.js";


const dachnikPhraseWidget = document.getElementById("dachnik-phrase");
const dachnikPhrase = sessionStorage.getItem("dachnikPhrase");

const dachnikPhraseDoesNotExistYet = isObjectNullOrUndefined({object: dachnikPhrase});


if (dachnikPhraseDoesNotExistYet) {
    dachnikPhraseWidget.textContent = "Привет, я - Дачник! Я помогу Вам с урожаем. Так, что вы хотите найти? Скажите мне в каталоге! Мой номер Вы найдете в странице «О нас»."
} else {
    dachnikPhraseWidget.textContent = sessionStorage.getItem("dachnikPhrase");
}
