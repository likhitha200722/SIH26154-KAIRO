import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Document, Transformation, Output
from schemas.transformation import TransformationRequest
from services.ai_service import generate_content


router = APIRouter(
    prefix="/transform",
    tags=["AI Transformation"]
)


@router.post("/")
def transform_document(
    request: TransformationRequest,
    db: Session = Depends(get_db)
):

    document = (
        db.query(Document)
        .filter(Document.id == request.document_id)
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if not document.extracted_data:
        raise HTTPException(
            status_code=400,
            detail="Document must be analyzed first"
        )

    transformation = Transformation(
        document_id=request.document_id,
        audience=request.audience,
        tone=request.tone,
        language=request.language,
        detail_level=request.detail_level,
        objective=request.objective,
        status="processing"
    )

    db.add(transformation)
    db.commit()
    db.refresh(transformation)

    source_data = json.loads(
        document.extracted_data
    )

    generated_outputs = []

    try:

        for output_type in request.outputs:

            result = generate_content(
                source_data,
                request.audience,
                request.tone,
                request.language,
                request.detail_level,
                request.objective,
                output_type
            )

            output = Output(
                transformation_id=transformation.id,
                output_type=output_type,
                content=result["content"],
                status="generated"
            )

            db.add(output)
            db.commit()
            db.refresh(output)

            generated_outputs.append({
                "output_id": output.id,
                "output_type": output.output_type,
                "content": output.content
            })

        transformation.status = "completed"

        db.commit()

        return {
            "message": "Transformation completed",
            "transformation_id": transformation.id,
            "outputs": generated_outputs
        }

    except Exception as error:

        transformation.status = "error"
        db.commit()

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
    