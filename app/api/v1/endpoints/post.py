from typing import Annotated
from fastapi import APIRouter, Security, HTTPException
from app.schemas.post import Post, PostCreate
from app.services.post import get_post, create_post
from app.core.security import gate, get_current_user

router = APIRouter()

@router.get("/{post_id}", response_model=Post)
def show(post_id, current_user: Annotated[dict, Security(get_current_user)]):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if gate.denied("posts:view", current_user, post):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    return post

@router.post("/", response_model=Post)
def create(post: PostCreate, current_user: Annotated[dict, Security(get_current_user)]):
    if gate.denied("posts:create", current_user, post):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    return create_post(post)