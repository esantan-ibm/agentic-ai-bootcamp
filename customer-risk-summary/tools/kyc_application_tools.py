###list_pending_kyc_applications_tool

from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock data: list of pending KYC applications
mock_pending_kyc_applications = [
    {
        "applicant_name": "Ryan Hogan",
        "application_id": "KYC10234",
        "application_type": "Loan",
        "date_submitted": "2025-07-31",
        "status": "Pending"
    },
    {
        "applicant_name": "Priya Raizada",
        "application_id": "KYC10235",
        "application_type": "Credit Card",
        "date_submitted": "2025-07-30",
        "status": "Pending"
    },
    {
        "applicant_name": "Ahmad Saleh",
        "application_id": "KYC10236",
        "application_type": "Overdraft",
        "date_submitted": "2025-07-29",
        "status": "Pending"
    },
    {
        "applicant_name": "Emily Chen",
        "application_id": "KYC10237",
        "application_type": "Business Loan",
        "date_submitted": "2025-07-29",
        "status": "Pending"
    },
    {
        "applicant_name": "Liam Patel",
        "application_id": "KYC10238",
        "application_type": "Mortgage",
        "date_submitted": "2025-07-28",
        "status": "Pending"
    }
]

@tool()
def list_pending_kyc_applications_tool() -> str:
    """
    Returns a formatted string listing all pending KYC applications
    including applicant name, application ID, type, submission date, and status.
    """
    lines = [
        "| Applicant Name | Application ID | Type          | Date Submitted | Status  |",
        "|----------------|----------------|---------------|----------------|---------|"
    ]
    for app in mock_pending_kyc_applications:
        line = f"| {app['applicant_name']} | {app['application_id']} | {app['application_type']} | {app['date_submitted']} | {app['status']} |"
        lines.append(line)
    return "\n".join(lines)


### start_loan_application_review_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock data for applicant details
mock_loan_applications = {
    "KYC10234": {
        "applicant_name": "Ryan Hogan",
        "estimated_revenue": "$1.2M",
        "ownership": "Family-owned",
        "id_issued_by": "Ireland",
        "risk_level": "High"
    },
    "KYC10235": {
        "applicant_name": "Priya Raizada",
        "estimated_revenue": "$850K",
        "ownership": "Sole Proprietor",
        "id_issued_by": "India",
        "risk_level": "Medium"
    },
    "KYC10236": {
        "applicant_name": "Ahmad Saleh",
        "estimated_revenue": "$2.4M",
        "ownership": "Private Limited",
        "id_issued_by": "UAE",
        "risk_level": "High"
    },
    "KYC10237": {
        "applicant_name": "Emily Chen",
        "estimated_revenue": "$650K",
        "ownership": "LLC",
        "id_issued_by": "USA",
        "risk_level": "Low"
    },
    "KYC10238": {
        "applicant_name": "Liam Patel",
        "estimated_revenue": "$400K",
        "ownership": "Sole Proprietor",
        "id_issued_by": "UK",
        "risk_level": "Minimal"
    }
}

@tool()
def start_loan_application_review_tool(application_id: str) -> dict:
    """
    Returns key applicant details and initial risk level for a loan KYC application.
    If the application ID is not found, returns None.
    """
    return mock_loan_applications.get(application_id)


####kyc_requirements_summary_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock requirements, keyed by risk level
kyc_requirements = {
    "High": {
        "kyc_level": "High",
        "required_documents": [
            "Proof of identity",
            "Business registration",
            "Beneficial ownership declaration"
        ]
    },
    "Medium": {
        "kyc_level": "Medium",
        "required_documents": [
            "Proof of identity",
            "Business registration"
        ]
    },
    "Low": {
        "kyc_level": "Low",
        "required_documents": [
            "Proof of identity"
        ]
    },
    "Minimal": {
        "kyc_level": "Minimal",
        "required_documents": [
            "Proof of identity"
        ]
    }
}

@tool()
def kyc_requirements_summary_tool(risk_level: str) -> dict:
    """
    Returns KYC requirements and required document list based on applicant's risk level.
    If risk level not found, returns minimal requirements.
    """
    return kyc_requirements.get(risk_level, kyc_requirements["Minimal"])


###high_risk_trigger_explanation_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock reasons why an applicant is high risk
high_risk_triggers = {
    "KYC10234": [
        "Non-US nationality (Ireland)",
        "Revenue > $1M",
        "Loan amount > $1M"
    ],
    "KYC10236": [
        "Non-US nationality (UAE)",
        "Revenue > $2M",
        "Multiple large overdraft lines"
    ]
}

@tool()
def high_risk_trigger_explanation_tool(application_id: str) -> list:
    """
    Returns a list of triggers or conditions for why the applicant is classified as high risk.
    If no triggers are recorded, returns an empty list.
    """
    return high_risk_triggers.get(application_id, [])
