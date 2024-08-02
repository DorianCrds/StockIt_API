from app.schemas import *


class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    description: str
    categorie: typing.Optional[str]
    image_url: str


class ProductSchema(ProductBase):
    id: int

    class Config:
        orm_mode: True
