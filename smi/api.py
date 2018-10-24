import frappe
import json
from frappe.utils import get_request_session
import string

@frappe.whitelist(allow_guest=False)
def me():
	user_id = get_user_id_by_session()
	data = dict()
	data["student"] = frappe.get_all('Student',fields="*",filters={"name": user_id})[0]
	assessment = frappe.cache().get_value("Assessment")
	data["assessment"] = frappe.get_all('Assessment Plan',fields="*",filters={"name": assessment})[0]
	return data

@frappe.whitelist(allow_guest=True)
def get_question():
	post = json.loads(frappe.request.data)
	data = dict()
	data["question"] = frappe.db.sql("SELECT * FROM `tabQuestion` WHERE name IN (SELECT question FROM `tabTest Question Item` WHERE parent = '{}')".format(post["test"]),as_dict=True)
	for row in data["question"]:
		row["choice"] = frappe.get_all('Answer',fields="*",filters={"parent": row["name"]})
	return data

@frappe.whitelist(allow_guest=False)
def get_user_id_by_session():
	user = frappe.session.user
	data_student = frappe.get_all("Student",filters={"student_email_id":user})
	return data_student[0]["name"]

@frappe.whitelist(allow_guest=False)
def get_list_test():
	user_id = get_user_id_by_session()
	list_test = frappe.db.sql("SELECT name, test, to_time, course FROM `tabAssessment Plan` WHERE student_group IN (SELECT parent FROM `tabStudent Group Student` WHERE student = '{}') AND docstatus=1 AND NOW() BETWEEN from_time AND to_time".format(user_id),as_dict=True)
	return list_test

@frappe.whitelist(allow_guest=False)
def take_test():
	post = json.loads(frappe.request.data)
	frappe.cache().set_value("Assessment", post["assessment"])
	value = frappe.cache().get_value("Assessment")
	return value

@frappe.whitelist(allow_guest=False)
def set_submited_answer():
	post = json.loads(frappe.request.data)

	for i in post["answer"]:
		answer_type = "answer"
		question = frappe.db.sql("SELECT weight, category FROM `tabQuestion` WHERE name = '{}'".format(post["question"][i]),as_dict=True)
		answer = frappe.db.sql("SELECT is_correct FROM `tabAnswer` WHERE name = '{}'".format(post["answer"][i]),as_dict=True)
		if(question[0]["category"] == "Multiple Choice"):
			status = "Marked"
			if(post["checked"][i] == True and answer[0]["is_correct"] == 1):
				score = question[0]["weight"]
			else:
				score = 0
		elif(question[0]["category"] == "Check"):
			status = "Marked"
			total_answer = frappe.db.sql("SELECT COUNT(name) AS total_answer FROM `tabAnswer` WHERE parent = '{}'".format(post["question"][i]),as_dict=True)
			if(post["checked"][i] == True and answer[0]["is_correct"] == 1):
				score = question[0]["weight"] / total_answer[0]["total_answer"]
			elif(post["checked"][i] == False and answer[0]["is_correct"] == 0):
				score = question[0]["weight"] / total_answer[0]["total_answer"]
			else:
				score = 0
		else:
			answer_type = "essay_answer"
			status = "Unmarked"
			score = 0

		doc = frappe.get_doc({
			'doctype':'Submited Answer',
			'test':post["test"],
			"student":post["user_id"],
			"question":post["question"][i],
			answer_type:post["answer"][i],
			"score":score,
			"status":status
		})
		doc.insert(ignore_permissions=True)
		frappe.db.commit()

	return post["answer"]

@frappe.whitelist(allow_guest=False)
def test():
	post = json.loads(frappe.request.data)
	return post