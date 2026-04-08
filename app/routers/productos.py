from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.models import ProductoLista
from app.schemas.schemas import ProductoCreate, ProductoResponse

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=ProductoResponse)
def agregar_producto(prod: ProductoCreate, db: Session = Depends(get_db)):

    nuevo_producto = ProductoLista(**prod.dict())

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


@router.get("/{lista_id}", response_model=list[ProductoResponse])
def productos_por_lista(lista_id: int, db: Session = Depends(get_db)):

    return db.query(ProductoLista)\
        .filter(ProductoLista.lista_id == lista_id)\
        .all()