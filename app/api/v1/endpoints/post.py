from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Security, HTTPException
from app.schemas.post import Post, PostCreate
from app.services.post import get_post, create_post
from app.core.security import gate, get_current_user
from app.core.db import get_db

router = APIRouter()

@router.get("/{post_id}", response_model=Post)
def show(
    post_id,
    current_user: Annotated[dict, Security(get_current_user)],
    db: Session = Depends(get_db)
):
    post = get_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if gate.denied("posts:view", current_user, post):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    return post

@router.post("/", response_model=Post)
def create(
    post: PostCreate,
    current_user: Annotated[dict, Security(get_current_user)],
    db: Session = Depends(get_db)
):
    if gate.denied("posts:create", current_user, post):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    return create_post(db=db, post=post)