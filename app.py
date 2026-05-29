import os
import json
import tempfile
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder=".")

UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {"mp3", "mp4", "wav", "m4a", "ogg", "flac", "webm", "mpeg", "mpga"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "Dosya bulunamadı"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Dosya seçilmedi"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Desteklenmeyen dosya formatı"}), 400

    try:
        import whisper
    except ImportError:
        return jsonify({"error": "Whisper yüklü değil. Lütfen 'pip install openai-whisper' komutunu çalıştırın."}), 500

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        model_name = request.form.get("model", "base")
        language = request.form.get("language", None)
        if language == "auto":
            language = None

        model = whisper.load_model(model_name)

        options = {}
        if language:
            options["language"] = language

        result = model.transcribe(filepath, **options)

        segments = []
        for seg in result.get("segments", []):
            segments.append({
                "start": round(seg["start"], 2),
                "end": round(seg["end"], 2),
                "text": seg["text"].strip()
            })

        return jsonify({
            "text": result["text"].strip(),
            "language": result.get("language", "bilinmiyor"),
            "segments": segments
        })

    except Exception as e:
        return jsonify({"error": f"Transkripsiyon hatası: {str(e)}"}), 500

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == "__main__":
    print("\n🎙️  Transkriptor başlatılıyor...")
    print("📌  Tarayıcınızda açın: http://localhost:5000\n")
    app.run(debug=False, host="0.0.0.0", port=5000)
