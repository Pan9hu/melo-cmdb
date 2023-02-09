from datetime import datetime


class TaskDetail:
    def __init__(self, _id: str = None,
                 machine_id: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 status: str = None,
                 is_delete: bool = None):
        self.__id = _id
        self.__machine_id = machine_id
        self.__create_time = create_time
        self.__update_time = update_time
        self.__status = status
        self.__is_delete = is_delete

    def get__id(self) -> str:
        return self.__id

    def set__id(self, _id: str):
        self.__id = _id

    # ============================

    def get_machine_id(self) -> str:
        return self.__machine_id

    def set_machine_id(self, machine_id: str):
        self.__machine_id = machine_id

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

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    # ============================

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool):
        self.__is_delete = is_delete
