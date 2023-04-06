from datetime import datetime
from model.account_model import AccountModel
from util.jwt_util import JWTUtile


class AuthService:
    @staticmethod
    def login(username: str, password: str, login_time: datetime):
        r_password = AccountModel.auth_user(username)
        if r_password is None:
            return None, None, "20000"
        elif r_password.get_password() == password:
            access_token = JWTUtile.generate_token(username, login_time, True)
            refresh_token = JWTUtile.generate_token(username, login_time, False)
            if access_token is Exception or refresh_token is Exception:
                return access_token, refresh_token, "40000"
            else:
                return access_token, refresh_token, "10000"
        else:
            return None, None, "30000"

    @staticmethod
    def refresh(refresh: str):
        pass

    @staticmethod
    def reset_password(username):
        pass
