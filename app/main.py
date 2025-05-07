from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.endpoints import user
from app.api.v1.endpoints import post
from app.core.security import gate
from app.policies.user import UserPolicy
from app.policies.post import PostPolicy

@asynccontextmanager
async def lifespan(app: FastAPI):
    await gate.setup()

app = FastAPI(lifespan=lifespan)
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["Posts"])