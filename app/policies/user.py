from scutum import AsyncPolicy
from app.core.security import gate

@gate.policy("users")
class UserPolicy(AsyncPolicy):
    async def view(self, user):
        return user.role == "admin"
    
    async def create(self, user, data):
        return user.role == "admin"