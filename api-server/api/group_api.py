from datetime import datetime
from flask import request, Blueprint
from flask_restful import marshal
from bean.dto.group_dto import GroupDTO
from core.response.generic_json_response import GenericJSONResponse
from service.group_service import GroupService
from util.request_util import RequestUtil
from util.string_util import StringUtil
from util.token_handler import TokenHandler


class GroupAPI:
    api = Blueprint("group", __name__, url_prefix="/group")

    @staticmethod
    @api.route("/<name>", methods=('GET',))
    def get_group_by_name(name):
        """
        通过组名来获取组的详细信息
        :param
        """
        p_token = RequestUtil.get_param_from_headers(request, "X-Auth-Token")
        # 获取token 并在下面验证是否过期
        handler_result = TokenHandler.token_handler(p_token)
        if handler_result:
            return handler_result
        group = GroupService.get_group_by_name(StringUtil.smart_trim("%s" % name))
        # 将Get请求的name参数过滤后，调用对应的Service层模块
        group_dto = [GroupDTO(
            group.get_name(),
            group.get_usage(),
            group.get_create_time(),
            group.get_update_time(),
        )]
        # 获取经过Dao层处理后的数据
        return GenericJSONResponse(data=marshal(group_dto, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('GET',))
    def get_group():
        """
        获取url中的参数根据usage来获取组，如果参数为空则返回全部组的数据
        """
        p_token = RequestUtil.get_param_from_headers(request, "X-Auth-Token")
        handler_result = TokenHandler.token_handler(p_token)
        if handler_result:
            return handler_result
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        usage = StringUtil.smart_trim(p_usage)

        groups = GroupService.get_group(usage)

        dto_list = []
        # 创建一个dto字典，用于将获得的数据逐个输入进去
        for group in groups:
            dto_list.append(GroupDTO(group.get_name(),
                                     group.get_usage(),
                                     group.get_create_time(),
                                     group.get_update_time()))
        # 将数据append到字典中
        return GenericJSONResponse(data=marshal(dto_list, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('POST',))
    def create_group():
        p_token = RequestUtil.get_param_from_headers(request, "X-Auth-Token")
        handler_result = TokenHandler.token_handler(p_token)
        if handler_result:
            return handler_result
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")

        name = StringUtil.smart_trim(p_name)
        usage = StringUtil.smart_trim(p_usage)
        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        GroupService.create_group(name, usage, create_time, update_time)

        group = GroupService.get_group_by_name(StringUtil.smart_trim("%s" % name))
        # 将Get请求的name参数过滤后，调用对应的Service层模块
        group_dto = [GroupDTO(
            group.get_name(),
            group.get_usage(),
            group.get_create_time(),
            group.get_update_time(),
        )]
        # 获取经过Dao层处理后的数据
        return GenericJSONResponse(data=marshal(group_dto, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/<name>", methods=('PUT',))
    def update_group_by_name(name):
        p_token = RequestUtil.get_param_from_headers(request, "X-Auth-Token")
        handler_result = TokenHandler.token_handler(p_token)
        if handler_result:
            return handler_result
        f_name = StringUtil.smart_trim("%s" % name)
        p_usage = RequestUtil.get_param_from_body_raw_json(request, "usage")
        usage = StringUtil.smart_trim(p_usage)
        update_time = datetime.utcnow()

        GroupService.update_group_by_name(f_name, usage, update_time)
        group = GroupService.get_group_by_name(f_name)
        # 将Get请求的name参数过滤后，调用对应的Service层模块
        group_dto = [GroupDTO(
            group.get_name(),
            group.get_usage(),
            group.get_create_time(),
            group.get_update_time(),
        )]
        # 获取经过Dao层处理后的数据
        return GenericJSONResponse(data=marshal(group_dto, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/<name>", methods=('DELETE',))
    def delete_group_by_name(name):
        p_token = RequestUtil.get_param_from_headers(request, "X-Auth-Token")
        handler_result = TokenHandler.token_handler(p_token)
        if handler_result:
            return handler_result
        f_name = StringUtil.smart_trim("%s" % name)
        GroupService.delete_group_by_name(f_name)

        group = []
        # 获取经过Dao层处理后的数据
        return GenericJSONResponse(data=marshal(group, fields=GroupDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=('DELETE',))
    def delete_group():
        p_token = RequestUtil.get_param_from_headers(request, "X-Auth-Token")
        handler_result = TokenHandler.token_handler(p_token)
        if handler_result:
            return handler_result
        name_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(name_list) > 0:
            GroupService.delete_group(name_list)

        groups = GroupService.get_group("")

        dto_list = []
        # 创建一个dto字典，用于将获得的数据逐个输入进去
        for group in groups:
            dto_list.append(GroupDTO(group.get_name(),
                                     group.get_usage(),
                                     group.get_create_time(),
                                     group.get_update_time()))
        # 将数据append到字典中
        return GenericJSONResponse(data=marshal(dto_list, fields=GroupDTO.fields)).build()
