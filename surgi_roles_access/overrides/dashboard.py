import frappe
from frappe.desk.doctype.dashboard import dashboard
from surgi_roles_access.config.dashboard_roles import ROLE_DASHBOARD_CONFIG

def get_dashboard_data_override(module, doctype, name=None):
    data = dashboard.get_dashboard_data(module, doctype, name)
    user_roles = frappe.get_roles(frappe.session.user)

    # Iterate through roles and apply filters
    for role in user_roles:
        if role in ROLE_DASHBOARD_CONFIG:
            cfg = ROLE_DASHBOARD_CONFIG[role]

            # Filter connections
            connections = data.get("connections", [])
            filtered = []

            for conn in connections:
                dt = conn.get("doctype")
                if dt in cfg.get("deny", []):
                    continue
                if cfg.get("allow") and dt not in cfg["allow"]:
                    continue
                filtered.append(conn)

            data["connections"] = filtered
            break  # stop at first matching role

    return data
