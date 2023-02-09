from flask import Blueprint, request

from service.audit_service import AuditService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AuditAPI:
    api = Blueprint("audit", __name__, url_prefix="/audit")

    @staticmethod
    @api.route("/", methods=('GET',))
    def list_audit():
        p_level = RequestUtil.get_param_from_url_query_param(request, "level")
        p_result = RequestUtil.get_param_from_url_query_param(request, "result")
        p_uid = RequestUtil.get_param_from_url_query_param(request, "uid")
        p_name = RequestUtil.get_param_from_url_query_param(request, "name")
        p_event = RequestUtil.get_param_from_url_query_param(request, "event")

        level = StringUtil.smart_trim(p_level)
        result = StringUtil.smart_trim(p_result)
        uid = StringUtil.smart_trim(p_uid)
        name = StringUtil.smart_trim(p_name)
        event = StringUtil.smart_trim(p_event)

        AuditService.list_audit(level, uid, result, name, event)

        return {}
