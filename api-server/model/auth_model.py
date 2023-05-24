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
    def get_sms_code_by_phone(username: str, auth_method: str) -> SecurityCode | None:
        result = Server.datasource["default"].db["security_code"].find_one(
            {"_id": username, "auth_method": auth_method},
            {"code": 1, "_id": 0})

        if result is None:
            return None
        return SecurityCode(code=result["code"])

    @staticmethod
    def get_sms_code_by_email(username: str, auth_method: str) -> SecurityCode | None:
        pass
