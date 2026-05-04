import sqlite3
from flask import jsonify

DB_NAME = "proteccio.db"


def get_connection():
    return sqlite3.connect(DB_NAME, timeout=5)


def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            )
        """)

        conn.commit()
        conn.close()

        return jsonify({
            "message": "Database initialized successfully"
        })

    except sqlite3.OperationalError as e:
        return jsonify({
            "error": f"Database timeout/lock issue: {str(e)}"
        }), 500


def get_tables():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table'
        """)

        tables = [row[0] for row in cursor.fetchall()]

        conn.close()

        return jsonify({
            "tables": tables
        })

    except sqlite3.OperationalError as e:
        return jsonify({
            "error": f"Database timeout/lock issue: {str(e)}"
        }), 500