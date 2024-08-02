from app.entities import *
from app.entities.product import Product

customer_order_product_association = Table(
    'customer_order_product',
    Base.metadata,
    Column("customer_order_id", Integer, ForeignKey("customer_orders.id")),
    Column("product_id", Integer, ForeignKey("products.id"))
)


class CustomerOrder(Base):
    __tablename__ = "customer_orders"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    products = relationship("Product", secondary=customer_order_product_association, back_populates='orders')
    status = Column(String, index=True)


Product.orders = relationship('CustomerOrder', secondary=customer_order_product_association, back_populates='products')
