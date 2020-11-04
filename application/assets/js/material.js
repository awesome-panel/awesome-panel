var templateDesignMap = {
    // ".bk-btn": {
    //     "remove": ["bk-btn"],
    //     "add": ["mdc-icon-button"],
    // },
    // ".bk-btn-default": {
    //     "remove": ["bk-btn-default"],
    //     "add": ["mdc-button--outlined", "mdc-ripple-upgraded--unbounded", "mdc-ripple-upgraded"],
    //     "style": ["--mdc-ripple-fg-size:28px; --mdc-ripple-fg-scale:1.71429; --mdc-ripple-left:10px; --mdc-ripple-top:10px;"]
    // },
}
function updateTemplateClasses(){
    for (var key in templateDesignMap) {
        // check if the property/key is defined in the object itself, not in parent
        if (templateDesignMap.hasOwnProperty(key)) {
            var els=document.querySelectorAll(key);
            for (let el of els){
                console.log(el)
                var settings=templateDesignMap[key]
                for (var index in settings["remove"]){
                    el.classList.remove(settings["remove"][index])
                    console.log(settings["remove"][index])
                }
                for (var index in settings["add"]){
                    console.log(index);
                    el.classList.add(settings["add"][index])
                    console.log(settings["add"][index])
                }
                el.style.cssText=el.style.cssText+";"+settings["style"]
            }
        }
    }
}