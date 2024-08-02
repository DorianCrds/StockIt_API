from app.schemas import *
from app.schemas.product_schema import Product


class CustomerOrderBase(BaseModel):
    date: datetime.date
    products: list[Product]
    status: str


class CustomerOrder(CustomerOrderBase):
    id: int

    class Config:
        orm_mode: True
