from flask import request, Blueprint

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login", methods=('POST',))
def login():
    return "Login"
