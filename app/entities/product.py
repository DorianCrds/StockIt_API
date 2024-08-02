from app.entities import *


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    quantity = Column(Integer, index=True)
    description = Column(String, index=True)
    categorie = Column(String, index=True, nullable=True)
    image_url = Column(String, index=True)