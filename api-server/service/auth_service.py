from datetime import datetime
from model.account_model import AccountModel
from util.jwt_util import JWTUtile


class AuthService:
    @staticmethod
    def login(username: str, password: str, login_time: datetime):
        r_password = AccountModel.auth_user(username)
        if r_password.get_password() == password:
            tokens = JWTUtile.generate_token(username, login_time)
            if tokens is not None:
                return tokens
        else:
            return 0

    @staticmethod
    def refresh(refresh):
        pass

    @staticmethod
    def reset_password(username):
        pass
