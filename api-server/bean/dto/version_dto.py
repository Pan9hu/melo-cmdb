from flask_restful import fields


class VersionDTO:
    fields = {
        "version": fields.String,
    }

    def __init__(self, version: str = None):
        self.version = version

    def get_name(self) -> str:
        return self.version

    def set_name(self, version: str):
        self.version = version
