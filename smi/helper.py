import frappe
import json

def log(title, content):
	doc = frappe.get_doc({
			'doctype':'Log',
			'title':title,
			'content':content
		})

	doc.insert(ignore_permissions=True)
	frappe.db.commit()