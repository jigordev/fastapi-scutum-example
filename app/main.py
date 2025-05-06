from fastapi import FastAPI
from contextlib import asynccontextmanager
from scutum.ext.fastapi import create_api_gate
from app.api.v1.endpoints import user
from app.api.v1.endpoints import post
from app.core.security import get_current_user
from app.policies.user import UserPolicy
from app.policies.post import PostPolicy

gate = create_api_gate(get_current_user)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await gate.add_policy("users", UserPolicy)
    await gate.add_policy("posts", PostPolicy)

app = FastAPI(lifespan=lifespan)
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["Posts"])