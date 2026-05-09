# DASHBOARD METRICS

def generate_dashboard_metrics(results):

    total_scanned_records = len(results)

    total_sensitive_records = 0

    risk_distribution = {}

    classification_distribution = {}

    high_risk_sources = 0

    for item in results:

        # SENSITIVE RECORDS

        sensitive_count = item.get(
            "profiling",
            {}
        ).get("sensitive_record_count", 0)

        total_sensitive_records += sensitive_count

        # RISK DISTRIBUTION

        risk_level = item.get(
            "risk_analysis",
            {}
        ).get("risk_level", "Unknown")

        risk_distribution[risk_level] = (
            risk_distribution.get(risk_level, 0) + 1
        )

        # HIGH RISK COUNT

        if risk_level in ["High", "Critical"]:
            high_risk_sources += 1

        # CLASSIFICATION DISTRIBUTION

        classified_data = item.get(
            "classification",
            {}
        ).get("classified_data", [])

        for classified_item in classified_data:

            classification = classified_item.get(
                "classification",
                "Unknown"
            )

            classification_distribution[classification] = (
                classification_distribution.get(classification, 0) + 1
            )

    return {

        "total_scanned_records": total_scanned_records,

        "total_sensitive_records": total_sensitive_records,

        "risk_distribution": risk_distribution,

        "classification_distribution": classification_distribution,

        "high_risk_source_count": high_risk_sources
    }