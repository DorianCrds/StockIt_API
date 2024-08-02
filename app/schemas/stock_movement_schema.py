from app.schemas import *


class StockMovementBase(BaseModel):
    product_id: int
    quantity: int
    type: str
    date: datetime.date
    comment: typing.Optional[str]


class StockMovement(StockMovementBase):
    id: int

    class Config:
        orm_mode: True
