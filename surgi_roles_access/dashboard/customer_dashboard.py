import frappe
from surgi_roles_access.dashboard.customer_dashboard_config import ROLE_DASHBOARD_RULES

def get_data():
    # Load original Customer dashboard structure
    data = frappe.get_meta("Customer").dashboard or {}
    transactions = data.get("transactions", [])

    # Get roles for current user
    user_roles = set(frappe.get_roles())

    # Apply rules for the first matching role
    for role, rules in ROLE_DASHBOARD_RULES.items():
        if role in user_roles:

            # --------------------------
            # REMOVE items
            # --------------------------
            remove_list = set(rules.get("remove", []))
            for section in transactions:
                section["items"] = [
                    item for item in section.get("items", [])
                    if item not in remove_list
                ]

            # --------------------------
            # ADD new items
            # --------------------------
            additions = rules.get("add", {})

            for label, doctypes_to_add in additions.items():
                # Check if section already exists
                section = next((sec for sec in transactions if sec.get("label") == label), None)
                if section:
                    for dt in doctypes_to_add:
                        if dt not in section["items"]:
                            section["items"].append(dt)
                else:
                    # Create a new section
                    transactions.append({
                        "label": label,
                        "items": doctypes_to_add
                    })

            break   # Stop after applying first matching role

    return data
