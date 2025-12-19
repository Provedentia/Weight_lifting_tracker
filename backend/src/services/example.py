# Business logic layer

def get_example(id: int):
    # Add your business logic here
    return {"id": id, "name": "example"}

def create_example(data: dict):
    # Add your business logic here
    return {"id": 1, **data}

