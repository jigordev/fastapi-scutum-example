from jwt import decode, InvalidTokenError
from scutum.ext.fastapi import create_api_gate
from fastapi import Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.policies.user import UserPolicy
from app.policies.post import PostPolicy

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

gate = create_api_gate(get_current_user)
gate.add_policy("users", UserPolicy)
gate.add_policy("posts", PostPolicy)