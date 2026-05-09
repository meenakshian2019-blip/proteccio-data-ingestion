# SEARCH FUNCTIONS

def search_by_risk(results, risk_level):

    matched = []

    for item in results:

        if item.get("risk_analysis", {}).get("risk_level") == risk_level:
            matched.append(item)

    return matched


def search_by_classification(results, classification):

    matched = []

    for item in results:

        classified_data = item.get(
            "classification",
            {}
        ).get("classified_data", [])

        for classified_item in classified_data:

            if classified_item.get("classification") == classification:

                matched.append(item)
                break

    return matched


def search_by_source(results, source_name):

    matched = []

    for item in results:

        mappings = item.get(
            "mapping",
            {}
        ).get("mappings", [])

        for mapping in mappings:

            if mapping.get("source_name") == source_name:

                matched.append(item)
                break

    return matched


def search_by_detection(results, detection_type):

    matched = []

    for item in results:

        detections = item.get(
            "discovery",
            {}
        ).get("detections", [])

        for detection in detections:

            if detection.get("type") == detection_type:

                matched.append(item)
                break

    return matched