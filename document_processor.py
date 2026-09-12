import os


def process_document(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return {
            "topic": "Document",
            "summary": text[:500],
            "key_facts": [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ],
            "dates": [],
            "locations": [],
            "entities": []
        }

    return {
        "topic": "Document",
        "summary": "Document format extraction not implemented yet.",
        "key_facts": [],
        "dates": [],
        "locations": [],
        "entities": []
    }