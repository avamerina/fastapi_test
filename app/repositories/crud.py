from sqlalchemy.orm import Session
from app import models
from app.repositories.base_crud import BaseCRUD
from app.schemas.schemas import Score, Student, StudentCreate, ScoreCreate, ScoreUpdate, StudentUpdate


class StudentCRUD(BaseCRUD[Student, StudentCreate, StudentUpdate]):
    def __init__(self, db: Session) -> None:
        super().__init__(db, models.Student)


class ScoreCRUD(BaseCRUD[Score, ScoreCreate, ScoreUpdate]):
    def __init__(self, db: Session) -> None:
        super().__init__(db, models.Score)
