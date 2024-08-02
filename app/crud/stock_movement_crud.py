from app.crud import *
from app.entities.stock_movement import StockMovement
from app.schemas.stock_movement_schema import StockMovementSchema


def create_stock_movement(db: Session, stock_movement: StockMovementSchema):
    db_stock_movement = StockMovement(**stock_movement.model_dump())
    db.add(db_stock_movement)
    db.commit()
    db.refresh(db_stock_movement)
    return db_stock_movement


def get_stock_movements(db: Session):
    return db.query(StockMovement).all()


def get_stock_movement(db: Session, stock_movement_id: int):
    return db.query(StockMovement).filter(StockMovement.id == stock_movement_id).first()


def update_stock_movement(db: Session, stock_movement_id: int, stock_movement: StockMovementSchema):
    db_stock_movement = db.query(StockMovement).filter(StockMovement.id == stock_movement_id).first()
    if db_stock_movement:
        for key, value in stock_movement.model_dump().items():
            setattr(db_stock_movement, key, value)
        db.commit()
        db.refresh(db_stock_movement)
    return db_stock_movement


def delete_stock_movement(db: Session, stock_movement_id: int):
    db_stock_movement = db.query(StockMovement).filter(StockMovement.id == stock_movement_id).first()
    if db_stock_movement:
        db.delete(db_stock_movement)
        db.commit()
    return db_stock_movement
