from flask import Blueprint

bp_audit = Blueprint("audit", __name__, url_prefix="/audit")
