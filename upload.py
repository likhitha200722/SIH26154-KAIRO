from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Document
from services.document_service import save_uploaded_file


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:
        file_path = save_uploaded_file(file)

        document = Document(
            filename=file.filename,
            file_path=file_path,
            file_type=file.content_type,
            status="uploaded"
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return {
            "message": "File uploaded successfully",
            "document_id": document.id,
            "filename": document.filename,
            "status": document.status
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Error uploading file"
        )