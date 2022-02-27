odoo.define('syntax_zebra_printer.action_print', function (require){
    "use strict";
    
    let FormController = require('web.FormController');
    
    FormController.include({
        _onButtonClicked: function (event) {

        let url = "http://localhost:8000/syntax_zebra_printer/print";

        if(event.data.attrs.print === "action_print") {
            let data_print = event.data.record.data.data_print;
    
            console.log(data_print)
    
            if (!data_print) {
                alert('No data to print. Please click Update Printer Data');
                return;
            }

            $.ajax({
                type    : "POST",
                url     : url,
                data    : {
                    data_print : data_print
                },
                success: function(data) {
                    alert('Print Succeeded!');
                    console.log(data);
                },
                error: function(data) {
                    alert('Barcode Print Failed. Please check the Printer Proxy running');
                    console.log(data);
                },
            });

        }
    
        this._super(event);
        },
    });
    });