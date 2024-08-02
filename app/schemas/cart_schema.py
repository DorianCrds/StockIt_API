from app.schemas import *
from app.schemas.product_schema import ProductSchema


class CartBase(BaseModel):
    client_id: str
    products: list[ProductSchema]
    status: str


class CartSchema(CartBase):
    id: int

    class Config:
        orm_mode: True
