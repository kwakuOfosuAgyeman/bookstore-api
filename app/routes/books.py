from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models, dependencies

router = APIRouter()

@router.get("/books/", response_model=List[schemas.Book])
def list_books(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(dependencies.get_db)):
    book = crud.get_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_book(db=db, book=book)
