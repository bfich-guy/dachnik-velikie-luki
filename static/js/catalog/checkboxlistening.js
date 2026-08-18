import { checkboxIdList } from "../config/server.js";
import { productTypesList } from "../config/products.js";

import { addCheckboxListener } from "../utils/listeners.js";


addCheckboxListener({
    checkboxIdList: checkboxIdList,
    key: "productType",
    valuesList: productTypesList,
});
