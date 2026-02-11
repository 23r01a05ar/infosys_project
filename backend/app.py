from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
from preprocessing import preprocess_image

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/upload-image", methods=["POST"])
def upload_image():

    if "image" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file format"}), 400

    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)

    if file_size > MAX_FILE_SIZE:
        return jsonify({"error": "File size exceeds 10MB limit"}), 400

    unique_id = str(uuid.uuid4())
    extension = file.filename.rsplit(".", 1)[1].lower()
    filename = f"{unique_id}.{extension}"

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # ⭐ Preprocessing pipeline
    preprocess_image(filepath)

    return jsonify({
        "message": "Image uploaded successfully",
        "image_id": unique_id
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
