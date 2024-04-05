def is_allowed_file_extension(file):
    allowed_extensions = {"mp3", "mp4", "mpeg", "wav", " m4a", "webm"}
    if (
        "." not in file.filename
        or file.filename.rsplit(".", 1)[1].lower() in allowed_extensions
    ):
        return True
    return False
