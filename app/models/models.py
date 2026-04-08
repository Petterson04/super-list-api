from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


# =====================
# USUARIOS
# =====================
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String, nullable=False)

    productos = relationship("ProductoLista", back_populates="usuario")


# =====================
# LISTAS
# =====================
class Lista(Base):
    __tablename__ = "listas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    creada_por = Column(Integer, ForeignKey("usuarios.id"))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    productos = relationship("ProductoLista", back_populates="lista")


# =====================
# PRODUCTOS
# =====================
class ProductoLista(Base):
    __tablename__ = "productos_lista"

    id = Column(Integer, primary_key=True, index=True)

    nombre_producto = Column(String, nullable=False)
    cantidad = Column(String)
    tienda = Column(String)
    comprado = Column(Boolean, default=False)

    lista_id = Column(Integer, ForeignKey("listas.id"))
    agregado_por = Column(Integer, ForeignKey("usuarios.id"))

    lista = relationship("Lista", back_populates="productos")
    usuario = relationship("Usuario", back_populates="productos")