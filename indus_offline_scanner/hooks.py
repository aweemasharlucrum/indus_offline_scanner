app_name = "indus_offline_scanner"
app_title = "indus_offline_scanner"
app_publisher = "Lucrum"
app_description = "indus_offline_scanner"
app_email = "info@lucrumerp.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/indus_offline_scanner/css/indus_offline_scanner.css"
# app_include_js = "/assets/indus_offline_scanner/js/indus_offline_scanner.js"

# include js, css files in header of web template
# web_include_css = "/assets/indus_offline_scanner/css/indus_offline_scanner.css"
# web_include_js = "/assets/indus_offline_scanner/js/indus_offline_scanner.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "indus_offline_scanner/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "indus_offline_scanner/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "indus_offline_scanner.utils.jinja_methods",
#	"filters": "indus_offline_scanner.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "indus_offline_scanner.install.before_install"
# after_install = "indus_offline_scanner.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "indus_offline_scanner.uninstall.before_uninstall"
# after_uninstall = "indus_offline_scanner.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "indus_offline_scanner.utils.before_app_install"
# after_app_install = "indus_offline_scanner.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "indus_offline_scanner.utils.before_app_uninstall"
# after_app_uninstall = "indus_offline_scanner.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See ducky.core.notifications.get_notification_config

# notification_config = "indus_offline_scanner.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "ducky.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "ducky.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"indus_offline_scanner.tasks.all"
#	],
#	"daily": [
#		"indus_offline_scanner.tasks.daily"
#	],
#	"hourly": [
#		"indus_offline_scanner.tasks.hourly"
#	],
#	"weekly": [
#		"indus_offline_scanner.tasks.weekly"
#	],
#	"monthly": [
#		"indus_offline_scanner.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "indus_offline_scanner.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"ducky.desk.doctype.event.event.get_events": "indus_offline_scanner.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Ducky apps
# override_doctype_dashboards = {
#	"Task": "indus_offline_scanner.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["indus_offline_scanner.utils.before_request"]
# after_request = ["indus_offline_scanner.utils.after_request"]

# Job Events
# ----------
# before_job = ["indus_offline_scanner.utils.before_job"]
# after_job = ["indus_offline_scanner.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"indus_offline_scanner.auth.validate"
# ]
