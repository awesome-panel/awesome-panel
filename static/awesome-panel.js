/*!
 * Copyright (c) 2012 - 2020, Anaconda, Inc., and Bokeh Contributors
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 * 
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 * 
 * Neither the name of Anaconda nor the names of any contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
*/
(function(root, factory) {
  factory(root["Bokeh"], undefined);
})(this, function(Bokeh, version) {
  var define;
  return (function(modules, entry, aliases, externals) {
    const bokeh = typeof Bokeh !== "undefined" && (version != null ? Bokeh[version] : Bokeh);
    if (bokeh != null) {
      return bokeh.register_plugin(modules, entry, aliases);
    } else {
      throw new Error("Cannot find Bokeh " + version + ". You have to load it prior to loading plugins.");
    }
  })
({
"b41f2b1d65": /* index.js */ function _(require, module, exports) {
    Object.defineProperty(exports, "__esModule", { value: true });
    const tslib_1 = require("tslib");
    const AwesomePanel = tslib_1.__importStar(require("515b1a12fc") /* ./package/awesome_panel/express/models/ */);
    exports.AwesomePanel = AwesomePanel;
    const base_1 = require("@bokehjs/base");
    base_1.register_models(AwesomePanel);
},
"515b1a12fc": /* package\awesome_panel\express\models\index.js */ function _(require, module, exports) {
    Object.defineProperty(exports, "__esModule", { value: true });
    var web_component_1 = require("e601bd599b") /* ./web_component */;
    exports.WebComponent = web_component_1.WebComponent;
},
"e601bd599b": /* package\awesome_panel\express\models\web_component.js */ function _(require, module, exports) {
    Object.defineProperty(exports, "__esModule", { value: true });
    const tslib_1 = require("tslib");
    const dom_1 = require("@bokehjs/core/dom");
    const p = tslib_1.__importStar(require("@bokehjs/core/properties"));
    const html_box_1 = require("@bokehjs/models/layouts/html_box");
    const inputs_1 = require("@bokehjs/styles/widgets/inputs");
    function htmlDecode(input) {
        var doc = new DOMParser().parseFromString(input, "text/html");
        return doc.documentElement.textContent;
    }
    class WebComponentView extends html_box_1.HTMLBoxView {
        connect_signals() {
            super.connect_signals();
            this.connect(this.model.properties.name.change, () => this.handleNameChange());
            this.connect(this.model.properties.innerHTML.change, () => this.render());
            this.connect(this.model.properties.attributesLastChange.change, () => this.handleAttributesLastChangeChange());
            this.connect(this.model.properties.propertiesLastChange.change, () => this.handlePropertiesLastChangeChange());
            this.connect(this.model.properties.columnDataSource.change, () => this.handleColumnDataSourceChange());
        }
        handleNameChange() {
            if (this.label_el)
                this.label_el.textContent = this.model.name;
        }
        render() {
            super.render();
            if (this.el.innerHTML !== this.model.innerHTML)
                this.createOrUpdateWebComponentElement();
        }
        after_layout() {
            if ("after_layout" in this.webComponentElement)
                this.webComponentElement.after_layout();
        }
        createOrUpdateWebComponentElement() {
            if (this.webComponentElement)
                this.webComponentElement.onchange = null;
            // @Philippfr: How do we make sure the component is automatically sized according to the
            // parameters of the WebComponent like width, height, sizing_mode etc?
            // Should we set height and width to 100% or similar?
            // For now I've set min_height as a part of .py __init__ for some of the Wired components?
            const title = this.model.name;
            if (this.model.componentType === "inputgroup" && title) {
                this.group_el = dom_1.div({ class: inputs_1.bk_input_group }, this.label_el);
                this.group_el.innerHTML = htmlDecode(this.model.innerHTML);
                this.webComponentElement = this.group_el.firstElementChild;
                this.label_el = dom_1.label({ style: { display: title.length == 0 ? "none" : "" } }, title);
                this.group_el.insertBefore(this.label_el, this.webComponentElement);
                this.el.appendChild(this.group_el);
            }
            else {
                this.el.innerHTML = htmlDecode(this.model.innerHTML);
                this.webComponentElement = this.el.firstElementChild;
            }
            this.activate_scripts(this.webComponentElement.parentNode);
            // Initialize properties
            this.initPropertyValues();
            this.handlePropertiesLastChangeChange();
            this.handleColumnDataSourceChange();
            // Subscribe to events
            this.webComponentElement.onchange = (ev) => this.handlePropertiesChange(ev);
            this.addEventListeners();
            this.addAttributesMutationObserver();
        }
        addAttributesMutationObserver() {
            if (!this.model.attributesToWatch)
                return;
            let options = {
                childList: false,
                attributes: true,
                characterData: false,
                subtree: false,
                attributeFilter: Object.keys(this.model.attributesToWatch),
                attributeOldValue: false,
                characterDataOldValue: false
            };
            const handleAttributesChange = (_) => {
                let attributesLastChange = new Object();
                for (let attribute in this.model.attributesToWatch) {
                    const value = this.webComponentElement.getAttribute(attribute);
                    attributesLastChange[attribute] = value;
                }
                if (this.model.attributesLastChange !== attributesLastChange)
                    this.model.attributesLastChange = attributesLastChange;
            };
            let observer = new MutationObserver(handleAttributesChange);
            observer.observe(this.webComponentElement, options);
        }
        addEventListeners() {
            this.eventsCount = {};
            for (let event in this.model.eventsToWatch) {
                this.eventsCount[event] = 0;
                this.webComponentElement.addEventListener(event, (ev) => this.eventHandler(ev), false);
            }
        }
        transform_cds_to_records(cds) {
            const data = [];
            const columns = cds.columns();
            if (columns.length === 0) {
                return [];
            }
            for (let i = 0; i < cds.data[columns[0]].length; i++) {
                const item = {};
                for (const column of columns) {
                    const shape = cds._shapes[column];
                    if ((shape !== undefined) && (shape.length > 1) && (typeof shape[0] == "number"))
                        item[column] = cds.get_array(column).slice(i * shape[1], i * shape[1] + shape[1]);
                    else
                        item[column] = cds.data[column][i];
                }
                data.push(item);
            }
            return data;
        }
        // https://stackoverflow.com/questions/5999998/check-if-a-variable-is-of-function-type
        isFunction(functionToCheck) {
            if (functionToCheck) {
                const stringName = {}.toString.call(functionToCheck);
                return stringName === '[object Function]' || stringName === '[object AsyncFunction]';
            }
            else {
                return false;
            }
        }
        /**
         * Handles changes to `this.model.columnDataSource`
         * by
         * updating the data source of `this.webComponentElement`
         * using the function or property specifed in `this.model.columnDataSourceLoadFunction`
         */
        handleColumnDataSourceChange() {
            // @Philippfr: Right now we just reload all the data
            // For example Perspective has an `update` function to append data
            // Is this something we could/ should support?
            if (this.model.columnDataSource) {
                let data; // list
                const columnDataSourceOrient = this.model.columnDataSourceOrient;
                if (columnDataSourceOrient === "records")
                    data = this.transform_cds_to_records(this.model.columnDataSource);
                else
                    data = this.model.columnDataSource.data; // @ts-ignore
                const loadFunctionName = this.model.columnDataSourceLoadFunction.toString();
                const loadFunction = this.webComponentElement[loadFunctionName];
                if (this.isFunction(loadFunction))
                    this.webComponentElement[loadFunctionName](data);
                else
                    this.webComponentElement[loadFunctionName] = data;
            }
            // Todo: handle situation where this.model.columnDataSource is null
        }
        activate_scripts(el) {
            Array.from(el.querySelectorAll("script")).forEach((oldScript) => {
                const newScript = document.createElement("script");
                Array.from(oldScript.attributes)
                    .forEach(attr => newScript.setAttribute(attr.name, attr.value));
                newScript.appendChild(document.createTextNode(oldScript.innerHTML));
                if (oldScript.parentNode)
                    oldScript.parentNode.replaceChild(newScript, oldScript);
            });
        }
        // See https://stackoverflow.com/questions/6491463/accessing-nested-javascript-objects-with-string-key
        /**
         * Example:
         *
         * `get_nested_property(element, "textInput.value")` returns `element.textInput.value`
         *
         * @param element
         * @param property_
         */
        get_nested_property(element, property_) {
            property_ = property_.replace(/\[(\w+)\]/g, '.$1'); // convert indexes to properties
            property_ = property_.replace(/^\./, ''); // strip a leading dot
            let a = property_.split('.');
            for (let i = 0, n = a.length; i < n; ++i) {
                let k = a[i];
                if (k in element)
                    element = element[k];
                else
                    return "";
            }
            return element;
        }
        set_nested_property(element, property_, value) {
            // @Phillipfr: I need your help to understand and solve this
            // hack: Setting the value of the WIRED-SLIDER before its ready
            // will destroy the setter.
            // I don't yet understand this.
            // if (["WIRED-SLIDER"].indexOf(element.tagName)>=0){
            //   const setter = element.__lookupSetter__(property_);
            //   if (!setter){return}
            // }
            const pList = property_.split('.');
            if (pList.length === 1)
                element[property_] = value;
            else {
                const len = pList.length;
                for (let i = 0; i < len - 1; i++) {
                    const elem = pList[i];
                    if (!element[elem])
                        element[elem] = {};
                    element = element[elem];
                }
                element[pList[len - 1]] = value;
            }
        }
        /**
         * Handles events from `eventsToWatch` by
         *
         * - Incrementing the count of the event
         * - Checking if any properties have changed
         *
         * @param ev The Event Fired
         */
        eventHandler(ev) {
            let event = ev.type;
            this.eventsCount[event] += 1;
            let eventsCountLastChanged = {};
            eventsCountLastChanged[event] = this.eventsCount[event];
            this.model.eventsCountLastChange = eventsCountLastChanged;
            this.checkIfPropertiesChanged();
        }
        /** Checks if any properties have changed. In case this is communicated to the server.
         *
         * For example the Wired `DropDown` does not run the `onchange` event handler when the selection changes.
         * Insted the `select` event is fired. Thus we can subscribe to this event and manually check for property changes.
         */
        checkIfPropertiesChanged() {
            const propertiesChange = {};
            for (const property in this.model.propertiesToWatch) {
                const oldValue = this.propertyValues[property];
                const newValue = this.get_nested_property(this.webComponentElement, property);
                if (oldValue != newValue) {
                    propertiesChange[property] = newValue;
                    this.propertyValues[property] = newValue;
                }
            }
            if (Object.keys(propertiesChange).length)
                this.model.propertiesLastChange = propertiesChange;
        }
        /** Handles the `WebComponentElement` `(on)change` event
         *
         * Communicates any changed properties in `propertiesToWatch` to the server
         * by updating `this.model.propertiesLastChange`.
         * @param ev
         */
        handlePropertiesChange(ev) {
            const properties_change = new Object();
            for (const property in this.model.propertiesToWatch) {
                if (property in ev.detail) {
                    properties_change[property] = ev.detail[property];
                    this.propertyValues[property] = ev.detail[property];
                }
            }
            if (Object.keys(properties_change).length)
                this.model.propertiesLastChange = properties_change;
        }
        initPropertyValues() {
            this.propertyValues = new Object();
            if (!this.webComponentElement) {
                return;
            }
            for (let property in this.model.propertiesToWatch) {
                let old_value = this.propertyValues[property];
                let new_value = this.get_nested_property(this.webComponentElement, property);
                if (new_value !== old_value) {
                    this.propertyValues[property] = new_value;
                }
            }
        }
        /**
         * Handles changes to `this.model.attributesLastChange`
         * by
         * updating the attributes of `this.webComponentElement` accordingly
         */
        handleAttributesLastChangeChange() {
            if (!this.webComponentElement)
                return;
            let attributesLastChange = this.model.attributesLastChange;
            for (let attribute in this.model.attributesLastChange) {
                if (attribute in this.model.attributesToWatch) {
                    let old_value = this.webComponentElement.getAttribute(attribute);
                    let new_value = attributesLastChange[attribute];
                    if (old_value !== new_value) {
                        if (new_value === null)
                            this.webComponentElement.removeAttribute(attribute);
                        else
                            this.webComponentElement.setAttribute(attribute, new_value);
                    }
                }
            }
        }
        /**
        * Handles changes to `this.model.propertiesLastChange`
        * by
        * updating the properties of `this.webComponentElement` accordingly
        */
        handlePropertiesLastChangeChange() {
            if (!this.webComponentElement) {
                return;
            }
            let propertiesLastChange = this.model.propertiesLastChange;
            for (let property in this.model.propertiesLastChange) {
                if (property in this.model.propertiesToWatch) {
                    let value = propertiesLastChange[property];
                    this.set_nested_property(this.webComponentElement, property, value);
                }
            }
        }
    }
    exports.WebComponentView = WebComponentView;
    WebComponentView.__name__ = "WebComponentView";
    class WebComponent extends html_box_1.HTMLBox {
        constructor(attrs) {
            super(attrs);
        }
        static init_WebComponent() {
            this.prototype.default_view = WebComponentView;
            this.define({
                // @Philipfr: How do I make property types more specific
                componentType: [p.String, 'htmlbox'],
                innerHTML: [p.String, ''],
                attributesToWatch: [p.Any],
                attributesLastChange: [p.Any],
                propertiesToWatch: [p.Any],
                propertiesLastChange: [p.Any],
                eventsToWatch: [p.Any],
                eventsCountLastChange: [p.Any],
                columnDataSource: [p.Any],
                columnDataSourceOrient: [p.Any],
                columnDataSourceLoadFunction: [p.Any],
            });
        }
    }
    exports.WebComponent = WebComponent;
    WebComponent.__name__ = "WebComponent";
    WebComponent.__module__ = "awesome_panel.express.models.web_component";
    WebComponent.init_WebComponent();
},
}, "b41f2b1d65", {"index":"b41f2b1d65","package/awesome_panel/express/models/index":"515b1a12fc","package/awesome_panel/express/models/web_component":"e601bd599b"}, {});
})

//# sourceMappingURL=awesome-panel.js.map
