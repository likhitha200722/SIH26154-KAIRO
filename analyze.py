import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Document
from services.document_processor import process_document


router = APIRouter(
    prefix="/analyze",
    tags=["Document Analysis"]
)


@router.post("/{document_id}")
def analyze_document(
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

    try:

        document.status = "processing"
        db.commit()

        result = process_document(
            document.file_path
        )

        document.extracted_data = json.dumps(result)
        document.status = "analyzed"

        db.commit()

        return {
            "message": "Document analyzed successfully",
            "document_id": document.id,
            "data": result
        }

    except Exception as error:

        document.status = "error"
        db.commit()

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )