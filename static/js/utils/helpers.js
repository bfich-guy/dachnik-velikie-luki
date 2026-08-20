export function doListsHaveSameLength({
    listsMatrix,
}) {
    const listsMatrixLength = listsMatrix.length;
    const listsMatrixIsEmpty = listsMatrixLength === 0;

    if (listsMatrixIsEmpty) {
        return false;
    } 

    const firstList = listsMatrix[0];
    const etalonLength = firstList.length;
    const slicedListsMatrix = listsMatrix.slice(1);

    for (let list of slicedListsMatrix) {
        const listLength = list.length;
        const mismatchHappened = listLength !== etalonLength;

        if (mismatchHappened) {
            return false;
        }
    }

    return true;
}


export function isIterableObjectEmpty({
    iterableObject,
}) {
    const iterableObjectIsNullOrUndefined = !iterableObject;

    if (iterableObjectIsNullOrUndefined) {
        return false;
    }

    const iterableObjectLength = iterableObject.length;
    const isIterableObjectEmpty = iterableObjectLength === 0;

    return isIterableObjectEmpty;
}


export function isObjectNullOrUndefined({
    object,
}) {
    const isObjectNullOrUndefined = (object === null) || (object === undefined);
    return isObjectNullOrUndefined;
}
