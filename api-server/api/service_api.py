from datetime import datetime

from flask import request, Blueprint

from service.service_service import ServiceService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class ServiceAPI:
    api = Blueprint("service", __name__, url_prefix="/service")

    @staticmethod
    @api.route("/<name>", methods=('GET',))
    def get_service_by_name(name):
        ServiceService.get_service_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/", methods=('GET',))
    def get_service():
        p_level = RequestUtil.get_param_from_body_raw_json(request, "level")
        p_parent = RequestUtil.get_param_from_body_raw_json(request, "parent")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        level = StringUtil.smart_trim(p_level)
        parent = StringUtil.smart_trim(p_parent)
        usage = StringUtil.smart_trim(p_usage)

        ServiceService.get_service(level, parent, usage)
        return {}

    @staticmethod
    @api.route("/<name>", methods=('DELETE',))
    def delete_service_by_name(name):
        ServiceService.delete_service_by_name(StringUtil.smart_trim(name))

    @staticmethod
    @api.route("/", methods=('DELETE',))
    def delete_service():
        name_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(name_list) > 0:
            ServiceService.delete_service(name_list)

        return {}

    @staticmethod
    @api.route("/", methods=('POST',))
    def create_service():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_parent = RequestUtil.get_param_from_body_raw_json(request, "parent")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        parent = StringUtil.smart_trim(p_parent)
        usage = StringUtil.smart_trim(p_usage)
        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        ServiceService.create_service(name, parent, usage, create_time, update_time)

        return {}

    @staticmethod
    @api.route("/", methods=('POST',))
    def update_service_by_name(name):
        p_parent = RequestUtil.get_param_from_body_raw_json(request, "parent")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        parent = StringUtil.smart_trim(p_parent)
        usage = StringUtil.smart_trim(p_usage)
        update_time = datetime.utcnow()

        ServiceService.update_service_by_name(StringUtil.smart_trim(name), parent, usage, update_time)
        return {}

    @staticmethod
    @api.route("/safe-group/<name>", methods=('POST',))
    def change_safe_group():
        safe_group_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(safe_group_list) > 0:
            ServiceService.change_safe_group(safe_group_list)

        return {}