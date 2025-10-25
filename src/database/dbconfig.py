import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Forzar la ruta absoluta al .env
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = BASE_DIR / '.env'

# Cargar el .env explícitamente
load_dotenv(dotenv_path=env_path)

# URL para MySQL
URL_DATABASE = os.getenv("DATABASE_URL")

# Si no se cargó, usar valor por defecto o lanzar error
if not URL_DATABASE:
    URL_DATABASE = "mysql+pymysql://root:0000@localhost:3306/ProyectoProducto"
    print(f"⚠️ Usando URL por defecto: {URL_DATABASE}")

print(f"✅ Conectando a: {URL_DATABASE}")

# Crear el engine
engine = create_engine(URL_DATABASE)

# Crear SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]