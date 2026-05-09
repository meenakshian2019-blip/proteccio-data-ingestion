import json
import os
from datetime import datetime

# LOG FILE PATH

LOG_FOLDER = "logs"

LOG_FILE = os.path.join(LOG_FOLDER, "audit.log")

os.makedirs(LOG_FOLDER, exist_ok=True)


# WRITE AUDIT LOG

def write_audit_log(
    action,
    source,
    status,
    duration,
    message="Internal processing error"
):

    log_entry = {

        "timestamp": str(datetime.now()),

        "action": action,

        "source": source,

        "status": status,

        "processing_duration_seconds": duration,

        "message": message
    }

    with open(LOG_FILE, "a") as file:

        file.write(json.dumps(log_entry) + "\n")

    return {
        "message": "Audit log created successfully"
    }