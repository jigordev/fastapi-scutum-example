from pydantic import BaseModel
from app.schemas.user import User

class Post(BaseModel):
    title: str
    content: str
    author: User

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int