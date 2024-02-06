from typing import Union
from fastapi import FastAPI
from routes import crud

from database.connection import init_db


app = FastAPI()


@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(crud.router)

