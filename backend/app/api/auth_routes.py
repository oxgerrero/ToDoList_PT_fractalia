from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db import models
from app.schemas import user as user_schema
from app.auth import get_db, get_password_hash, verify_password, create_access_token
from app.schemas.user import Token

router = APIRouter()

@router.post("/register", response_model=user_schema.UserOut)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter_by(username=user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed = get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(username=form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
