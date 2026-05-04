from flask import jsonify


def mongo_status():
    return jsonify({
        "message": "MongoDB connector ready. Add credentials in .env"
    })