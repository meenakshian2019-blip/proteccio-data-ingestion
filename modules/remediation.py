# modules/remediation.py

REMEDIATION_STEPS = {
    "email": "Mask or encrypt email addresses",
    "phone": "Apply phone number masking",
    "aadhaar": "Encrypt Aadhaar data",
    "pan": "Restrict PAN access",
    "credit_card": "Tokenize card information",
    "bank_account": "Enable secure banking encryption",
    "passport": "Restrict passport visibility"
}


def generate_remediation(detections):

    recommendations = []

    for data_type in detections:

        if data_type in REMEDIATION_STEPS:

            recommendations.append({
                "data_type": data_type,
                "recommendation": REMEDIATION_STEPS[data_type],
                "status": "Open"
            })

    return {
        "remediation_plan": recommendations,
        "total_recommendations": len(recommendations)
    }