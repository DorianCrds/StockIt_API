from app.schemas import *
from app.schemas.product_schema import Product


class CartBase(BaseModel):
    client_id: str
    products: list[Product]
    status: str


class Cart(CartBase):
    id: int

    class Config:
        orm_mode: True
