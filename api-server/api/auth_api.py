import base64
from datetime import datetime

from flask import request, Blueprint
from service.auth_service import AuthService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AuthAPI:
    api = Blueprint("auth", __name__, url_prefix="/auth")

    @staticmethod
    @api.route("/login", methods=('POST',))
    def login():
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        p_password_b64 = RequestUtil.get_param_from_body_raw_json(request, "password")
        # 从body中获取账号和密码
        p_password = base64.b64decode(p_password_b64).decode("UTF-8")
        # base64解码
        username = StringUtil.smart_trim(p_username)
        password = StringUtil.smart_trim(p_password)
        login_time = datetime.utcnow()
        # 判断账号密码是否为空
        auth_token = AuthService.login(username, password, login_time)
        print(auth_token)

        return {}

    @staticmethod
    @api.route("/refresh", methods=('POST',))
    def refresh():
        p_refresh = RequestUtil.get_param_from_body_raw_json(request, " refresh")
        refresh = StringUtil.smart_trim(p_refresh)
        # 刷新过期的token
        AuthService.refresh(refresh)
        return {}

    @staticmethod
    @api.route("/reset-password", methods=('POST',))
    def reset_password():
        """
        忘记密码， 重置密码， 向可能的通知类型发送验证码(邮箱, 手机号码）
        :return:
        """
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        username = StringUtil.smart_trim(p_username)

        AuthService.reset_password(username)

        return {}
