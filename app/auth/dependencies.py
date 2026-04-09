from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from app.auth.auth import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(
            token.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload["user_id"]

    except JWTError:
        raise HTTPException(401, "Token inválido")
    
    