import { buttonRedirect } from "./utils.js";
import { buttonIdDict, endpointDict, pageNameList} from "./config.js";


for (const pageName of pageNameList) {
    const buttonId = buttonIdDict[pageName];
    const endpoint = endpointDict[pageName];

    buttonRedirect({
        buttonId: buttonId,
        endpoint: endpoint,
    });
}
