import * as AwesomePanel from "./package/awesome_panel/express/models/"
export {AwesomePanel}

import {register_models} from "@bokehjs/base"
register_models(AwesomePanel as any)