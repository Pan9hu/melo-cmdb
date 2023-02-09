from datetime import datetime


class Task:
    def __init__(self, _id: str = None,
                 repo: str = None,
                 branch: str = None,
                 tag: str = None,
                 target_machine: list = None,
                 target_directory: list = None,
                 target_service: list = None,
                 post_sync_script: str = None,
                 webhook_url: str = None,
                 webhook_sign: str = None,
                 logs: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 status: str = None,
                 timeout: datetime = None,
                 is_delete: bool = None,
                 retry: int = 3):
        self.__id = _id
        self.__repo = repo
        self.__branch = branch
        self.__tag = tag
        self.__target_machine = target_machine
        self.__target_directory = target_directory
        self.__target_service = target_service
        self.__post_sync_script = post_sync_script
        self.__webhook_url = webhook_url
        self.__webhook_sign = webhook_sign
        self.__logs = logs
        self.__create_time = create_time
        self.__update_time = update_time
        self.__status = status
        self.__timeout = timeout
        self.__is_delete = is_delete
        self.__retry = retry

    def get__id(self) -> str:
        return self.__id

    def set__id(self, _id: str):
        self.__id = _id

    # ============================

    def get_repo(self) -> str:
        return self.__repo

    def set_repo(self, repo: str):
        self.__repo = repo

    # ============================

    def get_branch(self) -> str:
        return self.__branch

    def set_branch(self, branch: str):
        self.__branch = branch

    # ============================

    def get_tag(self) -> str:
        return self.__tag

    def set_tag(self, tag: str):
        self.__tag = tag

    # ============================

    def get_target_machine(self) -> list:
        return self.__target_machine

    def set_target_machine(self, target_machine: list):
        self.__target_machine = target_machine

    # ============================

    def get_target_directory(self) -> list:
        return self.__target_directory

    def set_target_directory(self, target_directory: list):
        self.__target_directory = target_directory

    # ============================

    def get_target_service(self) -> list:
        return self.__target_directory

    def set_target_service(self, target_service: list):
        self.__target_service = target_service

    # ============================

    def get_post_sync_script(self) -> str:
        return self.__post_sync_script

    def set_post_sync_script(self, post_sync_script: str):
        self.__post_sync_script = post_sync_script

    # ============================

    def get_webhook_url(self) -> str:
        return self.__webhook_url

    def set_webhook_url(self, webhook_url: str):
        self.__webhook_url = webhook_url

    # ============================

    def get_webhook_sign(self) -> str:
        return self.__webhook_sign

    def set_webhook_sign(self, webhook_sign: str):
        self.__webhook_sign = webhook_sign

    # ============================

    def get_logs(self) -> str:
        return self.__logs

    def set_logs(self, logs: str):
        self.__logs = logs

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
    def get_timeout(self) -> datetime:
        return self.__timeout

    def set_timeout(self, timeout: datetime):
        self.__timeout = timeout

    # ============================

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool):
        self.__is_delete = is_delete

    # ============================
    def get_retry(self) -> int:
        return self.__retry

    def set_retry(self, retry: int):
        self.__retry = retry
