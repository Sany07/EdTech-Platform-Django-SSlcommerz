/**
* Theme: Montran Admin Template
* Author: Coderthemes
* Form wizard page
*/

!function($) {
    "use strict";

    var FormWizard = function() {};

    FormWizard.prototype.createBasic = function($form_container) {
        $form_container.children("div").steps({
            headerTag: "h3",
            bodyTag: "section",
            transitionEffect: "slideLeft"
        });
        return $form_container;
    },
    //creates form with validation

    //creates vertical form
    FormWizard.prototype.createVertical = function($form_container) {
        $form_container.steps({
            headerTag: "h3",
            bodyTag: "section",
            transitionEffect: "fade",
            stepsOrientation: "vertical"
        });
        return $form_container;
    },
    FormWizard.prototype.init = function() {
        //initialzing various forms

        //basic form
        this.createBasic($("#basic-form"));



        //vertical form
        this.createVertical($("#wizard-vertical"));
    },
    //init
    $.FormWizard = new FormWizard, $.FormWizard.Constructor = FormWizard
}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.FormWizard.init()
}(window.jQuery);