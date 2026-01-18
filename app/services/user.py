from app.schemas.user import UserCreate
from app.models.user import User

async def get_user(user_id: int):
    return User(id=user_id, email="test@example.com", password="test", posts=[])

async def create_user(user: UserCreate):
    return User(**user)