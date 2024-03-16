from rest_framework_simplejwt.tokens import RefreshToken


class Token:
    def __init__(self, user, request) -> None:
        self.user = user
        self.request = request
    
    def generate_token(self):
        token = RefreshToken.for_user(self.user).access_token
        return token
