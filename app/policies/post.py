from scutum import Policy

class PostPolicy(Policy):
    def view(self, user, post):
        return True
    
    def create(self, user, data):
        return True