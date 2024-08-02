from app.crud import *
from app.entities.customer_order import CustomerOrder
from app.schemas.customer_order_schema import CustomerOrderSchema


def create_customer_order(db: Session, customer_order: CustomerOrderSchema):
    db_customer_order = CustomerOrder(**customer_order.model_dump())
    db.add(db_customer_order)
    db.commit()
    db.refresh(db_customer_order)
    return db_customer_order


def get_customer_orders(db: Session):
    return db.query(CustomerOrder).all()


def get_customer_order(db: Session, customer_order_id: int):
    return db.query(CustomerOrder).filter(CustomerOrder.id == customer_order_id).first()


def update_customer_order(db: Session, customer_order_id: int, customer_order: CustomerOrderSchema):
    db_customer_order = db.query(CustomerOrder).filter(CustomerOrder.id == customer_order_id).first()
    if db_customer_order:
        for key, value in customer_order.model_dump().items():
            setattr(db_customer_order, key, value)
        db.commit()
        db.refresh(db_customer_order)
    return db_customer_order


def delete_customer_order(db: Session, customer_order_id: int):
    db_customer_order = db.query(CustomerOrder).filter(CustomerOrder.id == customer_order_id).first()
    if db_customer_order:
        db.delete(db_customer_order)
        db.commit()
    return db_customer_order
