from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

# --- User Operations ---
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Book Operations ---
def get_books(db: Session, skip: int = 0, limit: int = 10) -> List[models.Book]:
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        price=book.price,
        stock_quantity=book.stock_quantity
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book_stock(db: Session, book_id: int, quantity: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        book.stock_quantity -= quantity
        db.commit()
        db.refresh(book)
    return book

# --- Cart Operations ---
def get_cart_items(db: Session, user_id: int):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()

def add_to_cart(db: Session, user_id: int, cart_item: schemas.CartItemCreate):
    db_cart_item = models.CartItem(user_id=user_id, book_id=cart_item.book_id, quantity=cart_item.quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def remove_from_cart(db: Session, user_id: int, item_id: int):
    cart_item = db.query(models.CartItem).filter(models.CartItem.id == item_id, models.CartItem.user_id == user_id).first()
    if cart_item:
        db.delete(cart_item)
        db.commit()
    return cart_item

# --- Order Operations ---
def create_order(db: Session, user_id: int, order: schemas.OrderCreate):
    total_price = 0
    order_items = []
    for item in order.items:
        book = get_book(db, item.book_id)
        if book and book.stock_quantity >= item.quantity:
            total_price += book.price * item.quantity
            order_items.append(models.OrderItem(book_id=item.book_id, quantity=item.quantity, price=book.price))
            update_book_stock(db, item.book_id, item.quantity)
        else:
            raise HTTPException(status_code=400, detail=f"Book with ID {item.book_id} is out of stock.")
    
    db_order = models.Order(user_id=user_id, total_price=total_price, items=order_items)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, user_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()
