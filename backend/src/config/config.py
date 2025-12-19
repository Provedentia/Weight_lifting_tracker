import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_PUBLIC_KEY = os.getenv('SUPABASE_PUBLIC_KEY')
SUPABASE_PRIVATE_KEY = os.getenv('SUPABASE_PRIVATE_KEY')

PORT = os.getenv('PORT')