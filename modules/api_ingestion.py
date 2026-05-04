import requests
from flask import jsonify
from modules.history import add_history


def ingest_api(request):
    """
    Ingest data from external API
    """

    try:
        data = request.get_json()

        url = data.get("url")
        method = data.get("method", "GET").upper()
        headers = data.get("headers", {})
        payload = data.get("payload", {})

        if not url:
            return jsonify({"error": "URL is required"}), 400

        # GET request
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=10)

        # POST request
        elif method == "POST":
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=10
            )

        else:
            return jsonify({"error": "Only GET and POST supported"}), 400

        result = response.json()

        add_history(
            source="External API",
            status="SUCCESS",
            details=f"Fetched data from {url}"
        )

        return jsonify({
            "message": "API data fetched successfully",
            "records": result
        })

    except Exception as e:
        add_history(
            source="External API",
            status="FAILED",
            details=str(e)
        )

        return jsonify({
            "error": str(e)
        }), 500