from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = None):
    # Add your authentication logic here
    if not credentials:
        raise HTTPException(status_code=401, detail="Not authenticated")
    # Verify token logic
    return True

