from fastapi import FastAPI, Request
from .models import Base
from .database import engine, SessionLocal
from .routers import auth
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(auth.router)