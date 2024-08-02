from app.entities import *
from app.entities.product import Product

supplier_order_product_association = Table(
    'supplier_order_product',
    Base.metadata,
    Column("supplier_order_id", Integer, ForeignKey("supplier_orders.id")),
    Column("product_id", Integer, ForeignKey("products.id"))
)


class SupplierOrder(Base):
    __tablename__ = "supplier_orders"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(String, index=True)
    products = relationship("Product", secondary=supplier_order_product_association, back_populates='supplier_orders')
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, index=True)


Product.carts = relationship('SupplierOrder', secondary=supplier_order_product_association, back_populates='products')
