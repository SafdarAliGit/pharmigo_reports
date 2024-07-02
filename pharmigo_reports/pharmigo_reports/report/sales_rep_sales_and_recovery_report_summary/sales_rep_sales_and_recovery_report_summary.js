frappe.query_reports["Sales Rep Sales And Recovery Report Summary"] = {
    "filters": [

        {
            label: __("From Date"),
            fieldname: "from_date",
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            reqd: 1
        },
        {
            label: __("To Date"),
            fieldname: "to_date",
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
            reqd: 1
        },

    ]
};