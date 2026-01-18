from app.schemas.post import PostCreate
from app.models.post import Post

async def get_post(post_id: int):
    return Post(id=post_id, title="Test", content="Test", author_id=1)

async def create_post(post: PostCreate):
    return Post(**post)