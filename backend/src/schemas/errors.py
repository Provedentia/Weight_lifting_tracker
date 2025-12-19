from pydantic import BaseModel
from typing import Any
from datetime import datetime

class ErrorDetail(BaseModel):
    detail:str
    status_code:int

class ErrorResponse(BaseModel):
    success:nbool = False
    error: ErrorDetail
    timestamp: datetime.now()