from flask import Blueprint


class GroupAPI:
    api = Blueprint("group", __name__, url_prefix="/group")
