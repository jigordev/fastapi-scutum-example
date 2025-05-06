from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.post import PostCreate
from app.models.post import Post

async def get_post(db: AsyncSession, post_id: int):
    return await db.query(Post).filter(Post.id == post_id).first()

async def create_post(db: AsyncSession, post: PostCreate):
    db_post = Post(**post)
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post