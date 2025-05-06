from scutum import AsyncPolicy

class PostPolicy(AsyncPolicy):
    async def view(self, user, post):
        return True
    
    async def create(self, user, data):
        return True