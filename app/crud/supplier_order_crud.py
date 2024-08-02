from app.crud import *
from app.entities.supplier_order import SupplierOrder
from app.schemas.supplier_order_schema import SupplierOrderSchema


def create_supplier_order(db: Session, supplier_order: SupplierOrderSchema):
    db_supplier_order = SupplierOrder(**supplier_order.model_dump())
    db.add(db_supplier_order)
    db.commit()
    db.refresh(db_supplier_order)
    return db_supplier_order


def get_supplier_orders(db: Session):
    return db.query(SupplierOrder).all()


def get_supplier_order(db: Session, supplier_order_id: int):
    return db.query(SupplierOrder).filter(SupplierOrder.id == supplier_order_id).first()


def update_supplier_order(db: Session, supplier_order_id: int, supplier_order: SupplierOrderSchema):
    db_supplier_order = db.query(SupplierOrder).filter(SupplierOrder.id == supplier_order_id).first()
    if db_supplier_order:
        for key, value in supplier_order.model_dump().items():
            setattr(db_supplier_order, key, value)
        db.commit()
        db.refresh(db_supplier_order)
    return db_supplier_order


def delete_supplier_order(db: Session, supplier_order_id: int):
    db_supplier_order = db.query(SupplierOrder).filter(SupplierOrder.id == supplier_order_id).first()
    if db_supplier_order:
        db.delete(db_supplier_order)
        db.commit()
    return db_supplier_order
