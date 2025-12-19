from fastapi import HTTPException
from datetime import datetime
from src.schemas.example import ExampleCreate, ExampleResponse
from src.services.example import get_example, create_example
from src.config.config import SUPABASE_URL, SUPABASE_PUBLIC_KEY, SUPABASE_PRIVATE_KEY
from supabase import create_client
from src.schemas.auth_schema.auth_schemas import RegisterUser
from src.schemas.auth_schema.auth_exceptions import InvalidCredentialsError, UserNotFoundError, UserAlreadyExistsError, WeakPasswordError, InvalidEmailError, InvalidPhoneError, TokenExpiredError
import uuid

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_PUBLIC_KEY, SUPABASE_PRIVATE_KEY)
#initialize admin client 
admin_client = create_client(SUPABASE_URL, SUPABASE_PRIVATE_KEY)

def check_email_exists(email: str):
    existing_user = supabase.table('users').select('*').eq('email', email).execute()
    if existing_user.data:
        return True
    return False
#Register a new user
def register_user(user: RegisterUser):
    try:
        if check_email_exists(user.email):
            raise UserAlreadyExistsError(message="Email already registered")
    
        response = supabase.auth.sign_up({
            'email': user.email,
            'password': user.password,
            'options': {
                'data': {
                    'username': user.username,
                    'phone_number': user.phone_number if user.phone_number else None,
                }
            }
        })
        if response.user is None:
            raise HTTPException(status_code=500, detail="Server error, User not created")
         if not response.user.id:
            raise UserAlreadyExistsError(message="Email already registered")
        if response.error:
            raise InvalidCredentialsError(message=response.error.message)
        try:
            supabase.table('users').insert({
                'user_id': response.user.id,
                'email': user.email,
                'username': user.username,
                'phone_number': user.phone_number if user.phone_number else None,
                'created_at': datetime.now()
            }).execute()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        return {"message": "User registered successfully", "user_id": response.user.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

