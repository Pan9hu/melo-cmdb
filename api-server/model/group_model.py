from bean.pojo.group import Group
from core.server import Server
from datetime import datetime


class GroupModel:

    @staticmethod
    def get_group_by_name(name: str) -> Group:
        result = Server.datasource["default"].db["group"].find_one({"_id": name, "is_delete": False})

        # 获取连接池并通过名字查找数据
        return Group(name=result["_id"],
                     usage=result["usage"],
                     create_time=result["create_time"],
                     update_time=result["update_time"])

    @staticmethod
    def all_group() -> list:
        result = Server.datasource["default"].db["group"].find({"is_delete": False})

        groups = []

        for item in result:
            groups.append(Group(name=item["_id"],
                                usage=item["usage"],
                                create_time=item["create_time"],
                                update_time=item["update_time"]))
        return groups

    @staticmethod
    def get_group(usage: str) -> list:
        result = Server.datasource["default"].db["group"].find({"usage": usage, "is_delete": False})

        groups = []
        for item in result:
            groups.append(Group(name=item["_id"],
                                usage=item["usage"],
                                create_time=item["create_time"],
                                update_time=item["update_time"]))
        if not groups:
            result = Server.datasource["default"].db["group"].find({"usage": {"$regex": usage}, "is_delete": False})
            for item in result:
                groups.append(Group(name=item["_id"],
                                    usage=item["usage"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]))
        if not groups:
            result = Server.datasource["default"].db["group"].find({"name": {"$regex": usage}, "is_delete": False})
            for item in result:
                groups.append(Group(name=item["_id"],
                                    usage=item["usage"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]))

        return groups

    @staticmethod
    def create_group(name: str, usage: str, create_time: datetime, update_time: datetime):
        Server.datasource["default"].db["group"].insert_one({"_id": name,
                                                             "usage": usage,
                                                             "create_time": create_time,
                                                             "update_time": update_time,
                                                             "is_delete": False})

    @staticmethod
    def delete_group_by_name(name: str):
        Server.datasource["default"].db["group"].delete_one({"_id": name})

    @staticmethod
    def delete_group(name_list: list):
        for groupName in name_list:
            Server.datasource["default"].db["group"].delete_one({"_id": groupName})

    @staticmethod
    def update_group_by_name(name: str, usage: str, update_time: datetime):
        Server.datasource["default"].db["group"].find_one_and_update({"_id": name},
                                                                     {"$set": {"usage": usage,
                                                                               "update_time": update_time}},
                                                                     {"is_delete": False})
