from datetime import datetime
from flask import request, Blueprint
from flask_restful import marshal
from bean.dto.group_dto import GroupDTO
from core.response.generic_json_response import GenericJSONResponse
from service.group_service import GroupService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class GroupAPI:
    api = Blueprint("group", __name__, url_prefix="/group")

    @staticmethod
    @api.route("/<name>", methods=('GET',))
    def get_group_by_name(name):
        group = GroupService.get_group_by_name(StringUtil.smart_trim(name))

        group_dto = GroupDTO(
            name=group.get_name(),
            usage=group.get_usage(),
            create_time=group.get_create_time(),
            update_time=group.get_update_time(),
        )

        return GenericJSONResponse(data=marshal(group_dto, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('GET',))
    def get_group():
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        usage = StringUtil.smart_trim(p_usage)

        groups = GroupService.get_group(usage)

        dto_list = []

        for group in groups:
            dto_list.append(GroupDTO(group.get_name(),
                                     group.get_usage(),
                                     group.get_create_time(),
                                     group.get_update_time()))

        return GenericJSONResponse(data=marshal(dto_list, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('POST',))
    def create_group():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        usage = StringUtil.smart_trim(p_usage)

        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        GroupService.create_group(name, usage, create_time, update_time)
        return {}

    @staticmethod
    @api.route("/<name>", methods=('PUT',))
    def update_group_by_name(name):
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")
        usage = StringUtil.smart_trim(p_usage)

        GroupService.update_group_by_name(StringUtil.smart_trim(name), usage)

        return {}

    @staticmethod
    @api.route("/<name>", methods=('DELETE',))
    def delete_group_by_name(name):
        GroupService.delete_group_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/", methods=('DELETE',))
    def delete_group():
        name_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(name_list) > 0:
            GroupService.delete_group(name_list)

        return {}
