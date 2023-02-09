from flask import request, Blueprint


class OverViewAPI:
    api = Blueprint("overview", __name__, url_prefix="/overview")
