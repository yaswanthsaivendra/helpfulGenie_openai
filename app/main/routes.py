import os

from flask import jsonify, request, send_file

from . import main_bp
from .openai_api import question_to_answer, speech_to_text, text_to_speech
from .utils import is_allowed_file_extension


@main_bp.route("/")
def index():
    return jsonify({"message": "Hello, world!"})


@main_bp.route("/upload", methods=["POST"])
def upload_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty file provided"}), 400

    if not is_allowed_file_extension(file):
        return jsonify({"error": "Invalid file format"}), 400

    # Save the file
    file_path = os.path.dirname(__file__) + "/input_audio/" + file.filename
    file.save(file_path)

    # Convert the question audio to text
    transcription_text = speech_to_text(file_path)

    # reply with answer in text format to the question in text format
    content = question_to_answer(transcription_text)

    speech_file_path = os.path.dirname(__file__) + "/output_audio/" + file.filename

    # Convert the answer in text format to speech
    text_to_speech(speech_file_path, content)

    return send_file(speech_file_path, as_attachment=True)
