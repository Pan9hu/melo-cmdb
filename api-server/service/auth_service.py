from datetime import datetime
from model.account_model import AccountModel
from util.aes_util import AESUtil
from util.jwt_util import JWTUtil
from util.random_util import RandomUtil
from util.sms_verification_util import SMSVerificationUtil


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
        username_detail = AccountModel.get_account_by_uid(username)
        if auth_method == "phone":
            phone = username_detail.get_phone()
            if phone is not None:
                code = RandomUtil.get_random()
                template_param = str({'code': code})
                b_mes = SMSVerificationUtil.send_sms(phone, template_param)
                mes = eval(str(b_mes, encoding='utf-8'))
                if mes["Message"] == "OK":
                    return mes["Message"]
        elif auth_method == "email":
            email = username_detail.get_email()

    @staticmethod
    def reset_password(username: str, password: str):
        pass
