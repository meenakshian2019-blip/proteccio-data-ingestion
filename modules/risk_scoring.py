# RISK SCORES

RISK_SCORES = {

    "Personal Data": 2,

    "Sensitive Personal Data": 5,

    "Financial Data": 5,

    "Authentication Data": 5,

    "Public Data": 1
}


# CALCULATE RISK LEVEL

def calculate_risk(classification_results):

    classified_data = classification_results.get("classified_data", [])

    total_score = 0

    classifications_found = []

    for item in classified_data:

        classification = item.get("classification")

        classifications_found.append(classification)

        total_score += RISK_SCORES.get(classification, 1)

    # DETERMINE RISK LEVEL

    if total_score <= 2:
        risk_level = "Low"

    elif total_score <= 5:
        risk_level = "Medium"

    elif total_score <= 8:
        risk_level = "High"

    else:
        risk_level = "Critical"

    result = {
        "risk_level": risk_level,
        "risk_score": total_score,
        "classifications_found": list(set(classifications_found))
    }

    return result