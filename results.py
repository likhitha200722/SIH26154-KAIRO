import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Document, Transformation


router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


@router.get("/{document_id}")
def get_results(
    document_id: int,
    db: Session = Depends(get_db)
):

    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    transformations = (
        db.query(Transformation)
        .filter(
            Transformation.document_id == document_id
        )
        .all()
    )

    results = []

    for transformation in transformations:

        outputs = []

        for output in transformation.outputs:

            warnings = []

            if output.validation_warnings:
                warnings = json.loads(
                    output.validation_warnings
                )

            outputs.append({
                "output_id": output.id,
                "type": output.output_type,
                "content": output.content,
                "consistency_score": output.consistency_score,
                "warnings": warnings,
                "status": output.status
            })

        results.append({
            "transformation_id": transformation.id,
            "settings": {
                "audience": transformation.audience,
                "tone": transformation.tone,
                "language": transformation.language,
                "detail_level": transformation.detail_level,
                "objective": transformation.objective
            },
            "outputs": outputs
        })

    return {
        "document_id": document.id,
        "filename": document.filename,
        "status": document.status,
        "transformations": results
    }