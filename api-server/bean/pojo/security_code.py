from datetime import datetime


class SecurityCode:

    def __init__(self, name: str = None,
                 auth_method: str = None,
                 phone: str = None,
                 email: str = None,
                 expired_time: datetime = datetime.utcnow()):
        self.__name = name
        self.__auth_method = auth_method
        self.__phone = phone
        self.__email = email
        self.__expired_time = expired_time

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    # ============================

    def get_auth_method(self) -> str:
        return self.__auth_method

    def set_auth_method(self, auth_method: str):
        self.__auth_method = auth_method

    # ============================

    def get_phone(self) -> str:
        return self.__phone

    def set_phone(self, phone: str):
        self.__phone = phone

    # ============================

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    # ============================

    def get_expired_time(self) -> datetime:
        return self.__expired_time

    def set_create_time(self, expired_time: datetime):
        self.__expired_time = expired_time

    # ============================

