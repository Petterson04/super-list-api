from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.models import Lista
from app.schemas.schemas import ListaCreate, ListaResponse

router = APIRouter(prefix="/listas", tags=["Listas"])


@router.post("/", response_model=ListaResponse)
def crear_lista(lista: ListaCreate, db: Session = Depends(get_db)):

    nueva_lista = Lista(
        nombre=lista.nombre,
        creada_por=lista.creada_por
    )

    db.add(nueva_lista)
    db.commit()
    db.refresh(nueva_lista)

    return nueva_lista


@router.get("/", response_model=list[ListaResponse])
def obtener_listas(db: Session = Depends(get_db)):
    return db.query(Lista).all()