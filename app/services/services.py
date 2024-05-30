from app.repositories.crud import StudentCRUD, ScoreCRUD
from app.schemas.schemas import Score, Student, StudentCreate, ScoreCreate, StudentUpdate, ScoreUpdate
from app.services.base_services import BaseService


class StudentService(BaseService[Student, StudentCreate, StudentUpdate]):
    def __init__(self, repository: StudentCRUD) -> None:
        super().__init__(repository)


class ScoreService(BaseService[Score, ScoreCreate, ScoreUpdate]):
    def __init__(self, repository: ScoreCRUD) -> None:
        super().__init__(repository)
