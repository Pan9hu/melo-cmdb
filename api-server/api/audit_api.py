from flask import Blueprint


class AuditAPI:
    api = Blueprint("audit", __name__, url_prefix="/audit")


    @staticmethod
    @api.route("/",methods="GET")
    def list_audit():
        pass
