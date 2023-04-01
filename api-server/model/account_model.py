from bean.pojo.account import Account
from core.server import Server
from datetime import datetime


class AccountModel:

    @staticmethod
    def get_account_by_uid(uid: str) -> Account:
        result = Server.datasource["default"].db["account"].find_one({"_id": uid, "is_delete": False})

        return Account(username=result["_id"],
                       name=result["name"],
                       phone=result["phone"],
                       email=result["email"],
                       group=result["group"],
                       sex=result["sex"],
                       arch_group=result["arch_group"],
                       create_time=result["create_time"],
                       update_time=result["update_time"])

    @staticmethod
    def all_account() -> list:
        result = Server.datasource["default"].db["account"].find({"is_delete": False})

        accounts = []

        for item in result:
            accounts.append(Account(username=item["_id"],
                                    name=item["name"],
                                    phone=item["phone"],
                                    email=item["email"],
                                    group=item["group"],
                                    sex=item["sex"],
                                    arch_group=item["arch_group"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]))

        return accounts

    @staticmethod
    def get_account():
        pass

    @staticmethod
    def create_account(uid: str, name: str, group: str, sex: str, phone: str, email: str, arch_group: str,
                       create_time: datetime,
                       update_time: datetime):
        Server.datasource["default"].db["account"].insert_one({"_id": uid,
                                                               "name": name,
                                                               "group": group,
                                                               "sex": sex,
                                                               "phone": phone,
                                                               "email": email,
                                                               "arch_group": arch_group,
                                                               "create_time": create_time,
                                                               "update_time": update_time,
                                                               "is_delete": False})

    @staticmethod
    def delete_account(uid_list: list):
        for uid in uid_list:
            Server.datasource["default"].db["account"].delete_one({"_id": uid})
