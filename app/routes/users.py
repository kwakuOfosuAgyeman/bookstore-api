from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from .. import schemas, models, crud, auth, dependencies

router = APIRouter()

# Token expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- User Registration ---
@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    # Check if user with same username or email already exists
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create the user
    return crud.create_user(db=db, user=user)

# --- User Login ---
@router.post("/login", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(dependencies.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # Authenticate user based on username and password
    user = crud.authenticate_user(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token for the authenticated user
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    # Return the token as response
    return {"access_token": access_token, "token_type": "bearer"}

# --- Get Current User Profile ---
@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(dependencies.get_current_user)):
    # Returns the current user's profile data
    return current_user

# --- Get Current Admin User Profile ---
@router.get("/admin/me", response_model=schemas.User)
def read_admin_me(current_user: schemas.User = Depends(dependencies.get_current_admin_user)):
    # Returns the current admin's profile data
    return current_user
