from typing import Optional
from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.entities.base import Base

class Product(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_producto: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion_producto: Mapped[str] = mapped_column(String(150), nullable=False)
    precio_producto: Mapped[float] = mapped_column(Float, nullable=False)
    cantidad_producto: Mapped[int] = mapped_column(Integer, nullable=False)
    proveedor: Mapped[str] = mapped_column(String(150), nullable=False)
    rubro: Mapped[str] = mapped_column(String(150), nullable=False)
    categoria: Mapped[str] = mapped_column(String(150), nullable=False)