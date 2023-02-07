from flask import Blueprint

from service.machine_service import MachineService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class MachineAPI:
    api = Blueprint("machine", __name__, url_prefix="/machine")

    @staticmethod
    @api.route("/<uuid>", methods="GET")
    def get_machine_by_uuid(uuid):
        MachineService.get_machine_by_uuid(StringUtil.smart_trim(uuid))

        return {}

    @staticmethod
    @api.route("/<uuid>", methods="GET")
    def list_machine(uuid):
        p_service = RequestUtil.get_param_from_url_query_param(request, "service")
        p_res_pool = RequestUtil.get_param_from_url_query_param(request, "res_pool")
        p_service = RequestUtil.get_param_from_url_query_param(request, "service")
        p_service = RequestUtil.get_param_from_url_query_param(request, "service")
