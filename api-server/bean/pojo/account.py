from datetime import datetime


class Account:
    def __init__(self, name: str = None,
                 username: str = None,
                 password: str = None,
                 phone: str = None,
                 email: str = None,
                 group: str = None,
                 sex: str = None,
                 arch_group: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 is_delete: bool = None):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__phone = phone
        self.__email = email
        self.__group = group
        self.__sex = sex
        self.__arch_group = arch_group
        self.__create_time = create_time
        self.__update_time = update_time
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    # ============================

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username: str):
        self.__username = username

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

    def get_group(self) -> str:
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    # ============================

    def get_sex(self) -> str:
        return self.__sex

    def set_sex(self, sex: str):
        self.__sex = sex

    # ============================

    def get_arch_group(self) -> str:
        return self.__arch_group

    def set_arch_group(self, arch_group: str):
        self.__arch_group = arch_group

    # ============================

    def get_create_time(self) -> datetime:
        return self.__create_time

    def set_create_time(self, create_time: datetime):
        self.__create_time = create_time

    # ============================

    def get_update_time(self) -> datetime:
        return self.__update_time

    def set_update_time(self, update_time: datetime):
        self.__update_time = update_time

    # ============================

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool):
        self.__is_delete = is_delete
