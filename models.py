from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    file_path = Column(String, nullable=False)

    file_type = Column(String)

    status = Column(String, default="uploaded")

    extracted_data = Column(Text, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    transformations = relationship(
        "Transformation",
        back_populates="document"
    )


class Transformation(Base):

    __tablename__ = "transformations"

    id = Column(Integer, primary_key=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    audience = Column(String)

    tone = Column(String)

    language = Column(String)

    detail_level = Column(String)

    objective = Column(String)

    status = Column(
        String,
        default="processing"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    document = relationship(
        "Document",
        back_populates="transformations"
    )

    outputs = relationship(
        "Output",
        back_populates="transformation"
    )


class Output(Base):

    __tablename__ = "outputs"

    id = Column(
        Integer,
        primary_key=True
    )

    transformation_id = Column(
        Integer,
        ForeignKey("transformations.id")
    )

    output_type = Column(String)

    content = Column(Text)

    file_path = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="generated"
    )

    consistency_score = Column(
        Integer,
        nullable=True
    )

    validation_warnings = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    transformation = relationship(
        "Transformation",
        back_populates="outputs"
    )