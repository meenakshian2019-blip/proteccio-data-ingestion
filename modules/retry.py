from flask import jsonify
from modules.history import add_history
import time


def run_retry_jobs():
    """
    Simulate retrying failed jobs
    """

    try:
        # Example retry process
        time.sleep(1)

        add_history(
            source="Retry Engine",
            status="SUCCESS",
            details="Failed jobs retried successfully"
        )

        return jsonify({
            "message": "Retry jobs executed successfully"
        })

    except Exception as e:
        add_history(
            source="Retry Engine",
            status="FAILED",
            details=str(e)
        )

        return jsonify({
            "error": str(e)
        }), 500