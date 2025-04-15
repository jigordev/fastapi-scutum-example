from fastapi import FastAPI
from api.v1.endpoints import user
from api.v1.endpoints import post

app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["Posts"])