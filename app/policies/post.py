from app.core.security import auth_config

@auth_config.gate.policy("posts")
class PostPolicy:
    def view(self, user, post):
        return True
    
    def create(self, user, data):
        return True