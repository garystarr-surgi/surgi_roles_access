// Role-based dashboard customization for Customer
frappe.ui.form.on('Customer', {
	onload: function(frm) {
		// Get user roles
		const user_roles = frappe.user_roles || [];
		
		// Role-based dashboard rules
		const ROLE_DASHBOARD_RULES = {
			"Sales User": {
				remove: [
					"Sales Invoice",
					"Installation Note"
				],
				add: {
					"Service": ["Warranty Claim"]
				}
			}
		};
		
		// Apply rules for the first matching role
		for (const role in ROLE_DASHBOARD_RULES) {
			if (user_roles.includes(role)) {
				const rules = ROLE_DASHBOARD_RULES[role];
				
				// Function to apply dashboard customizations
				const applyDashboardRules = () => {
					// Remove items - try multiple selectors to catch different DOM structures
					if (rules.remove && rules.remove.length > 0) {
						rules.remove.forEach(doctype => {
							// Try various selectors to hide the items
							$(`[data-doctype='${doctype}']`).hide();
							$(`[data-doctype='${doctype}']`).parent().hide();
							$(`[data-doctype='${doctype}']`).closest('.dashboard-item').hide();
							$(`[data-doctype='${doctype}']`).closest('li').hide();
							$(`a[data-doctype='${doctype}']`).closest('.dashboard-item').hide();
							$(`a[data-doctype='${doctype}']`).parent().hide();
						});
					}
					
					// Add items - find Service section and add Warranty Claim
					if (rules.add && rules.add["Service"]) {
						const service_section = $('.dashboard-section').filter(function() {
							return $(this).text().includes('Service');
						}).first();
						
						if (service_section.length) {
							rules.add["Service"].forEach(doctype => {
								// Check if already exists
								if ($(`[data-doctype='${doctype}']`).length === 0) {
									// Find items container in service section
									const items_container = service_section.find('.dashboard-items, .list-item-container, ul').first();
									if (items_container.length) {
										// Create new item - try to match existing structure
										const existing_item = items_container.find('[data-doctype]').first();
										if (existing_item.length) {
											const new_item = existing_item.clone();
											new_item.attr('data-doctype', doctype);
											new_item.find('a').attr('data-doctype', doctype).text(doctype);
											new_item.find('a').on('click', function(e) {
												e.preventDefault();
												frappe.set_route('List', doctype, { customer: frm.doc.name });
											});
											items_container.append(new_item);
										}
									}
								}
							});
						}
					}
				};
				
				// Apply rules after dashboard is rendered
				// Use multiple timeouts to catch different render stages
				setTimeout(applyDashboardRules, 10);
				setTimeout(applyDashboardRules, 100);
				setTimeout(applyDashboardRules, 500);
				setTimeout(applyDashboardRules, 1000);
				
				// Also apply when dashboard refreshes
				if (frm.dashboard && frm.dashboard.refresh) {
					const original_refresh = frm.dashboard.refresh.bind(frm.dashboard);
					frm.dashboard.refresh = function() {
						const result = original_refresh();
						setTimeout(applyDashboardRules, 100);
						return result;
					};
				}
				
				// Watch for DOM changes (dashboard might load asynchronously)
				const observer = new MutationObserver(function(mutations) {
					applyDashboardRules();
				});
				
				// Observe the form container for changes
				if (frm.$wrapper && frm.$wrapper[0]) {
					observer.observe(frm.$wrapper[0], {
						childList: true,
						subtree: true
					});
				}
				
				break; // Stop after first matching role
			}
		}
	}
});

