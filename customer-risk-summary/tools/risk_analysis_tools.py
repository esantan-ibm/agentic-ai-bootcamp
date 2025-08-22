######risk_profile_summary_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock risk profile data for 5 customers
mock_risk_profiles = {
    "cust001": {
        "risk_score": 82,
        "risk_level": "Critical",
        "summary": "Multiple high-value late-night transactions; urgent review required."
    },
    "cust002": {
        "risk_score": 65,
        "risk_level": "High",
        "summary": "Frequent large cash-ins; matches risk indicators for gaming industry compliance checks."
    },
    "cust003": {
        "risk_score": 41,
        "risk_level": "Medium",
        "summary": "Occasional pattern changes; modest increase in transaction size."
    },
    "cust004": {
        "risk_score": 28,
        "risk_level": "Low",
        "summary": "Stable transaction behavior; no recent anomalies detected."
    },
    "cust005": {
        "risk_score": 13,
        "risk_level": "Minimal",
        "summary": "Low volumes and standard patterns; no flags raised."
    }
}

@tool()
def risk_profile_summary_tool(customer_id: str) -> dict:
    """
    Returns a summary of the customer's risk profile, including risk score, risk level, and a short summary.
    If customer_id is not found, returns data indicating a minimal risk profile.
    """
    return mock_risk_profiles.get(
        customer_id,
        {
            "risk_score": 10,
            "risk_level": "Minimal",
            "summary": "Customer not in database; no risk information available."
        }
    )

#########recent_transaction_review_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock transactions for 5 customers
mock_transactions = {
    "cust001": [
        {"date": "2025-07-30", "amount": 50000, "description": "Chip purchase", "risk_flag": True, "note": "Largest single transaction this month."},
        {"date": "2025-07-29", "amount": 17000, "description": "Cash advance", "risk_flag": True, "note": "Unusual amount for this profile."},
    ],
    "cust002": [
        {"date": "2025-07-28", "amount": 12000, "description": "Wire transfer", "risk_flag": False, "note": "Pattern consistent with prior behavior."},
        {"date": "2025-07-27", "amount": 8500, "description": "Chip redemption", "risk_flag": True, "note": "Multiple redemptions in 24 hours."},
    ],
    "cust003": [
        {"date": "2025-07-26", "amount": 2100, "description": "Table game wager", "risk_flag": False, "note": "Within standard range."},
        {"date": "2025-07-25", "amount": 4000, "description": "Slot play", "risk_flag": False, "note": "Slightly above average but non-suspicious."},
    ],
    "cust004": [
        {"date": "2025-07-24", "amount": 650, "description": "Restaurant bill", "risk_flag": False, "note": "Non-gaming spend."},
        {"date": "2025-07-22", "amount": 1500, "description": "Chip purchase", "risk_flag": False, "note": "Typical small buy-in."},
    ],
    "cust005": [
        {"date": "2025-07-21", "amount": 350, "description": "Gift shop", "risk_flag": False, "note": "No gaming risk."},
        {"date": "2025-07-19", "amount": 800, "description": "Token purchase", "risk_flag": False, "note": "Low-value, normal activity."},
    ]
}


@tool()
def recent_transaction_review_tool(customer_id: str) -> list:
    """
    Returns a list of recent transactions for a customer,
    tagging each with a risk flag and review note.
    Returns default non-risky activity if customer not found.
    """
    return mock_transactions.get(
        customer_id,
        [
            {"date": "2025-07-15", "amount": 200, "description": "ATM withdrawal", "risk_flag": False, "note": "No activity of concern."}
        ]
    )


####################transaction_pattern_analysis_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock pattern analysis for 5 customers
mock_patterns = {
    "cust001": {
        "pattern": "Large, frequent, late-night cash transactions.",
        "anomaly_detected": True,
        "details": "Transactions greatly exceed peer averages. Recommend immediate review."
    },
    "cust002": {
        "pattern": "Multiple chip redemptions across several days.",
        "anomaly_detected": True,
        "details": "Unusual for customer category; matches moderate-risk gaming activity."
    },
    "cust003": {
        "pattern": "Occasional larger bets, otherwise regular pattern.",
        "anomaly_detected": False,
        "details": "No persistent anomalies, but monitor for trend shifts."
    },
    "cust004": {
        "pattern": "Stable, low-value purchases. Non-gaming spending dominant.",
        "anomaly_detected": False,
        "details": "Consistent pattern with minimal risk."
    },
    "cust005": {
        "pattern": "Low-frequency, low-value gaming spend.",
        "anomaly_detected": False,
        "details": "Behavior fits low-risk, infrequent visitor."
    }
}

@tool()
def transaction_pattern_analysis_tool(customer_id: str) -> dict:
    """
    Provides a high-level pattern analysis of the customer's recent transactions,
    indicating whether anomalies or risky behaviors are detected. Returns minimal risk if not found.
    """
    return mock_patterns.get(
        customer_id,
        {
            "pattern": "Insufficient data to determine transaction patterns.",
            "anomaly_detected": False,
            "details": "Customer profile not recognized; no anomalies possible."
        }
    )
