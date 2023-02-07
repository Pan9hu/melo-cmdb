from datetime import datetime

from flask import request, Blueprint

from service.group_service import GroupService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class GroupAPI:
    api = Blueprint("group", __name__, url_prefix="/group")

    @staticmethod
    @api.route("/<name>", methods="GET")
    def get_group_by_name(name):
        GroupService.get_group_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/", methods="GET")
    def get_group():
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        usage = StringUtil.smart_trim(p_usage)

        GroupService.get_group(usage)

        return {}

    @staticmethod
    @api.route("/", methods="POST")
    def create_group():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        usage = StringUtil.smart_trim(p_usage)

        create_time = datetime.now()
        update_time = datetime.now()

        GroupService.create_group(name, usage, create_time, update_time)
        return {}

    @staticmethod
    @api.route("/<name>", methods="PUT")
    def update_group_by_name(name):
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")
        usage = StringUtil.smart_trim(p_usage)

        GroupService.update_group_by_name(StringUtil.smart_trim(name), usage)

        return {}

    @staticmethod
    @api.route("/<name>", methods="DELETE")
    def delete_group_by_name(name):
        GroupService.delete_group_by_name(StringUtil.smart_trim(name))

    @staticmethod
    @api.route("/", methods="DELETE")
    def delete_group(name):
        name_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(name_list) > 0:
            GroupService.delete_group(StringUtil.smart_trim(name))
