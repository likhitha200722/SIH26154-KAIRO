from pydantic import BaseModel
from typing import List, Optional


class OutputResponse(BaseModel):
    id: int
    transformation_id: int
    output_type: str
    content: Optional[str] = None
    file_path: Optional[str] = None
    status: str
    consistency_score: Optional[int] = None
    validation_warnings: Optional[List[str]] = None

    class Config:
        from_attributes = True