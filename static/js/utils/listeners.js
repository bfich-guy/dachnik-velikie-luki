import { doListsHaveSameLength } from "./helpers.js";


export function addCheckboxListener({
    checkboxIdList,
    key,
    valuesList,
}) {
    const listsMatrix = [checkboxIdList, valuesList];
    const lengthsAreMismatched = !doListsHaveSameLength({listsMatrix: listsMatrix});

    if (lengthsAreMismatched) {
        return;
    }

    const valuesListLength = valuesList.length;

    for (let index = 0; index < valuesListLength; index++) {
        const checkboxId = checkboxIdList[index];
        const value = valuesList[index];

        const checkboxWidget = document.getElementById(checkboxId);

        checkboxWidget.addEventListener("change", () => {
            sessionStorage.setItem(key, value)
        });
    }
}
