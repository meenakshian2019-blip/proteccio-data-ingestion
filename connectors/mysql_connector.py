from flask import jsonify


def mysql_status():
    return jsonify({
        "message": "MySQL connector ready. Add credentials in .env"
    })