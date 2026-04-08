from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, listas, productos

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(listas.router)
app.include_router(productos.router)