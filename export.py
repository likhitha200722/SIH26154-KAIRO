from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Output
from services.export_service import generate_export


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.post("/{output_id}")
def export_output(
    output_id: int,
    format_type: str,
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

    result = generate_export(
        output.content,
        output.output_type,
        format_type
    )

    output.file_path = result["file_path"]

    db.commit()

    return {
        "message": "Export generated",
        "output_id": output.id,
        "file_path": output.file_path
    }