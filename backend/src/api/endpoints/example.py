from fastapi import APIRouter
from src.schemas.example import ExampleCreate, ExampleResponse
from src.controllers.example import get_example_controller, create_example_controller

router = APIRouter()

@router.get("/example/{id}", response_model=ExampleResponse)
async def get_example(id: int):
    return get_example_controller(id)

@router.post("/example", response_model=ExampleResponse)
async def create_example(data: ExampleCreate):
    return create_example_controller(data)

