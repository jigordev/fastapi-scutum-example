from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import User, UserCreate
from app.services.user import get_user, create_user
from app.core.security import gate
from app.core.db import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=User)
async def show(
    user_id,
    db: Session = Depends(get_db),
    _: User = Depends(gate.authorized_user("users:view"))
):
    user = await get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(404, detail="User not found")
    return user

@router.post("/", response_model=User)
async def create(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    _: User = Depends(gate.authorized_user("users:create"))
):    
    return await create_user(db=db, user=user_data)