from fastapi import FastAPI
from src.api.endpoints import example

app = FastAPI()

app.include_router(example.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API is running"}

