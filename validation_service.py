from services.verifier import DocumentVerifier


def validate_content(source_data, generated_content):

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
                "\n".join(source_data["key_facts"])
                + "\n"
            )

    else:

        source_text = str(source_data)

    verifier = DocumentVerifier(threshold=0.70)

    verification_report = (
        verifier.verify_generated_content(
            source_text,
            generated_content
        )
    )

    if verification_report:

        average_score = (
            sum(
                item["similarity_score"]
                for item in verification_report
            )
            / len(verification_report)
        )

        consistency_score = round(
            average_score * 100
        )

    else:

        consistency_score = 0

    warnings = []

    for item in verification_report:

        if item["status"] != "VERIFIED":

            warnings.append({
                "claim": item["claim"],
                "status": item["status"],
                "similarity_score": item["similarity_score"]
            })

    if not warnings:

        status = "verified"

    else:

        status = "warnings"

    return {
        "consistency_score": consistency_score,
        "warnings": warnings,
        "status": status
    }