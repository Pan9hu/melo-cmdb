import base64
import datetime

from flask_restful import marshal
from bean.dto.auth_dto import AuthDTO
from core.response.generic_json_response import GenericJSONResponse
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
        login_time = datetime.datetime.now(tz=datetime.timezone.utc)
        # 判断账号密码是否为空
        access_token, refresh_token, code = AuthService.login(username, password, login_time)
        if code == "20000":
            return GenericJSONResponse(
                data=marshal({"access_token": access_token, "refresh_token": refresh_token, "username": username},
                             fields=AuthDTO.fields),
                message="用户不存在", code=code).build()
        elif code == "30000":
            return GenericJSONResponse(
                data=marshal({"access_token": access_token, "refresh_token": refresh_token, "username": username},
                             fields=AuthDTO.fields),
                message="密码错误", code=code).build()
        elif code == "40000":
            return GenericJSONResponse(
                data=marshal({"access_token": access_token, "refresh_token": refresh_token, "username": username},
                             fields=AuthDTO.fields),
                message="获取Token失败", code=code).build()
        else:
            return GenericJSONResponse(
                data=marshal({"access_token": access_token, "refresh_token": refresh_token, "username": username},
                             fields=AuthDTO.fields)).build()

    @staticmethod
    @api.route("/refresh", methods=('POST',))
    def refresh():
        p_refresh = RequestUtil.get_param_from_body_raw_json(request, "refresh")
        refresh = StringUtil.smart_trim(p_refresh)
        # 刷新过期的token
        access_token = AuthService.refresh(refresh)
        if access_token == "无效Token":
            return GenericJSONResponse(
                data=marshal({"access_token": access_token}, fields=AuthDTO.fields), message="无效的Token",
                code="20000").build()
        else:
            return GenericJSONResponse(
                data=marshal({"access_token": access_token}, fields=AuthDTO.fields)).build()

    @staticmethod
    @api.route("/security-code", methods=('POST',))
    def security_code():
        """
        忘记密码， 重置密码， 向可能的通知类型发送验证码(邮箱, 手机号码）
        :return:
        """
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        p_auth_method = RequestUtil.get_param_from_body_raw_json(request, "auth_method")
        # 获取用户名和验证方式
        username = StringUtil.smart_trim(p_username)
        auth_method = StringUtil.smart_trim(p_auth_method)
        expired_time = datetime.datetime.utcnow()
        # 发送验证码
        mes = AuthService.security_code(username, auth_method, expired_time)
        if mes == "OK":
            return GenericJSONResponse(data=marshal({"username": username}, fields=AuthDTO.fields)).build()

    @staticmethod
    @api.route("/verify_code", methods=('POST',))
    def verify_code():
        """
        验证用户输入的验证码，从定时的数据中核对验证码。
        :return:
        """
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        p_auth_method = RequestUtil.get_param_from_body_raw_json(request, "auth_method")
        p_code_b64 = RequestUtil.get_param_from_body_raw_json(request, "code")
        # 从body中获取账号和验证码
        p_code = base64.b64decode(p_code_b64).decode("UTF-8")

        # 获取用户名、验证方式和验证码
        username = StringUtil.smart_trim(p_username)
        auth_method = StringUtil.smart_trim(p_auth_method)
        code = StringUtil.smart_trim(p_code)

        result = AuthService.verify_code(username, auth_method, code)
        if result == "20000":
            return GenericJSONResponse(
                data=marshal({"username": username, "auth_method": auth_method}, fields=AuthDTO.fields),
                message="验证码已过期", code=result).build()
        elif result == "40000":
            return GenericJSONResponse(
                data=marshal({"username": username, "auth_method": auth_method}, fields=AuthDTO.fields),
                message="输入的验证码有误", code=result).build()
        else:
            return GenericJSONResponse(
                data=marshal({"username": username, "auth_method": auth_method}, fields=AuthDTO.fields)).build()

    @staticmethod
    @api.route("/reset-password", methods=('POST',))
    def reset_password():
        """
        忘记密码， 重置密码。
        :return:
        """
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        p_password_b64 = RequestUtil.get_param_from_body_raw_json(request, "password")
        # 从body中获取账号和密码
        p_password = base64.b64decode(p_password_b64).decode("UTF-8")
        # base64解码
        username = StringUtil.smart_trim(p_username)
        password = StringUtil.smart_trim(p_password)
        update_time = datetime.datetime.utcnow()

        result = AuthService.reset_password(username, password, update_time)

        if result == "50000":
            return GenericJSONResponse(
                data=marshal({"username": username}, fields=AuthDTO.fields),
                message="出现了无法预知的错误", code=result).build()
        elif result == "30000":
            return GenericJSONResponse(
                data=marshal({"username": username}, fields=AuthDTO.fields),
                message="出现了密码幂等性问题", code=result).build()
        elif result == "20000":
            return GenericJSONResponse(
                data=marshal({"username": username}, fields=AuthDTO.fields),
                message="修改失败, 密码不存在", code=result).build()
        else:
            return GenericJSONResponse(
                data=marshal({"username": username}, fields=AuthDTO.fields)).build()
