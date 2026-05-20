# modules/compliance.py

COMPLIANCE_RULES = {
    "GDPR": {
        "email": "Personal email detected",
        "phone": "Phone number detected",
        "ip_address": "IP address detected"},

    "HIPAA": {
        "health_record": "Health-related data detected"},

    "PCI-DSS": {
        "credit_card": "Credit card information detected"},

    "DPDP": {
        "aadhaar": "Aadhaar information detected",
        "pan": "PAN information detected"}
}

def evaluate_compliance(detections):
    compliance_results = []
    total_issues = 0

    for regulation, rules in COMPLIANCE_RULES.items():
        issues_found = []

        for data_type, message in rules.items():
            if data_type in detections and detections[data_type]:
                issues_found.append(message)

        if issues_found:
            status = "At Risk"
            total_issues += len(issues_found)
        else:
            status = "Compliant"

        compliance_results.append({
            "regulation": regulation,
            "status": status,
            "issues": issues_found
        })

    compliance_score = max(0, 100 - (total_issues * 10))

    return {
        "compliance_results": compliance_results,
        "compliance_score": compliance_score
    }