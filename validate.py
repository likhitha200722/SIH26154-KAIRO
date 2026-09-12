import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Output, Transformation, Document
from services.validation_service import validate_content


router = APIRouter(
    prefix="/validate",
    tags=["Validation"]
)


@router.post("/{output_id}")
def validate_output(
    output_id: int,
    db: Session = Depends(get_db)
):

    output = (
        db.query(Output)
        .filter(Output.id == output_id)
        .first()
    )

    if not output:
        raise HTTPException(
            status_code=404,
            detail="Output not found"
        )

    transformation = (
        db.query(Transformation)
        .filter(
            Transformation.id == output.transformation_id
        )
        .first()
    )

    document = (
        db.query(Document)
        .filter(
            Document.id == transformation.document_id
        )
        .first()
    )

    source_data = json.loads(
        document.extracted_data
    )

    result = validate_content(
        source_data,
        output.content
    )

    output.consistency_score = result["consistency_score"]

    output.validation_warnings = json.dumps(
        result["warnings"]
    )

    db.commit()

    return {
        "output_id": output.id,
        "consistency_score": output.consistency_score,
        "warnings": result["warnings"],
        "status": result["status"]
    }