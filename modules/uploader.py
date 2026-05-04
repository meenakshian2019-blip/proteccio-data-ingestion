import os
import uuid
from flask import jsonify
from werkzeug.utils import secure_filename

from modules.metadata import get_metadata
from modules.history import add_history
from modules.security import encrypt_text

UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 500 * 1024 * 1024

ALLOWED_EXTENSIONS = {
    "csv",
    "xlsx",
    "pdf",
    "pst",
    "ost",
    "txt",
    "json"
}


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(request):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    file.seek(0, 2)
    size = file.tell()
    file.seek(0)

    if size > MAX_FILE_SIZE:
        return jsonify({"error": "File exceeds 500MB"}), 400

    filename = secure_filename(file.filename)
    ext = filename.split(".")[-1]

    unique_name = f"{uuid.uuid4()}.{ext}"
    filepath = os.path.join(UPLOAD_FOLDER, unique_name)

    file.save(filepath)

    metadata = get_metadata(filepath)

    encrypted_id = encrypt_text(unique_name)

    add_history(
        source="File Upload",
        status="SUCCESS",
        details=f"{unique_name} uploaded securely"
    )

    return jsonify({
        "message": "File uploaded successfully",
        "encrypted_file_id": encrypted_id,
        "metadata": metadata
    })