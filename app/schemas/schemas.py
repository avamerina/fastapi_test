from pydantic import BaseModel, conint, constr


class ScoreBase(BaseModel):
    subject: constr(min_length=1)
    score: conint(ge=0, le=5)
    student_id: conint(ge=0)


class ScoreCreate(ScoreBase):
    pass


class ScoreUpdate(BaseModel):
    subject: constr(min_length=1) | None = None
    score: conint(ge=0, le=5) | None = None
    student_id: conint(gt=0) | None = None


class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    name: constr(min_length=1)
    age: conint(ge=1)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    name: constr(min_length=1) | None = None
    age: conint(ge=1) | None = None


class Student(StudentBase):
    id: int
    scores: list[Score] = []

    class Config:
        orm_mode = True
