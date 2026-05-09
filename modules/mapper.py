# DATA MAPPING ENGINE

def generate_data_mapping(
    source_name,
    source_type,
    classified_results,
    risk_results
):

    mappings = []

    classified_data = classified_results.get("classified_data", [])

    for item in classified_data:

        mapping = {

            "field": item.get("field"),

            "detection_type": item.get("type"),

            "classification": item.get("classification"),

            "risk_level": risk_results.get("risk_level"),

            "source_name": source_name,

            "source_type": source_type,

            "destination": "Proteccio Discover",

            "lineage": f"{source_name} -> Proteccio Discover"
        }

        mappings.append(mapping)

    return {
        "total_mappings": len(mappings),
        "mappings": mappings
    }