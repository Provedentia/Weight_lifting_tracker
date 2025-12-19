from fastapi import HTTPException

class InvalidCredentialsError(HTTPException):
    def __init__(self, message: str = "Invalid email or password"):
        super().__init__(status_code=401, detail=message)

class UserNotFoundError(HTTPException):
    def __init__(self, message: str = "User not found"):
        super().__init__(status_code=404, detail=message)

class UserAlreadyExistsError(HTTPException):
    def __init__(self, message: str = "User already exists"):
        super().__init__(status_code=409, detail=message)

class WeakPasswordError(HTTPException):
    def __init__(self, message: str = "Password does not meet requirements"):
        super().__init__(status_code=400, detail=message)

class InvalidEmailError(HTTPException):
    def __init__(self, message: str = "Invalid email format"):
        super().__init__(status_code=400, detail=message)

class InvalidPhoneError(HTTPException):
    def __init__(self, message: str = "Invalid phone number format"):
        super().__init__(status_code=400, detail=message)

class TokenExpiredError(HTTPException):
    def __init__(self, message: str = "Token has expired"):
        super().__init__(status_code=401, detail=message)

class TokenInvalidError(HTTPException):
    def __init__(self, message: str = "Invalid or missing token"):
        super().__init__(status_code=401, detail=message)

