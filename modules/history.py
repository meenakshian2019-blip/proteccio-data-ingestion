import json
import os
from datetime import datetime
from flask import jsonify

HISTORY_FILE = "logs/history.json"


def ensure_history_file():
    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)


def add_history(source, status, details):
    """
    Add new history record
    """

    ensure_history_file()

    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)

    entry = {
        "timestamp": str(datetime.now()),
        "source": source,
        "status": status,
        "details": details
    }

    data.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_history():
    """
    Return full ingestion history
    """

    ensure_history_file()

    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)

    return jsonify(data)