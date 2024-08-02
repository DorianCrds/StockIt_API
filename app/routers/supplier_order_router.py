from app.routers import *

supplier_order_router = APIRouter()


@supplier_order_router.post("/supplier_order")
def create_supplier_order():
    pass


@supplier_order_router.get("/supplier_orders/")
def read_supplier_orders():
    pass


@supplier_order_router.get("/supplier_order/{supplier_order_id}")
def read_supplier_order_by_id():
    pass


@supplier_order_router.put("/supplier_order/{supplier_order_id}")
def update_supplier_order_by_id():
    pass


@supplier_order_router.delete("/supplier_order/{supplier_order_id}")
def delete_supplier_order_by_id():
    pass
