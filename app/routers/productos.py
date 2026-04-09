from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.models import ProductoLista
from app.schemas.schemas import ProductoCreate, ProductoResponse
from app.routers import auth as au
from app.auth.dependencies import get_current_user



router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/")
def agregar_producto(
    prod: ProductoCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    nuevo_producto = ProductoLista(
        nombre_producto=prod.nombre_producto,
        cantidad=prod.cantidad,
        tienda=prod.tienda,
        lista_id=prod.lista_id,
        agregado_por=user_id
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


@router.get("/{lista_id}", response_model=list[ProductoResponse])
def productos_por_lista(lista_id: int, db: Session = Depends(get_db)):

    return db.query(ProductoLista)\
        .filter(ProductoLista.lista_id == lista_id)\
        .all()