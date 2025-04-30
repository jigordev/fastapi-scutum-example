from scutum import Policy

class UserPolicy(Policy):
    def view(self, user):
        return user.role == "admin"
    
    def create(self, user, data):
        return user.role == "admin"