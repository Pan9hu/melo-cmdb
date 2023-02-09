from datetime import datetime

from flask import request, Blueprint

from service.safe_group_service import SafeGroupService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class SafeGroupAPI:
    api = Blueprint("safe_group", __name__, url_prefix="/safe-group")

    @staticmethod
    @api.route("/<name>", methods=('GET',))
    def get_safe_group_by_name(name):
        SafeGroupService.get_safe_group_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/", methods=('GET',))
    def list_safe_group():
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")
        usage = StringUtil.smart_trim(p_usage)

        SafeGroupService.list_safe_group(usage)

        return {}

    @staticmethod
    @api.route("/", methods=('POST',))
    def create_safe_group():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_ports = RequestUtil.get_param_from_body_raw_json(request, "ports")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        ports = StringUtil.smart_trim(p_ports)
        usage = StringUtil.smart_trim(p_usage)

        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        SafeGroupService.create_safe_group(name, ports, usage, create_time, update_time)

        return {}

    @staticmethod
    @api.route("/<name>", methods=('PUT',))
    def update_safe_group_by_name(name):
        p_ports = RequestUtil.get_param_from_body_raw_json(request, "ports")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        ports = StringUtil.smart_trim(p_ports)
        usage = StringUtil.smart_trim(p_usage)
        update_time = datetime.utcnow()

        SafeGroupService.update_safe_group_by_name(StringUtil.smart_trim(name), ports, usage, update_time)

        return {}

    @staticmethod
    @api.route("/<name>", methods=('DELETE',))
    def delete_safe_group_by_name(name):
        SafeGroupService.delete_safe_group_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/", methods=('DELETE',))
    def delete_safe_group(name):
        name_list =RequestUtil.get_param_from_body_raw_json_as_list(request)
        if len(name) > 0:
            SafeGroupService.delete_safe_group(name_list)

        return {}
