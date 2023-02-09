from bean.pojo.group import Group


class GroupDTO:
    def __init__(self, o: Group):
        self.o = o

    def to_json(self) -> dict | list:
        return {
            "name": self.o.get_name(),
            "usage": self.o.get_usage(),
            "ctime": self.o.get_create_time(),
            "utime": self.o.get_update_time()
        }
