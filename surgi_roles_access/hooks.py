app_name = "surgi_roles_access"
app_title = "Surgi Roles Access"
app_publisher = "SurgiShop"
app_description = "Role-based dashboard and access customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# ------------------------------
# Include JavaScript files
# ------------------------------
app_include_js = [
    "public/js/customer_dashboard.js"
]

# ------------------------------
# Override Customer dashboard (Python approach for adding items)
# ------------------------------
override_doctype_dashboards = {
    "Customer": "surgi_roles_access.dashboard.customer_dashboard.get_data"
}
