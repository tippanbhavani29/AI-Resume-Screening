from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Float,
    Text
)
from sqlalchemy import DateTime
from datetime import datetime

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ScreeningResult(Base):

    __tablename__ = "screening_results"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_name = Column(String)

    overall_match_score = Column(Float)

    skill_match_score = Column(Float)

    matched_skills = Column(Text)

    missing_skills = Column(Text)
    # recommendation = Column(String)

    # created_at = Column(DateTime)