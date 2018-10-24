# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "smi"
app_title = "SMI"
app_publisher = "DAS"
app_description = "Sekolah Musik Indonesia"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "digitalasiasolusindo@gmail.com"
app_license = "Copyright DAS 2018"

doc_events = {
	"Student": {
		"after_insert": "smi.trigger.student.create_user_and_enroll_program"
	}
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/smi/css/smi.css"
# app_include_js = "/assets/smi/js/smi.js"

# include js, css files in header of web template
# web_include_css = "/assets/smi/css/smi.css"
# web_include_js = "/assets/smi/js/smi.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "smi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "smi.install.before_install"
# after_install = "smi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "smi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"smi.tasks.all"
# 	],
# 	"daily": [
# 		"smi.tasks.daily"
# 	],
# 	"hourly": [
# 		"smi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"smi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"smi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "smi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "smi.event.get_events"
# }

