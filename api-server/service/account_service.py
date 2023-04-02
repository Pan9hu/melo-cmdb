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
            condition_dict = {'name': "" if name is None else name, 'group': "" if group is None else group,
                              'phone': "" if phone is None else phone, 'email': "" if email is None else email,
                              'sex': "" if sex is None else sex,
                              'arch_group': "" if arch_group is None else arch_group}
            return AccountModel.get_account(condition_dict)

    @staticmethod
    def create_account(uid: str, name: str, group: str, sex: str, phone: str, email: str, arch_group: str,
                       create_time: datetime,
                       update_time: datetime):
        if uid is None or name is None:
            return {}
        AccountModel.create_account(uid, name, group, sex, phone, email, arch_group, create_time, update_time)

    @staticmethod
    def delete_account_by_uid(uid: str):
        if uid is None:
            return {}
        AccountModel.delete_account_by_uid(uid)

    @staticmethod
    def delete_account(uid_list: list):
        if len(uid_list) == 0:
            return []
        AccountModel.delete_account(uid_list)

    @staticmethod
    def update_account(uid: str, name: str, group: str, phone: str, email: str, sex: str, arch_group: str,
                       update_time: datetime):
        if uid is None:
            return {}
        elif name is None and group is None and phone is None and email is None and sex is None and arch_group is None:
            return {}
        update_fields_dict = {'name': name, 'group': group, 'phone': phone, 'email': email, 'sex': sex,
                              'arch_group': arch_group, 'update_time': update_time}
        update_dict = {}
        for field in update_fields_dict:
            if update_fields_dict[field] is None:
                continue
            else:
                update_dict[field] = update_fields_dict[field]

        AccountModel.update_account(uid, update_dict)
