from flask import Blueprint


class ServiceAPI:
    api = Blueprint("service", __name__, url_prefix="/service")
