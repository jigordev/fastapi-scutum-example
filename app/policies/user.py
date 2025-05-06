from scutum import AsyncPolicy

class UserPolicy(AsyncPolicy):
    async def view(self, user):
        return user.role == "admin"
    
    async def create(self, user, data):
        return user.role == "admin"