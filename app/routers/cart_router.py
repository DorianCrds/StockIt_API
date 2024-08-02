from app.routers import *

cart_router = APIRouter()


@cart_router.post("/cart")
def create_cart():
    pass


@cart_router.get("/carts/")
def read_carts():
    pass


@cart_router.get("/cart/{cart_id}")
def read_cart_by_id():
    pass


@cart_router.put("/cart/{cart_id}")
def update_cart_by_id():
    pass


@cart_router.delete("/cart/{cart_id}")
def delete_cart_by_id():
    pass
