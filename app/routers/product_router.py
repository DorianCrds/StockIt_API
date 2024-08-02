from app.routers import *

product_router = APIRouter()


@product_router.post("/product")
def create_product():
    pass


@product_router.get("/products/")
def read_products():
    pass


@product_router.get("/product/{product_id}")
def read_product_by_id():
    pass


@product_router.put("/product/{product_id}")
def update_product_by_id():
    pass


@product_router.delete("/product/{product_id}")
def delete_product_by_id():
    pass
