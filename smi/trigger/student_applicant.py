import frappe
import json
from frappe.utils import get_request_session
from smi.helper import log

@frappe.whitelist(allow_guest=False)
def enroll_applicant_program(self,method):
	if(self.application_status == "Approved"):
		fullname = self.first_name
		if self.middle_name != None:
			fullname += " " + self.middle_name
		if self.last_name != None:
			fullname += " " + self.last_name

		for row in self.program_table:
			data_student = frappe.db.sql("SELECT * FROM `tabStudent` WHERE student_applicant = '{}'".format(self.name),as_dict=True)
			doc = frappe.get_doc({
				"doctype": "Program Enrollment",
				"student": data_student[0]["name"],
				"student_name": fullname,
				"program": row.program,
				"academic_year": self.academic_year,
				"enrollment_date": frappe.utils.today()
			})
			doc.insert()
			frappe.db.commit()

		frappe.msgprint("Program Enrollment has been created")
		return self