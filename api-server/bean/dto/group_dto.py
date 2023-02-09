from datetime import datetime
from flask_restful import fields


class GroupDTO:
    fields = {
        "name": fields.String,
        "usage": fields.String,
        "create_time": fields.DateTime(attribute="create_time"),
        "update_time": fields.DateTime(attribute="update_time")

    }

    def __init__(self, name: str = None,
                 usage: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(), ):
        self.name = name
        self.usage = usage
        self.create_time = create_time
        self.update_time = update_time

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    # ============================

    def get_usage(self) -> str:
        return self.usage

    def set_usage(self, usage: str):
        self.usage = usage

    # ============================

    def get_create_time(self) -> datetime:
        return self.create_time

    def set_create_time(self, create_time: datetime):
        self.create_time = create_time

    # ============================

    def get_update_time(self) -> datetime:
        return self.update_time

    def set_update_time(self, update_time: datetime):
        self.update_time = update_time
