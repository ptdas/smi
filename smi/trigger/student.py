import frappe
import json
from frappe.utils import get_request_session
from smi.helper import log

@frappe.whitelist(allow_guest=False)
def create_user_and_enroll_program(self,method):
	password = str(self.date_of_birth).replace('-','')
	roles_to_apply=[{"role":"Student"}]
	full_name = self.first_name
	if self.middle_name != None:
		full_name += " " + self.middle_name
	if self.last_name != None:
		full_name += " " + self.last_name

	doc = frappe.get_doc({
		"doctype": "User",
		"email": self.student_email_id,
		"full_name": full_name,
		"first_name": self.first_name,
		"middle_name": self.middle_name,
		"last_name": self.last_name,
		"send_welcome_email": 0,
		"password": password,
		"send_password_update_notification": 0,
		"roles": roles_to_apply
	})
	doc.insert()
	frappe.db.commit()
	frappe.msgprint("New student has been created")

	if self.student_applicant != None:
		frappe.msgprint("Student applicant is exist")
		data_student_applicant = frappe.db.sql("SELECT * FROM `tabStudent Applicant` WHERE name = '{}'".format(self.student_applicant),as_dict=True)
		frappe.msgprint(str(len(data_student_applicant)))
		data_applicant_program = frappe.db.sql("SELECT * FROM `tabApplicant Program` WHERE parent = '{}'".format(data_student_applicant[0]["name"]),as_dict=True)
		frappe.msgprint(str(len(data_applicant_program)))
		for row in data_applicant_program:
			doc = frappe.get_doc({
				"doctype": "Program Enrollment",
				"docstatus": 1,
				"student": self.name,
				"student_name": full_name,
				"program": row["program"],
				"academic_year": data_student_applicant[0]["academic_year"],
				"enrollment_date": frappe.utils.today()
			})
			frappe.msgprint(str(row["program"]))
			doc.insert()
			frappe.db.commit()

			frappe.msgprint("Program enrollment is created")
