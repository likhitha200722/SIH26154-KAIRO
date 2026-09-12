import os
import re

from services.output_engine import MultiFormatOutputEngine


def convert_to_structured_content(content, output_type):
    """
    Convert the AI-generated text into the structure
    expected by Person 5's output engine.
    """

    lines = content.splitlines()

    title = output_type.title()

    sections = []
    current_section = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Remove Markdown formatting
        clean_line = re.sub(r"\*\*", "", line).strip()

        # Detect headings
        if clean_line.startswith("#"):
            heading = clean_line.lstrip("#").strip()

            if heading:
                current_section = {
                    "heading": heading,
                    "points": []
                }
                sections.append(current_section)

        # Detect bullet points
        elif clean_line.startswith(("* ", "- ", "• ")):
            point = clean_line[2:].strip()

            if current_section is None:
                current_section = {
                    "heading": "Content",
                    "points": []
                }
                sections.append(current_section)

            current_section["points"].append(point)

        else:
            # First normal line becomes the title
            if not sections and title == output_type.title():
                title = clean_line

            elif current_section is None:
                current_section = {
                    "heading": "Content",
                    "points": []
                }
                sections.append(current_section)

            else:
                current_section["points"].append(clean_line)

    # Safety fallback
    if not sections:
        sections.append({
            "heading": "Content",
            "points": [content]
        })

    return {
        "title": title,
        "sections": sections
    }


def generate_export(content, output_type, format_type):

    # Convert AI-generated content into Person 5 format
    structured_content = convert_to_structured_content(
        content,
        output_type
    )

    # Create Person 5 output engine
    engine = MultiFormatOutputEngine(
        structured_content
    )

    # Generate requested format
    format_type = format_type.upper()

    if format_type == "TXT":
        file_path = engine.create_txt()

    elif format_type == "DOCX":
        file_path = engine.create_docx()

    elif format_type == "PPTX":
        file_path = engine.create_ppt()

    elif format_type == "PDF":
        file_path = engine.create_pdf()

    else:
        raise ValueError(
            "Unsupported format. Use TXT, DOCX, PPTX or PDF."
        )

    return {
        "status": "generated",
        "file_path": file_path
    }
    