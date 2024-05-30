from typing import Generator
from fastapi import Depends

from app.database import SessionLocal
from app.repositories.crud import StudentCRUD, ScoreCRUD
from app.services.services import StudentService, ScoreService

from sqlalchemy.orm import Session


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_student_service(db: Session = Depends(get_db)) -> StudentService:
    student_repository = StudentCRUD(db)
    return StudentService(student_repository)


def get_score_service(db: Session = Depends(get_db)) -> ScoreService:
    score_repository = ScoreCRUD(db)
    return ScoreService(score_repository)



