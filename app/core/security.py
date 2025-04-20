from jwt import decode, InvalidTokenError
from scutum.ext.fastapi import auth_config
from fastapi import Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Security(oauth2_scheme)):
    try:
        payload = decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"username": username}
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
    
auth_config.get_current_user = get_current_user