from sqlalchemy.orm import Session
from app.schemas.post import PostCreate
from app.models.post import Post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, post: PostCreate):
    db_post = Post(**post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post