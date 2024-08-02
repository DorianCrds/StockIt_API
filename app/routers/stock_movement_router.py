from app.routers import *

stock_movement_router = APIRouter()


@stock_movement_router.post("/stock_movement")
def create_stock_movement():
    pass


@stock_movement_router.get("/stock_movements/")
def read_stock_movements():
    pass


@stock_movement_router.get("/stock_movement/{stock_movement_id}")
def read_stock_movement_by_id():
    pass


@stock_movement_router.put("/stock_movement/{stock_movement_id}")
def update_stock_movement_by_id():
    pass


@stock_movement_router.delete("/stock_movement/{stock_movement_id}")
def delete_stock_movement_by_id():
    pass
