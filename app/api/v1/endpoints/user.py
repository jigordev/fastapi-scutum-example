from typing import Annotated
from fastapi import APIRouter, Security, HTTPException
from app.schemas.user import User, UserCreate
from app.services.user import get_user, create_user
from app.core.security import gate, get_current_user

router = APIRouter()

@router.get("/{user_id}", response_model=User)
def show(user_id, current_user: Annotated[dict, Security(get_current_user)]):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if gate.denied("users:view", current_user):
        raise HTTPException(status_code=403, detail="Unauthorized")

    return user

@router.post("/", response_model=User)
def create(user: UserCreate, current_user: Annotated[dict, Security(get_current_user)]):
    if gate.denied("users:create", current_user, user):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    return create_user(user)