from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import User, UserCreate
from app.services.user import get_user, create_user
from app.core.security import gate

router = APIRouter()

@router.get("/{user_id}", response_model=User)
async def show(
    user_id,
    user: User = Depends(gate.can("users:view"))
):
    print(user)
    user = await get_user(user_id=user_id)
    if not user:
        raise HTTPException(404, detail="User not found")
    return user

@router.post("/", response_model=User)
async def create(
    user_data: UserCreate,
    _: User = Depends(gate.can("users:create"))
):    
    return await create_user(user=user_data)