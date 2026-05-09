import pandas as pd

# PROFILE DATASET

def profile_dataset(data, classified_results, risk_results):

    # CONVERT TO DATAFRAME

    df = pd.DataFrame([data])

    total_records = len(df)

    total_columns = len(df.columns)

    null_values = int(df.isnull().sum().sum())

    duplicate_records = int(df.duplicated().sum())

    unique_records = int(df.nunique().sum())

    # CLASSIFICATION DISTRIBUTION

    classification_distribution = {}

    classified_data = classified_results.get("classified_data", [])

    for item in classified_data:

        classification = item.get("classification")

        classification_distribution[classification] = (
            classification_distribution.get(classification, 0) + 1
        )

    # RISK DISTRIBUTION

    risk_distribution = {
        risk_results.get("risk_level"): 1
    }

    # SENSITIVE DATA DENSITY

    sensitive_count = len(classified_data)

    if total_columns > 0:
        sensitive_density = round(
            (sensitive_count / total_columns) * 100,
            2
        )
    else:
        sensitive_density = 0

    # FINAL PROFILE

    profile = {

        "total_records": total_records,

        "total_columns": total_columns,

        "null_values": null_values,

        "duplicate_records": duplicate_records,

        "unique_records": unique_records,

        "sensitive_record_count": sensitive_count,

        "sensitive_data_density_percent": sensitive_density,

        "classification_distribution": classification_distribution,

        "risk_distribution": risk_distribution
    }

    return profile