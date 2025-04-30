from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemas.user import User, UserCreate
from app.services.user import get_user, create_user
from app.core.security import gate
from app.core.db import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=User)
def show(
    user_id,
    db: Session = Depends(get_db),
    user: User = Depends(gate.authorized_user("users:view"))
):
    user = get_user(db=db, user_id=user_id)
    return user

@router.post("/", response_model=User)
def create(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    user: User = Depends(gate.authorized_user("users:create"))
):    
    return create_user(db=db, user=user_data)