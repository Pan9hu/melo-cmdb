from datetime import datetime
from model.account_model import AccountModel
from util.aes_util import AESUtil
from util.jwt_util import JWTUtil


class AuthService:
    @staticmethod
    def login(username: str, password: str, login_time: datetime):
        byte_password = AccountModel.auth_user(username)
        if byte_password is None:
            return None, None, "20000"
        elif byte_password:
            r_password = str(AESUtil.decrypt(eval(byte_password.get_password())["byte_password"]), 'utf-8')
            if r_password == password:
                access_token = JWTUtil.generate_token(username, login_time, True)
                refresh_token = JWTUtil.generate_token(username, login_time, False)
                if access_token is Exception or refresh_token is Exception:
                    return access_token, refresh_token, "40000"
                else:
                    return access_token, refresh_token, "10000"
            else:
                return None, None, "30000"

    @staticmethod
    def refresh(refresh: str):
        return JWTUtil.refresh_token(refresh)

    @staticmethod
    def security_code(username: str, auth_method: str):
        pass

    @staticmethod
    def reset_password(username: str, password: str):
        pass
