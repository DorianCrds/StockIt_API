from app.routers import *

customer_order_router = APIRouter()


@customer_order_router.post("/customer_order")
def create_customer_order():
    pass


@customer_order_router.get("/customer_orders/")
def read_customer_orders():
    pass


@customer_order_router.get("/customer_order/{customer_order_id}")
def read_customer_order_by_id():
    pass


@customer_order_router.put("/customer_order/{customer_order_id}")
def update_customer_order_by_id():
    pass


@customer_order_router.delete("/customer_order/{customer_order_id}")
def delete_customer_order_by_id():
    pass
