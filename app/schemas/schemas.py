from pydantic import BaseModel
from datetime import datetime


# ---------- USUARIOS ----------
class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str

    class Config:
        from_attributes = True


# ---------- LISTAS ----------
class ListaCreate(BaseModel):
    nombre: str
    creada_por: int


class ListaResponse(BaseModel):
    id: int
    nombre: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True


# ---------- PRODUCTOS ----------
class ProductoCreate(BaseModel):
    nombre_producto: str
    cantidad: str
    tienda: str
    lista_id: int
    agregado_por: int


class ProductoResponse(BaseModel):
    id: int
    nombre_producto: str
    cantidad: str
    tienda: str
    comprado: bool

    class Config:
        from_attributes = True