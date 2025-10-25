import os
from dotenv import load_dotenv
from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# URL para MySQL
URL_DATABASE = os.getenv("DATABASE_URL=mysql+pymysql://root:0000@localhost:3306/ProyectoProducto")

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