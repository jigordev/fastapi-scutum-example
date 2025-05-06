from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemas.post import Post, PostCreate
from app.services.post import get_post, create_post
from app.core.security import gate
from app.core.db import get_db

router = APIRouter()

@router.get("/{post_id}", response_model=Post)
async def show(
    post_id,
    db: Session = Depends(get_db),
    _ = Depends(gate.authorized_user("posts:view"))
):
    post = await get_post(db=db, post_id=post_id)
    return post

@router.post("/", response_model=Post)
async def create(
    post: PostCreate,
    db: Session = Depends(get_db),
    _ = Depends(gate.authorized_user("posts:create"))
):
    return await create_post(db=db, post=post)