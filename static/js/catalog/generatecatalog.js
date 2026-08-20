import { productCatalogId } from "../config/server.js";

import { generateCatalog } from "../utils/generators.js";


generateCatalog({
    productCatalogId: productCatalogId,
});
