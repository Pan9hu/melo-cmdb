from flask import Blueprint


class ConfigRepoAPI:
    api = Blueprint("config_repo", __name__, url_prefix="/config-repo")


    @staticmethod
    @api.route("/<name>",methods="GET")
    def get_config_repo_by_name(name):
        return {}

    @staticmethod
    @api.route("/", methods="GET")
    def list_config_repo():
        return {}

    @staticmethod
    @api.route("/", methods="POST")
    def create_config_repo ():
        return {}

    @staticmethod
    @api.route("/<name>", methods="PUT")
    def update_config_repo_by_name(name):
        return {}

    @staticmethod
    @api.route("/<name>", methods="DELETE")
    def delete_config_repo_by_name(name):
        return {}

    @staticmethod
    @api.route("/", methods="DELETE")
    def delete_config_repo():
        return {}
