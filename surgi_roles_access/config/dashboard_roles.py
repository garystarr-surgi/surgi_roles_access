ROLE_DASHBOARD_CONFIG = {
    "Sales User": {
        "allow": ["Warranty Claim", "Delivery Note"],
        "deny": ["Sales Invoice", "Installation Note"]
    },
    "Support User": {
        "allow": ["Warranty Claim"],
        "deny": []
    },
    # Add more roles here as needed
}
