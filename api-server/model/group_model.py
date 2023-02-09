from bean.pojo.group import Group
from core.server import Server


class GroupModel:

    @staticmethod
    def get_group_by_name(name) -> Group:
        result = Server.datasource["default"].db["group"].find_one({"_id": name})

        return Group(name=result["_id"],
                     usage=result["usage"],
                     create_time=result["create_time"],
                     update_time=result["update_time"])

    @staticmethod
    def all_group():
        result = Server.datasource["default"].db["group"].find({"is_delete": False})

        groups = []

        for item in result:
            groups.append(Group(name=item["_id"],
                                usage=item["usage"],
                                create_time=item["create_time"],
                                update_time=item["update_time"]))
        return groups

    @staticmethod
    def get_group(usage: str):
        result = Server.datasource["default"].db["group"].find({"usage": usage})

        return result
