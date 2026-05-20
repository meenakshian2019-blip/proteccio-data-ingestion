# modules/reporting.py

import json
import csv
from datetime import datetime


def generate_json_report(data):

    filename = f"report_{datetime.now().timestamp()}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    return filename


def generate_csv_report(data):

    filename = f"report_{datetime.now().timestamp()}.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Key", "Value"])

        for key, value in data.items():
            writer.writerow([key, value])

    return filename