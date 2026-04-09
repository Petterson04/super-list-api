from fastapi import FastAPI
from app.database import DATABASE_URL, engine, Base
from app.routers import users, listas, productos
from app.models import models
from app.routers import auth as au

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(listas.router)
app.include_router(productos.router)
app.include_router(au.router)

print("🚀 DATABASE_URL =", DATABASE_URL)
print ("🚀 Database connected successfully!")

@app.on_event("startup")
def startup():
    print("⚡ STARTUP EVENT RUNNING")
    Base.metadata.create_all(bind=engine)
