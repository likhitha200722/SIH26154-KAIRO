from pydantic import BaseModel
from typing import List


class TransformationRequest(BaseModel):
    document_id: int
    audience: str
    tone: str
    language: str
    detail_level: str
    objective: str
    outputs: List[str]