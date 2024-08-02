from app.schemas import *
from app.schemas.product_schema import ProductSchema


class CustomerOrderBase(BaseModel):
    date: datetime.date
    products: list[ProductSchema]
    status: str


class CustomerOrderSchema(CustomerOrderBase):
    id: int

    class Config:
        orm_mode: True
