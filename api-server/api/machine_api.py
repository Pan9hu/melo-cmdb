from flask import Blueprint


class MachineAPI:
    api = Blueprint("machine", __name__, url_prefix="/machine")
