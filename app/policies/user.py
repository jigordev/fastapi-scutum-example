from app.core.security import gate

@gate.policy("users")
class UserPolicy:
    def view(self, user):
        return user.role == "admin"
    
    def create(self, user, data):
        return user.role == "admin"