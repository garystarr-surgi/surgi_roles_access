app_name = "surgi_roles_access"
app_title = "Surgi Roles Access"
app_publisher = "SurgiShop"
app_description = "Role-based dashboard and access customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# ------------------------------
# Override Customer dashboard
# ------------------------------
override_doctype_dashboards = {
    "Customer": "surgi_roles_access.dashboard.customer_dashboard.get_data"
}

