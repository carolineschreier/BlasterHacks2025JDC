from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from fastapi.middleware.cors import CORSMiddleware
from handlers import message_handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine("sqlite:///./app.db")
    app.state.db = engine
    try:
        yield
    finally:
        engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(message_handler.router)

@app.get("/")
def read_root():
    """
    Returns the API version
    """
    return {"API Version": "1.0.0"}

DB_URL = "sqlite:///./app.db"
