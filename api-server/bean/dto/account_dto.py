from datetime import datetime
from flask_restful import fields


class AccountDTO:
    fields = {
        "name": fields.String,
        "username": fields.String,
        "password": fields.String,
        "phone": fields.String,
        "email": fields.String,
        "group": fields.String,
        "sex": fields.String,
        "arch_group": fields.String,
        "create_time": fields.DateTime(attribute="create_time"),
        "update_time": fields.DateTime(attribute="update_time")
    }

    def __init__(self, name: str = None,
                 username: str = None,
                 password: str = None,
                 phone: str = None,
                 email: str = None,
                 group: str = None,
                 sex: str = None,
                 arch_group: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow()):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.group = group
        self.sex = sex
        self.arch_group = arch_group
        self.create_time = create_time
        self.update_time = update_time

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

        # ============================

    def get_username(self) -> str:
        return self.username

    def set_username(self, username: str):
        self.username = username

        # ============================

    def get_phone(self) -> str:
        return self.phone

    def set_phone(self, phone: str):
        self.phone = phone

        # ============================

    def get_password(self) -> str:
        return self.password

    def set_password(self, password: str):
        self.password = password

        # ============================

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

        # ============================

    def get_group(self) -> str:
        return self.group

    def set_group(self, group: str):
        self.group = group

        # ============================

    def get_sex(self) -> str:
        return self.sex

    def set_sex(self, sex: str):
        self.sex = sex

        # ============================

    def get_arch_group(self) -> str:
        return self.arch_group

    def set_arch_group(self, arch_group: str):
        self.arch_group = arch_group

        # ============================

    def get_create_time(self) -> datetime:
        return self.create_time

    def set_create_time(self, create_time: datetime):
        self.create_time = create_time

        # ============================

    def get_update_time(self) -> datetime:
        return self.update_time

    def set_update_time(self, update_time: datetime):
        self.update_time = update_time
