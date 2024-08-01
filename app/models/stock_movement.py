from app.models import *


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer, index=True)
    type = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    comment = Column(String, index=True, nullable=True)
