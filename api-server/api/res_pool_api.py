from flask import Blueprint


class ResPoolAPI:
    api = Blueprint("res_pool", __name__, url_prefix="/res-pool")
