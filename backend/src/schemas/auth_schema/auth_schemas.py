from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
import re

class PasswordStr(BaseModel):
    password: str = Field(min_length=12, max_length=128)
    regex_password = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$'
    @validator('password')
    def validate_password(cls, v):
        if not re.match(cls.regex_password, v):
            raise ValueError('Password must be at least 12 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character')
        return v

class RegisterUser(BaseModel):
    email: EmailStr
    username: str
    password: PasswordStr
    phone_number: Optional[str] = Field(min_length=10, max_length=15)
    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not re.match(r'^\+[1-9]\d{1,14}$', v):
            raise ValueError('Phone number must be a valid international phone number')
        return v


