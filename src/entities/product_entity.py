from sqlalchemy import Column, Integer, String, Float
from database.dbconfig import Base

class ProductEntity(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_producto = Column(String(150), nullable=False)
    descripcion_producto = Column(String(150), nullable=False)
    precio_producto = Column(Float, nullable=False)
    cantidad_producto = Column(Integer, nullable=False)
    proveedor = Column(String(150), nullable=False)
    rubro = Column(String(150), nullable=False)
    categoria = Column(String(150), nullable=False)