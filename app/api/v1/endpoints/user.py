from sqlalchemy.orm import Session
from scutum.ext.fastapi import check_permission
from fastapi import APIRouter, Depends
from app.schemas.user import User, UserCreate
from app.services.user import get_user, create_user
from app.core.db import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=User)
def show(
    user_id,
    db: Session = Depends(get_db),
    _: bool = Depends(check_permission("users:view"))
):
    user = get_user(db=db, user_id=user_id)
    return user

@router.post("/", response_model=User)
def create(
    user: UserCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(check_permission("users:create"))
):    
    return create_user(db=db, user=user)