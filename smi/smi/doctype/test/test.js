// Copyright (c) 2018, DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Test', {

});


frappe.ui.form.on("Test Question Item", "weight", function(frm, cdt, cdn) { // notice the presence of cdt and cdn
    var item = locals[cdt][cdn];
    var total_weight = 0
    for(var i in frm.doc.questions){
	    total_weight += parseInt(frm.doc.questions[i].weight);
	}
    frm.set_value('total_score',total_weight);
});