from jwt import decode, InvalidTokenError
from fastapi import Security, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.core.db import AsyncSession, get_db
from app.services.user import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(
    token: str = Security(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    try:
        payload = decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user = await get_user(db=db, user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")