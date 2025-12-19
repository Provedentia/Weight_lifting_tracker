from fastapi import HTTPException
from datetime import datetime
from src.schemas.example import ExampleCreate, ExampleResponse
from src.services.example import get_example, create_example
from src.config.config import SUPABASE_URL, SUPABASE_PUBLIC_KEY, SUPABASE_PRIVATE_KEY
from supabase import create_client


# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_PUBLIC_KEY, SUPABASE_PRIVATE_KEY)
#initialize admin client 
admin_client = create_client(SUPABASE_URL, SUPABASE_PRIVATE_KEY)

#Register a new user
def register_user(user: RegisterUser):
    try:
        response = supabase.auth.sign_up(user.email, user.password)
        if response.error:
            raise HTTPException(status_code=400, detail=response.error.message)
        supabase.table('users').insert({
            'user.id': response.user.id,
            'email': user.email,
            'username': user.username,
            'phone_number': user.phone_number,
            'created_at': datetime.now()
        }).execute()
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))