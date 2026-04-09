from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from app.database import get_db
from app.models.models import Usuario
from app.schemas.schemas import UsuarioCreate, LoginRequest, TokenResponse
from app.auth.auth import (
    ALGORITHM,
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(prefix="/auth", tags=["Auth"])
secret_key = os.getenv("SECRET_KEY")

# ======================
# REGISTER
# ======================
@router.post("/register")
def register(user: UsuarioCreate, db: Session = Depends(get_db)):

    existing = db.query(Usuario)\
        .filter(Usuario.email == user.email)\
        .first()

    if existing:
        raise HTTPException(400, "Email ya registrado")

    new_user = Usuario(
        nombre=user.nombre,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "Usuario creado"}


# ======================
# LOGIN
# ======================
@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(Usuario)\
        .filter(Usuario.email == data.email)\
        .first()

    if not user:
        raise HTTPException(401, "Credenciales inválidas")

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Credenciales inválidas")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

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