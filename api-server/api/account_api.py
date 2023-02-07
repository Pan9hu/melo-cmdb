from flask import request, Blueprint
from datetime import datetime
from service.account_service import AccountService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AccountAPI:
    api = Blueprint("account", __name__, url_prefix="/account")

    @staticmethod
    @api.route("/<uid>", methods=("GET",))
    def get_account_by_id(uid):
        """
        根据工号，精确搜索
        :param uid:
        :return:
        """
        print("Get")
        print(uid)
        return {}

    @staticmethod
    @api.route("/", methods=("GET",))
    def list_account():
        """
        根据条件进行匹配
        :return:
        """
        p_name = RequestUtil.get_param(request, "name")
        p_phone = RequestUtil.get_param(request, "phone")
        p_email = RequestUtil.get_param(request, "email")
        p_sex = RequestUtil.get_param(request, "sex")
        p_arch_group = RequestUtil.get_param(request, "arch-group")

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
        p_uid = RequestUtil.get_param(request, "uid")
        p_name = RequestUtil.get_param(request, "name")
        p_phone = RequestUtil.get_param(request, "phone")
        p_email = RequestUtil.get_param(request, "email")
        p_sex = RequestUtil.get_param(request, "sex")
        p_arch_group = RequestUtil.get_param(request, "arch-group")

        uid = StringUtil.smart_trim(p_uid)
        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)
        create_time = datetime.now()
        update_time = datetime.now()

        AccountService.create_account(uid, name, phone, email, sex, arch_group, create_time,update_time)
        return {}
