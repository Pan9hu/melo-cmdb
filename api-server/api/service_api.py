from flask import request, Blueprint

from service.service_service import ServiceService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class ServiceAPI:
    api = Blueprint("service", __name__, url_prefix="/service")

    @staticmethod
    @api.route("/<name>", methods="GET")
    def get_service_by_name(name):
        ServiceService.get_service_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/<name>", methods="GET")
    def get_service(level, parent, usage):
        p_level = RequestUtil.get_param_from_body_raw_json(request, "level")
        p_parent = RequestUtil.get_param_from_body_raw_json(request, "parent")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        level = StringUtil.smart_trim(p_level)
        parent = StringUtil.smart_trim(p_parent)
        usage = StringUtil.smart_trim(p_usage)

        ServiceService.get_service(level, parent, usage)
        return {}

    @staticmethod
    @api.route("/<name>", methods="GET")
    def delete_service_by_name(name):
        pass

    @staticmethod
    @api.route("/", methods="GET")
    def delete_service():
        pass

    @staticmethod
    @api.route("/", methods="GET")
    def create_service():
        pass
