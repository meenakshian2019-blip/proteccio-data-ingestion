import re
import time

# REGEX PATTERNS
# Precompiled regex patterns for optimized performance

PATTERNS = {
    "email": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),

    "phone": re.compile(r"\b\d{10}\b"),

    "aadhaar": re.compile(r"\b\d{4}\s?\d{4}\s?\d{4}\b"),

    "pan": re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b"),

    "passport": re.compile(r"\b[A-Z]{1}[0-9]{7}\b"),

    "ip_address": re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"),

    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),

    "bank_account": re.compile(r"\b\d{9,18}\b")
}


# MASK SENSITIVE VALUES

def mask_value(value):

    value = str(value)

    if len(value) <= 4:
        return "*" * len(value)

    return value[:2] + "*" * (len(value) - 4) + value[-2:]


# DETECT SENSITIVE DATA

def discover_sensitive_data(data):

    start_time = time.time()

    detections = []

    if isinstance(data, dict):

        for field, value in data.items():

            value_str = str(value)

            for detection_type, pattern in PATTERNS.items():

                matches = pattern.findall(value_str)

                if matches:

                    for match in matches:

                        detections.append({
                            "field": field,
                            "type": detection_type,
                            "value": mask_value(match),
                            "confidence": 0.95
                        })

    duration = round(time.time() - start_time, 2)

    result = {
        "total_detections": len(detections),
        "processing_time_seconds": duration,
        "detections": detections
    }

    return result