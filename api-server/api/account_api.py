from flask import request, Blueprint
from datetime import datetime
from flask_restful import marshal
from bean.dto.account_dto import AccountDTO
from core.response.generic_json_response import GenericJSONResponse
from service.account_service import AccountService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AccountAPI:
    api = Blueprint("account", __name__, url_prefix="/account")

    @staticmethod
    @api.route("/<uid>", methods=("GET",))
    def get_account_by_uid(uid):
        """
        根据工号，精确搜索
        :param uid:
        :return:
        """
        account = AccountService.get_account_by_uid(StringUtil.smart_trim("%s" % uid))
        account_dto = [AccountDTO(username=account.get_username(),
                                  name=account.get_name(),
                                  group=account.get_group(),
                                  phone=account.get_phone(),
                                  email=account.get_email(),
                                  sex=account.get_sex(),
                                  arch_group=account.get_arch_group(),
                                  create_time=account.get_create_time(),
                                  update_time=account.get_update_time()
                                  )]

        return GenericJSONResponse(data=marshal(account_dto, fields=AccountDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=("GET",))
    def list_account():
        """
        根据条件进行匹配
        :return:
        """
        p_name = RequestUtil.get_param_from_url_query_param(request, "name")
        p_group = RequestUtil.get_param_from_url_query_param(request, "group")
        p_phone = RequestUtil.get_param_from_url_query_param(request, "phone")
        p_email = RequestUtil.get_param_from_url_query_param(request, "email")
        p_sex = RequestUtil.get_param_from_url_query_param(request, "sex")
        p_arch_group = RequestUtil.get_param_from_url_query_param(request, "arch_group")

        name = StringUtil.smart_trim(p_name)
        group = StringUtil.smart_trim(p_group)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)

        accounts = AccountService.list_account(name, group, phone, email, sex, arch_group)

        dto_list = []
        for account in accounts:
            dto_list.append(AccountDTO(username=account.get_username(),
                                       name=account.get_name(),
                                       group=account.get_group(),
                                       phone=account.get_phone(),
                                       email=account.get_email(),
                                       sex=account.get_sex(),
                                       arch_group=account.get_arch_group(),
                                       create_time=account.get_create_time(),
                                       update_time=account.get_update_time()))

        return GenericJSONResponse(data=marshal(dto_list, fields=AccountDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=("POST",))
    def create_account():
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_uid = RequestUtil.get_param_from_body_raw_json(request, "uid")
        p_group = RequestUtil.get_param_from_body_raw_json(request, "group")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "sex")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "phone")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "email")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "arch_group")

        uid = StringUtil.smart_trim(p_uid)
        name = StringUtil.smart_trim(p_name)
        group = StringUtil.smart_trim(p_group)
        sex = StringUtil.smart_trim(p_sex)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        arch_group = StringUtil.smart_trim(p_arch_group)
        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        AccountService.create_account(uid, name, group, sex, phone, email, arch_group, create_time, update_time)
        account = AccountService.get_account_by_uid(uid)
        account_dto = [AccountDTO(username=account.get_username(),
                                  name=account.get_name(),
                                  group=account.get_group(),
                                  phone=account.get_phone(),
                                  email=account.get_email(),
                                  sex=account.get_sex(),
                                  arch_group=account.get_arch_group(),
                                  create_time=account.get_create_time(),
                                  update_time=account.get_update_time()
                                  )]

        return GenericJSONResponse(data=marshal(account_dto, fields=AccountDTO.fields)).build()

    @staticmethod
    @api.route("/<uid>", methods=("DELETE",))
    def delete_account_by_uid(uid):
        AccountService.delete_account_by_uid(StringUtil.smart_trim("%s" % uid))

        account = []
        return GenericJSONResponse(data=marshal(account, fields=AccountDTO.fields)).build()

    @staticmethod
    @api.route("/", methods=("DELETE",))
    def delete_account():
        p_uid_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(p_uid_list) > 0:
            AccountService.delete_account(p_uid_list)

        accounts = AccountService.list_account(None, None, None, None, None, None)

        dto_list = []
        for account in accounts:
            dto_list.append(AccountDTO(username=account.get_username(),
                                       name=account.get_name(),
                                       group=account.get_group(),
                                       phone=account.get_phone(),
                                       email=account.get_email(),
                                       sex=account.get_sex(),
                                       arch_group=account.get_arch_group(),
                                       create_time=account.get_create_time(),
                                       update_time=account.get_update_time()))

        return GenericJSONResponse(data=marshal(dto_list, fields=AccountDTO.fields)).build()

    @staticmethod
    @api.route("/<uid>", methods=("PUT",))
    def update_account_by_uid(uid):
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "phone")
        p_group = RequestUtil.get_param_from_body_raw_json(request, "group")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "email")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "sex")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "arch_group")

        f_uid = StringUtil.smart_trim("%s" % uid)
        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        group = StringUtil.smart_trim(p_group)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)
        update_time = datetime.utcnow()

        AccountService.update_account(f_uid, name, group, phone, email, sex, arch_group, update_time)

        account = AccountService.get_account_by_uid(f_uid)
        account_dto = [AccountDTO(username=account.get_username(),
                                  name=account.get_name(),
                                  group=account.get_group(),
                                  phone=account.get_phone(),
                                  email=account.get_email(),
                                  sex=account.get_sex(),
                                  arch_group=account.get_arch_group(),
                                  create_time=account.get_create_time(),
                                  update_time=account.get_update_time()
                                  )]

        return GenericJSONResponse(data=marshal(account_dto, fields=AccountDTO.fields)).build()
