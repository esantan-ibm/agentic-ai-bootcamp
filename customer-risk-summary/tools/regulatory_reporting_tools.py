from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock compliance reports keyed by type
mock_reports = {
    "cust001": {
        "report_id": "REP2001",
        "report_type": "Suspicious Activity Report (SAR)",
        "customer_id": "cust001",
        "summary": "Large late-night cash transactions and high-value chip purchases inconsistent with profile.",
        "status": "Draft"
    },
    "cust002": {
        "report_id": "REP2002",
        "report_type": "Suspicious Activity Report (SAR)",
        "customer_id": "cust002",
        "summary": "Frequent chip redemptions and large transfers flagged for AML review.",
        "status": "Draft"
    },
    "cust003": {
        "report_id": "REP2003",
        "report_type": "Audit Summary Report",
        "customer_id": "cust003",
        "summary": "Medium risk activity with occasional spikes. No SAR required but monitoring ongoing.",
        "status": "Completed"
    },
    "cust004": {
        "report_id": "REP2004",
        "report_type": "Audit Summary Report",
        "customer_id": "cust004",
        "summary": "Low-risk transactions. No anomalies detected this period.",
        "status": "Completed"
    },
    "cust005": {
        "report_id": "REP2005",
        "report_type": "Routine Compliance Report",
        "customer_id": "cust005",
        "summary": "Minimal activity, no suspicious indicators. No SAR required.",
        "status": "Completed"
    }
}

@tool()
def report_generator_tool(customer_id: str) -> str:
    """
    Returns a formatted table with the compliance or SAR report for the given customer_id.
    """
    key = customer_id.lower()
    report = mock_reports.get(
        key,
        {
            "report_id": "REP9999",
            "report_type": "Routine Compliance Report",
            "customer_id": customer_id,
            "summary": "Customer not in database; no suspicious activity detected.",
            "status": "Completed"
        }
    )

    lines = [
        "| Report ID | Type                         | Customer | Status    | Summary |",
        "|-----------|------------------------------|----------|-----------|---------|",
        f"| {report['report_id']} | {report['report_type']} | {report['customer_id']} | {report['status']} | {report['summary']} |"
    ]
    return "\n".join(lines)


mock_audit_logs = {
    "cust001": [
        {"timestamp": "2025-07-30", "event": "SAR draft generated"},
        {"timestamp": "2025-07-29", "event": "High-value transaction flagged"},
        {"timestamp": "2025-07-27", "event": "Pattern anomaly detected"}
    ],
    "cust002": [
        {"timestamp": "2025-07-28", "event": "Chip redemption flagged"},
        {"timestamp": "2025-07-27", "event": "AML check performed"}
    ],
    "cust003": [
        {"timestamp": "2025-07-25", "event": "Transaction review completed"},
        {"timestamp": "2025-07-24", "event": "No anomalies detected"}
    ],
    "cust004": [
        {"timestamp": "2025-07-22", "event": "Low-risk customer — minimal activity"},
        {"timestamp": "2025-07-20", "event": "Routine KYC check"}
    ],
    "cust005": [
        {"timestamp": "2025-07-19", "event": "Gift shop spend logged"},
        {"timestamp": "2025-07-18", "event": "No suspicious activity"}
    ]
}

@tool()
def audit_log_search_tool(customer_id: str) -> str:
    """
    Returns a formatted table of audit log entries for the specified customer ID.
    """
    logs = mock_audit_logs.get(customer_id, [])
    if not logs:
        return f"No audit logs found for {customer_id}"

    lines = [
        "| Timestamp  | Event                          |",
        "|------------|-------------------------------|"
    ]
    for entry in logs:
        line = f"| {entry['timestamp']} | {entry['event']} |"
        lines.append(line)

    return "\n".join(lines)