from core.server import Server
from bean.pojo.security_code import SecurityCode
from datetime import datetime


class AuthModel:

    @staticmethod
    def create_sms_code_by_phone(username: str, code: str, auth_method: str, phone: str, expired_time: datetime):
        Server.datasource["default"].db["security_code"].insert_one(
            {"_id": username, "code": code, "auth_method": auth_method, "phone": phone, "expiredAt": expired_time})

    @staticmethod
    def create_sms_code_by_email(email: str):
        pass

    @staticmethod
    def get_sms_code_by_phone(phone: str):
        pass

    @staticmethod
    def get_sms_code_by_email(email: str):
        pass
