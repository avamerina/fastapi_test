from fastapi import FastAPI

from app import models
from app.database import engine
from app.routing import routes

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(routes.student_router)
app.include_router(routes.score_router)
