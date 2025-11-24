import frappe
import copy
from surgi_roles_access.dashboard.customer_dashboard_config import ROLE_DASHBOARD_RULES

def get_data():
    # Load original Customer dashboard structure
    original_data = frappe.get_meta("Customer").dashboard or {}
    # Make a deep copy to avoid modifying the original
    data = copy.deepcopy(original_data) if original_data else {}
    transactions = data.get("transactions", [])
    if not transactions:
        data["transactions"] = transactions = []

    # Get roles for current user
    user_roles = set(frappe.get_roles())

    # Apply rules for the first matching role
    for role, rules in ROLE_DASHBOARD_RULES.items():
        if role in user_roles:

            # --------------------------
            # REMOVE items
            # --------------------------
            remove_list = set(rules.get("remove", []))
            
            def should_remove_item(item):
                """Check if item should be removed - handles both string and dict formats"""
                if isinstance(item, str):
                    return item in remove_list
                elif isinstance(item, dict):
                    # Check if item name/doctype matches any in remove_list
                    item_name = item.get("name") or item.get("doctype") or item.get("label")
                    return item_name in remove_list
                return False
            
            for section in transactions:
                section["items"] = [
                    item for item in section.get("items", [])
                    if not should_remove_item(item)
                ]

            # --------------------------
            # ADD new items
            # --------------------------
            additions = rules.get("add", {})

            for label, doctypes_to_add in additions.items():
                # Check if section already exists
                section = next((sec for sec in transactions if sec.get("label") == label), None)
                if section:
                    existing_items = section.get("items", [])
                    # Get existing item names (handle both string and dict formats)
                    existing_names = set()
                    for item in existing_items:
                        if isinstance(item, str):
                            existing_names.add(item)
                        elif isinstance(item, dict):
                            existing_names.add(item.get("name") or item.get("doctype") or item.get("label"))
                    
                    # Add new items that don't already exist
                    for dt in doctypes_to_add:
                        if dt not in existing_names:
                            section["items"].append(dt)
                else:
                    # Create a new section
                    transactions.append({
                        "label": label,
                        "items": doctypes_to_add
                    })

            break   # Stop after applying first matching role

    return data
