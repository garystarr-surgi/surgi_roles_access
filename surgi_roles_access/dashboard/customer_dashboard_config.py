# ----------------------------------------
# Role-based dashboard rules
# ----------------------------------------

ROLE_DASHBOARD_RULES = {
    "Sales User": {
        "remove": [
            "Sales Invoice",
            "Installation Note"
        ],
        "add": {
            "Service": ["Warranty Claim"]
        }
    }

    # Add future roles here
    # Example:
    # "Customer Service": {
    #     "remove": ["Sales Order", "Address"],
    #     "add": {
    #         "Support": ["Issue", "Warranty Claim"]
    #     }
    # }
}
