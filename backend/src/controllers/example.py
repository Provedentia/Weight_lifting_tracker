from fastapi import HTTPException
from src.schemas.example import ExampleCreate, ExampleResponse
from src.services.example import get_example, create_example

def get_example_controller(id: int) -> ExampleResponse:
    result = get_example(id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return ExampleResponse(**result)

def create_example_controller(data: ExampleCreate) -> ExampleResponse:
    result = create_example(data.dict())
    return ExampleResponse(**result)

