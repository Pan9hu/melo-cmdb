from flask import Blueprint


class TaskAPI:
    api = Blueprint("task", __name__, url_prefix="/task")
