from app.schemas import *
from app.schemas.product_schema import Product


class SupplierOrderBase(BaseModel):
    supplier_id: str
    products: list[Product]
    date: datetime.date
    status: str


class SupplierOrder(SupplierOrderBase):
    id: int

    class Config:
        orm_mode: True
