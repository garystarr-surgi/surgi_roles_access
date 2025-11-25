import frappe
from frappe.desk.doctype.dashboard import dashboard

def get_dashboard_data_override(module, doctype, name=None):
    # Get the normal dashboard data
    data = dashboard.get_dashboard_data(module, doctype, name)

    # If user has the restricted role, remove all connections
    if "Sales User" in frappe.get_roles(frappe.session.user):
        data["connections"] = []

    return data
