import base64

from flask import request, Blueprint

from service.auth_service import AuthService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AuthAPI:
    api = Blueprint("auth", __name__, url_prefix="/auth")

    @staticmethod
    @api.route("/login", methods=('POST',))
    def login():
        p_username = RequestUtil.get_param(request, "username")
        p_password_b64 = RequestUtil.get_param(request, "password")

        p_password = base64.b64decode(p_password_b64).decode("UTF-8")

        username = StringUtil.smart_trim(p_username)
        password = StringUtil.smart_trim(p_password)

        AuthService.login(username, password)

    @staticmethod
    @api.route("/refresh", methods=('POST',))
    def refresh():
        p_refresh = RequestUtil.get_param(request, " refresh")
        refresh = StringUtil.smart_trim(p_refresh)

        AuthService.refresh(refresh)
        return {}

    @staticmethod
    @api.route("/reset-password", methods=('POST',))
    def reset_password():
        """
        忘记密码， 重置密码， 向可能的通知类型发送验证码(邮箱, 手机号码）
        :return:
        """

        p_username = RequestUtil.get_param(request, "username")
        username = StringUtil.smart_trim(p_username)

        AuthService.reset_password(username)

        return {}
