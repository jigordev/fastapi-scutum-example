from scutum.ext.fastapi import fastapi_adapter
from scutum import AsyncGate
from fastapi import Request, Depends, HTTPException
from app.core.config import settings
from app.services.user import get_user

async def get_current_user(
    request: Request,
):
    user_id: str = request.headers.get("x-user-id")
    if user_id is None:
        raise HTTPException(status_code=401, detail="User ID not found in request headers")
    
    user = await get_user(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
gate = AsyncGate()
gate = fastapi_adapter(gate, get_current_user)