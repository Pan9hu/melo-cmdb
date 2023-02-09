from datetime import datetime


class Machine:
    def __init__(self, _id: str = None,
                 _type: str = None,
                 service: str = None,
                 res_pool: str = None,
                 safe_group: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 status: str = None,
                 is_delete: bool = None):
        self.__id = _id
        self.__type = _type
        self.__service = service
        self.__res_pool = res_pool
        self.__safe_group = safe_group
        self.__create_time = create_time
        self.__update_time = update_time
        self.__status = status
        self.__is_delete = is_delete

    def get_id(self) -> str:
        return self.__id

    def set_id(self, _id: str = None):
        self.__id = _id

    # ============================

    def get_type(self) -> str:
        return self.__type

    def set_type(self, _type: str):
        self.__type = _type

    # ============================

    def get_res_pool(self) -> str:
        return self.__res_pool

    def set_res_pool(self, res_pool: str):
        self.__res_pool = res_pool

    # ============================

    def get_safe_group(self) -> str:
        return self.__safe_group

    def set_safe_group(self, safe_group: str):
        self.__safe_group = safe_group

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
