from flask import request, Blueprint
from datetime import datetime
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
        AccountService.get_account_by_uid(StringUtil.smart_trim(uid))

        return {}

    @staticmethod
    @api.route("/", methods=("GET",))
    def list_account():
        """
        根据条件进行匹配
        :return:
        """
        p_name = RequestUtil.get_param_from_url_query_param(request, "name")
        p_phone = RequestUtil.get_param_from_url_query_param(request, "phone")
        p_email = RequestUtil.get_param_from_url_query_param(request, "email")
        p_sex = RequestUtil.get_param_from_url_query_param(request, "sex")
        p_arch_group = RequestUtil.get_param_from_url_query_param(request, "arch-group")

        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)

        AccountService.list_account(name, phone, email, sex, arch_group)

        return {}

    @staticmethod
    @api.route("/", methods=("POST",))
    def create_account():
        p_uid = RequestUtil.get_param_from_body_raw_json(request, "uid")
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "phone")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "email")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "sex")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "arch-group")

        uid = StringUtil.smart_trim(p_uid)
        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)
        create_time = datetime.utcnow()
        update_time = datetime.utcnow()

        AccountService.create_account(uid, name, phone, email, sex, arch_group, create_time, update_time)
        return {}

    @staticmethod
    @api.route("/<uid>", methods=("DELETE",))
    def delete_account_by_uid(uid):
        AccountService.delete_account_by_uid(StringUtil.smart_trim(uid))
        pass

    @staticmethod
    @api.route("/", methods=("DELETE",))
    def delete_account():
        p_uid_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(p_uid_list) > 0:
            AccountService.delete_account(p_uid_list)

        return {}

    @staticmethod
    @api.route("/<uid>", methods=("PUT",))
    def update_account_by_uid(uid):
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "phone")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "email")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "sex")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "arch-group")

        uid = StringUtil.smart_trim(uid)
        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)

        AccountService.update_account(uid, name, phone, email, sex, arch_group)

        return {}
