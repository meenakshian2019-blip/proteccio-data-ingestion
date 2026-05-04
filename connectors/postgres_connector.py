from flask import jsonify


def postgres_status():
    return jsonify({
        "message": "PostgreSQL connector ready. Add credentials in .env"
    })