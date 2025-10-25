from pydantic import BaseModel
from typing import Optional

class ProductDto(BaseModel):
    id: Optional[int] = None
    nombre_producto: str
    descripcion_producto: str
    precio_producto: float
    cantidad_producto: int
    proveedor: str
    rubro: str
    categoria: str

    class Config:
        from_attributes = True

class ProductResponseDto(BaseModel):
    id: int
    nombre_producto: str
    descripcion_producto: str
    precio_producto: float
    cantidad_producto: int
    proveedor: str
    rubro: str
    categoria: str

    class Config:
        from_attributes = True