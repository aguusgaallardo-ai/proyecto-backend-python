from sqlalchemy.orm import Session
from src.schemas.producto_schema import ProductoCreate, ProductoUpdate
from src.entities.producto_entity import Producto

def create_new_producto(db: Session, producto: ProductoCreate):
    nuevo_producto = Producto(
        nombre_producto=producto.nombre_producto,
        descripcion_producto=producto.descripcion_producto,
        precio_producto=producto.precio_producto,
        cantidad_producto=producto.cantidad_producto,
        proveedor=producto.proveedor,
        rubro=producto.rubro,
        categoria=producto.categoria
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def get_all_productos(db: Session):
    return db.query(Producto).all()

def get_producto_by_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def update_producto_by_id(db: Session, producto_id: int, producto_update: ProductoUpdate):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        if producto_update.nombre_producto is not None:
            producto.nombre_producto = producto_update.nombre_producto
        if producto_update.descripcion_producto is not None:
            producto.descripcion_producto = producto_update.descripcion_producto
        if producto_update.precio_producto is not None:
            producto.precio_producto = producto_update.precio_producto
        if producto_update.cantidad_producto is not None:
            producto.cantidad_producto = producto_update.cantidad_producto
        if producto_update.proveedor is not None:
            producto.proveedor = producto_update.proveedor
        if producto_update.rubro is not None:
            producto.rubro = producto_update.rubro
        if producto_update.categoria is not None:
            producto.categoria = producto_update.categoria
        
        db.commit()
        db.refresh(producto)
        return producto
    return None

def delete_producto_by_id(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False