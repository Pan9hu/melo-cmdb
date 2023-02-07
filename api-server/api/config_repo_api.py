from flask import Blueprint


class ConfigRepoAPI:
    api = Blueprint("config_repo", __name__, url_prefix="/config-repo")
