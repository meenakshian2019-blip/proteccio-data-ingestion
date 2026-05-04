from flask import Flask, jsonify, request
from modules.uploader import upload_file
from modules.scheduler import start_scheduler
from modules.history import get_history
from modules.normalizer import normalize

from connectors.sqlite_connector import init_db, get_tables
from connectors.s3_connector import list_buckets, list_files

from modules.api_ingestion import ingest_api
from modules.retry import run_retry_jobs

app = Flask(__name__)


# Home Route

@app.route("/")
def home():
    return jsonify({
        "message": "Proteccio Discover Running Successfully"
    })


# Health Check

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })



# SQLite DB Routes

@app.route("/db/init")
def db_init():
    return init_db()


@app.route("/db/tables")
def db_tables():
    return get_tables()



# File Upload Route

@app.route("/upload", methods=["POST"])
def upload():
    return upload_file(request)



# S3 Routes

@app.route("/s3/buckets")
def s3_buckets():
    return list_buckets()


@app.route("/s3/files/<bucket>")
def s3_bucket_files(bucket):
    return list_files(bucket)



# External API Ingestion

@app.route("/api/ingest", methods=["POST"])
def api_ingest():
    return ingest_api(request)



# Retry Failed Jobs

@app.route("/retry/run", methods=["POST"])
def retry_jobs():
    return run_retry_jobs()



# History Route

@app.route("/history")
def history():
    return get_history()


# Test Normalizer

@app.route("/normalize/test", methods=["POST"])
def test_normalizer():
    data = request.get_json()
    result = normalize(data)
    return jsonify(result)



# Start Scheduler

start_scheduler()


# Main

if __name__ == "__main__":
    app.run(debug=True)