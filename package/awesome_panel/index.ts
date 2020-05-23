import * as AwesomePanel from "./express/models/"
export {AwesomePanel}

import {register_models} from "@bokeh/bokehjs/base"
register_models(AwesomePanel as any)