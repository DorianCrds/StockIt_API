from app.entities import *
from app.entities.product import Product

cart_product_association = Table(
    'cart_product',
    Base.metadata,
    Column("cart_id", Integer, ForeignKey("carts.id")),
    Column("product_id", Integer, ForeignKey("products.id"))
)


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, index=True)
    products = relationship("Product", secondary=cart_product_association, back_populates='carts')
    status = Column(String, index=True)


Product.carts = relationship('Cart', secondary=cart_product_association, back_populates='products')
