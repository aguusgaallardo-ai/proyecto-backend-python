from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProductoBase(BaseModel):
    nombre_producto: str
    descripcion_producto: Optional[str] = None
    precio_producto: float
    cantidad_producto: int
    proveedor: Optional[str] = None
    rubro: Optional[str] = None
    categoria: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre_producto: Optional[str] = None
    descripcion_producto: Optional[str] = None
    precio_producto: Optional[float] = None
    cantidad_producto: Optional[int] = None
    proveedor: Optional[str] = None
    rubro: Optional[str] = None
    categoria: Optional[str] = None

class ProductoOut(ProductoBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)