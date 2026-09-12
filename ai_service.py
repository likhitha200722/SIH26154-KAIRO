from services.ai_engine import transform_content


def generate_content(
    source_data,
    audience,
    tone,
    language,
    detail_level,
    objective,
    output_type
):

    if isinstance(source_data, dict):

        source_text = ""

        if source_data.get("topic"):
            source_text += (
                "Topic: "
                + source_data["topic"]
                + "\n"
            )

        if source_data.get("summary"):
            source_text += (
                "Summary: "
                + source_data["summary"]
                + "\n"
            )

        if source_data.get("key_facts"):
            source_text += (
                "\nKey Facts:\n"
                + "\n".join(
                    source_data["key_facts"]
                )
                + "\n"
            )

    else:

        source_text = str(source_data)

    final_tone = (
        f"{tone}. "
        f"Detail level: {detail_level}"
    )

    generated_content = transform_content(
        source_text=source_text,
        audience=audience,
        tone=final_tone,
        language=language,
        objective=objective,
        output_type=output_type
    )

    return {
        "output_type": output_type,
        "content": generated_content
    }