from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from .. import schemas, models, crud, auth, dependencies

router = APIRouter()

@router.post("/orders/", response_model=schemas.Order)
def place_order(order: schemas.OrderCreate, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.create_order(db=db, user_id=current_user.id, order=order)

@router.get("/orders/", response_model=List[schemas.Order])
def get_user_orders(db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.get_orders(db=db, user_id=current_user.id)
