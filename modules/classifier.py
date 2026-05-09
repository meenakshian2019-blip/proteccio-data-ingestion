# CLASSIFICATION MAPPING

CLASSIFICATION_MAP = {

    "email": {
        "classification": "Personal Data",
        "confidence": 0.95
    },

    "phone": {
        "classification": "Personal Data",
        "confidence": 0.93
    },

    "aadhaar": {
        "classification": "Sensitive Personal Data",
        "confidence": 0.99
    },

    "pan": {
        "classification": "Sensitive Personal Data",
        "confidence": 0.98
    },

    "passport": {
        "classification": "Sensitive Personal Data",
        "confidence": 0.97
    },

    "credit_card": {
        "classification": "Financial Data",
        "confidence": 0.99
    },

    "bank_account": {
        "classification": "Financial Data",
        "confidence": 0.95
    },

    "ip_address": {
        "classification": "Personal Data",
        "confidence": 0.85
    }
}


# CLASSIFY DETECTED DATA

def classify_data(discovery_results):

    classified_results = []

    detections = discovery_results.get("detections", [])

    for item in detections:

        detection_type = item.get("type")

        classification_info = CLASSIFICATION_MAP.get(
            detection_type,
            {
                "classification": "Public Data",
                "confidence": 0.50
            }
        )

        classified_item = {
            "field": item.get("field"),
            "type": detection_type,
            "classification": classification_info["classification"],
            "confidence": classification_info["confidence"],
            "masked_value": item.get("value")
        }

        classified_results.append(classified_item)

    return {
        "total_classified": len(classified_results),
        "classified_data": classified_results
    }