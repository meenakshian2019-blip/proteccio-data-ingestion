import time
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from modules.uploader import upload_file
from modules.scheduler import start_scheduler
from modules.history import get_history
from modules.normalizer import normalize

from connectors.sqlite_connector import init_db, get_tables
from connectors.s3_connector import list_buckets, list_files

from modules.api_ingestion import ingest_api
from modules.retry import run_retry_jobs

from modules.discovery import discover_sensitive_data
from modules.classifier import classify_data
from modules.risk_scoring import calculate_risk
from modules.profiler import profile_dataset
from modules.mapper import generate_data_mapping
from modules.audit import write_audit_log

from modules.search import (
    search_by_risk,
    search_by_classification,
    search_by_source,
    search_by_detection
)

from modules.dashboard import generate_dashboard_metrics

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

ANALYSIS_HISTORY = []

# API AUTHENTICATION

def authenticate_request(request):

    request_api_key = request.headers.get("x-api-key")

    if request_api_key != API_KEY:
        return False

    return True

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


# MAIN ANALYZE API

@app.route('/analyze', methods=['POST'])
def analyze_data():
    if not authenticate_request(request):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    start_time = time.time()

    try:

        data = request.json

        if "data" not in data:

            return jsonify({
                "error": "Missing data field"
            }), 400

        if not data:
            return jsonify({
                "error": "No JSON data provided"
            }), 400

        # SOURCE DETAILS

        source_name = data.get(
            "source_name",
            "Unknown Source"
        )

        source_type = data.get(
            "source_type",
            "API"
        )

        records = data.get("data", {})

        # DISCOVERY

        discovery_results = discover_sensitive_data(records)

        # CLASSIFICATION

        classification_results = classify_data(
            discovery_results
        )

        # RISK SCORING

        risk_results = calculate_risk(
            classification_results
        )

        # PROFILING

        profile_results = profile_dataset(
            records,
            classification_results,
            risk_results
        )

        # DATA MAPPING

        mapping_results = generate_data_mapping(
            source_name,
            source_type,
            classification_results,
            risk_results
        )

        duration = round(time.time() - start_time, 2)

        # AUDIT LOG

        write_audit_log(
            action="analyze",
            source=source_name,
            status="success",
            duration=duration,
            message="Privacy analysis completed"
        )

        ANALYSIS_HISTORY.append({

            "discovery": discovery_results,

            "classification": classification_results,

            "risk_analysis": risk_results,

            "profiling": profile_results,

            "mapping": mapping_results
        })

        # FINAL RESPONSE

        return jsonify({

            "discovery": discovery_results,

            "classification": classification_results,

            "risk_analysis": risk_results,

            "profiling": profile_results,

            "mapping": mapping_results
        })

    except Exception as e:

        duration = round(time.time() - start_time, 2)

        write_audit_log(
            action="analyze",
            source="Unknown",
            status="failed",
            duration=duration,
            message=str(e)
        )

        return jsonify({
            "error": str(e)
        }), 500
    

# SEARCH BY RISK

@app.route('/search/risk', methods=['GET'])
def search_risk():
    if not authenticate_request(request):

        return jsonify({
            "error": "Unauthorized"
        }), 401
    
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    level = request.args.get("level")

    results = search_by_risk(
        ANALYSIS_HISTORY,
        level
    )

    start = (page - 1) * per_page
    end = start + per_page

    paginated_results = results[start:end]

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total_results": len(results),
        "results": paginated_results
    })


# SEARCH BY CLASSIFICATION

@app.route('/search/classification', methods=['GET'])
def search_classification():
    if not authenticate_request(request):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    classification = request.args.get(
        "type"
    )

    results = search_by_classification(
        ANALYSIS_HISTORY,
        classification
    )

    return jsonify(results)

# SEARCH BY SOURCE

@app.route('/search/source', methods=['GET'])
def search_source():
    if not authenticate_request(request):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    source = request.args.get("name")

    results = search_by_source(
        ANALYSIS_HISTORY,
        source
    )

    return jsonify(results)

# SEARCH BY DETECTION

@app.route('/search/detection', methods=['GET'])
def search_detection():
    if not authenticate_request(request):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    detection = request.args.get("type")

    results = search_by_detection(
        ANALYSIS_HISTORY,
        detection
    )

    return jsonify(results)

# DASHBOARD METRICS

@app.route('/dashboard/metrics', methods=['GET'])
def dashboard_metrics():
    if not authenticate_request(request):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    metrics = generate_dashboard_metrics(
        ANALYSIS_HISTORY
    )

    return jsonify(metrics)


# Main

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)