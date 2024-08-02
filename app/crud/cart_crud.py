from app.crud import *
from app.entities.cart import Cart
from app.schemas.cart_schema import CartSchema


def create_cart(db: Session, cart: CartSchema):
    db_cart = Cart(**cart.model_dump())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart


def get_carts(db: Session):
    return db.query(Cart).all()


def get_cart(db: Session, cart_id: int):
    return db.query(Cart).filter(Cart.id == cart_id).first()


def update_cart(db: Session, cart_id: int, cart: CartSchema):
    db_cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart:
        for key, value in cart.model_dump().items():
            setattr(db_cart, key, value)
        db.commit()
        db.refresh(db_cart)
    return db_cart


def delete_cart(db: Session, cart_id: int):
    db_cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart:
        db.delete(db_cart)
        db.commit()
    return db_cart
