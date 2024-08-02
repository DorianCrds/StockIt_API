from app.schemas import *
from app.schemas.product_schema import ProductSchema


class SupplierOrderBase(BaseModel):
    supplier_id: str
    products: list[ProductSchema]
    date: datetime.date
    status: str


class SupplierOrderSchema(SupplierOrderBase):
    id: int

    class Config:
        orm_mode: True
