from scutum import AsyncPolicy
from app.core.security import gate

@gate.policy("posts")
class PostPolicy(AsyncPolicy):
    async def view(self, user, post):
        return True
    
    async def create(self, user, data):
        return True