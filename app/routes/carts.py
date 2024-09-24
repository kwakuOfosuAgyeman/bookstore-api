@router.get("/cart/", response_model=List[schemas.CartItem])
def get_cart(db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.get_cart_items(db, user_id=current_user.id)

@router.post("/cart/", response_model=schemas.CartItem)
def add_to_cart(cart_item: schemas.CartItemCreate, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.add_to_cart(db=db, user_id=current_user.id, cart_item=cart_item)

@router.delete("/cart/{item_id}")
def remove_from_cart(item_id: int, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.remove_from_cart(db=db, user_id=current_user.id, item_id=item_id)
