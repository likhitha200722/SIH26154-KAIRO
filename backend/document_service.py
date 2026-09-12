import os
import shutil
import uuid


UPLOAD_DIRECTORY = "uploads"

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}


def save_uploaded_file(file):

    filename = file.filename

    extension = os.path.splitext(
        filename
    )[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise ValueError(
            "Only PDF, DOCX and TXT files are allowed"
        )

    unique_filename = (
        f"{uuid.uuid4()}{extension}"
    )

    os.makedirs(
        UPLOAD_DIRECTORY,
        exist_ok=True
    )

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        unique_filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return file_path
