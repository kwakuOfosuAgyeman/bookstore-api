from pydantic import BaseModel
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    price: float
    stock_quantity: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    book_id: int
    quantity: int

class CartItem(CartItemBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    total_price: float
    items: List[CartItemBase]

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
