from fastapi import Depends, APIRouter, status, HTTPException

from app.schemas import schemas
from app.depends import get_student_service, get_score_service
from app.services.services import StudentService, ScoreService


student_router = APIRouter(prefix="/students", tags=["students"])
score_router = APIRouter(prefix="/scores", tags=["scores"])


@student_router.get(
    '/{student_id}',
    status_code=status.HTTP_200_OK,
    responses={400: {"description": "Bad Request"}},
    response_model=schemas.Student,
    summary="Get student"
)
async def get_student(
        student_id: int,
        student_service: StudentService = Depends(get_student_service)
) -> schemas.Student:
    return student_service.get(student_id)


@student_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.StudentCreate,
    summary="Create student"
)
async def create_student(
        student: schemas.StudentCreate,
        student_service: StudentService = Depends(get_student_service)
) -> schemas.Student:
    return student_service.create(student)


@student_router.put(
    '/{student_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.StudentCreate,
    summary="Update student"
)
async def update_student(
        student_id: int,
        student: schemas.StudentCreate,
        student_service: StudentService = Depends(get_student_service)
) -> schemas.Student:
    return student_service.update(student_id, student)


@student_router.patch(
    '/{student_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.StudentUpdate,
    summary="Partial update student"
)
async def partial_update_student(
        student_id: int,
        student: schemas.StudentUpdate,
        student_service: StudentService = Depends(get_student_service)
) -> schemas.Student:
    return student_service.partial_update(student_id, student)


@student_router.delete(
    "/{student_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete student"
)
async def delete_student(
        student_id: int,
        student_service: StudentService = Depends(get_student_service)
):
    return student_service.delete(student_id)


@score_router.get(
    '/{score_id}',
    status_code=status.HTTP_200_OK,
    responses={400: {"description": "Bad Request"}},
    response_model=schemas.Score,
    summary="Get score"
)
async def get_score(
        score_id: int,
        score_service: ScoreService = Depends(get_score_service)
) -> schemas.Score:
    return score_service.get(score_id)


@score_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ScoreCreate,
    summary="Create score"
)
async def create_score(
        score: schemas.ScoreCreate,
        score_service: ScoreService = Depends(get_score_service)
) -> schemas.Score:
    try:
        return score_service.create(score)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@score_router.put(
    '/{score_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.ScoreCreate,
    summary="Update score"
)
async def update_score(
        score_id: int,
        score: schemas.ScoreCreate,
        score_service: ScoreService = Depends(get_score_service)
) -> schemas.Score:
    try:
        return score_service.update(score_id, score)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@score_router.patch(
    '/{score_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.ScoreUpdate,
    summary="Partial update score"
)
async def partial_update_score(
        score_id: int,
        score: schemas.ScoreUpdate,
        score_service: ScoreService = Depends(get_score_service)
) -> schemas.Score:
    try:
        return score_service.partial_update(score_id, score)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@score_router.delete(
    "/{score_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete score"
)
async def delete_score(
        score_id: int,
        score_service: ScoreService = Depends(get_score_service)
):
    return score_service.delete(score_id)
