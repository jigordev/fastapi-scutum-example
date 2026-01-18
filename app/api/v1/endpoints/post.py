from fastapi import APIRouter, Depends
from app.schemas.post import Post, PostCreate
from app.services.post import get_post, create_post
from app.core.security import gate

router = APIRouter()

@router.get("/{post_id}", response_model=Post)
async def show(
    post_id,
    _ = Depends(gate.can("posts:view"))
):
    post = await get_post(post_id=post_id)
    return post

@router.post("/", response_model=Post)
async def create(
    post: PostCreate,
    _ = Depends(gate.can("posts:create"))
):
    return await create_post(post=post)