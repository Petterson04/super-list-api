from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.models import Usuario
from app.schemas.schemas import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UsuarioResponse)
def crear_usuario(user: UsuarioCreate, db: Session = Depends(get_db)):

    nuevo_usuario = Usuario(
        nombre=user.nombre,
        email=user.email,
        password_hash=user.password  # luego encriptamos
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario