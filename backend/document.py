from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    filename: str
    status: str

    class Config:
        from_attributes = True