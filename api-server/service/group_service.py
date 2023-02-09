from model.group_model import GroupModel


class GroupService:

    @staticmethod
    def get_group_by_name(name: str):
        return GroupModel.get_group_by_name(name)

    @staticmethod
    def get_group(name):
        pass

    @staticmethod
    def create_group(name, usage, create_time, update_time):
        pass

    @staticmethod
    def update_group_by_name(name, usage):
        pass

    @staticmethod
    def delete_group_by_name(name):
        pass

    @staticmethod
    def delete_group(name_list):
        pass
