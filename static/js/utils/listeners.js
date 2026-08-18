export function addCheckboxListener({
    checkboxIdList,
    key,
    valuesList,
}) {
    const checkboxIdListLength = checkboxIdList.length;
    const valuesListLength = valuesList.length;

    const lengthsAreMismatched = checkboxIdListLength !== valuesListLength;

    if (lengthsAreMismatched) {
        return;
    } else {
        for (let index = 0; index < valuesListLength; index++) {
            const checkboxId = checkboxIdList[index];
            const value = valuesList[index];

            const checkboxWidget = document.getElementById(checkboxId);

            checkboxWidget.addEventListener("change", () => {
                sessionStorage.setItem(key, value)
            });
        }
    }
}
