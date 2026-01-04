from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel): #  схема для товара в корзине
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be greater than 0)") # минимальное значение = 0 (gt=0)

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="New quantity (must be greader than 0)") # минимальное значение = 0 (gt=0)

class CartItem(BaseModel): # подробная инфа о товарах в корзине
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product Price")
    quantity: int = Field(..., gt=0, description="Quantity in cart")
    subtotal: float = Field(..., description="Total price for this item (price * quantity)") # стоимость всех товаров этого типа
    image_url: Optional[str] = Field(None, description="product image URL")

class CartResponse(BaseModel): # инфа о самой корзине с товарами
    items: list[CartItem] = Field(..., description="List items in cart") # список всех товаров в корзине
    total: float = Field(..., description="Total cart price") # стоимость вообще всех товаров
    items_count: int = Field(..., description="Total number of items in cart") # количество всех товаров
