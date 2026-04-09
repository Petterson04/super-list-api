from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import os
import hashlib

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 días

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ======================
# PASSWORD HASH
# ======================
def hash_password(password: str):
    # pre-hash SHA256 (sin perder seguridad)
    sha = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(sha)

def verify_password(plain: str, hashed: str):
    sha = hashlib.sha256(plain.encode()).hexdigest()
    return pwd_context.verify(sha, hashed)


# ======================
# JWT
# ======================
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)