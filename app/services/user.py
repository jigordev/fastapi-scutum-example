from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.models.user import User

async def get_user(db: AsyncSession, user_id: int):
    return await db.query(User).filter(User.id == user_id).first()

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user