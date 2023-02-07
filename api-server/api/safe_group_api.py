from flask import Blueprint


class SafeGroupAPI:
    api = Blueprint("safe_group", __name__, url_prefix="/safe-group")
