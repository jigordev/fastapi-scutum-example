from app.core.security import gate

@gate.policy("posts")
class PostPolicy:
    def view(self, user, post):
        return True
    
    def create(self, user, data):
        return True