from model.account_model import AccountModel
from datetime import datetime


class AccountService:

    @staticmethod
    def get_account_by_uid(uid: str):
        return AccountModel.get_account_by_uid(uid)

    @staticmethod
    def list_account(name: str | None, group: str | None, phone: str | None, email: str | None, sex: str | None,
                     arch_group: str | None):
        if name is None and group is None and phone is None and email is None and sex is None and arch_group is None:
            return AccountModel.all_account()
        else:
            return AccountModel.get_account()

    @staticmethod
    def create_account(uid: str, name: str, group: str, sex: str, phone: str, email: str, arch_group: str,
                       create_time: datetime,
                       update_time: datetime):
        if uid is None or name is None:
            return {}
        AccountModel.create_account(uid, name, group, sex, phone, email, arch_group, create_time, update_time)

    @staticmethod
    def delete_account_by_uid(uid):
        pass

    @staticmethod
    def delete_account(uid_list:list):
        if len(uid_list) == 0:
            return []
        AccountModel.delete_account(uid_list)

    @staticmethod
    def update_account(uid, name, phone, email, sex, arch_group):
        pass
