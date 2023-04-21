from flask_restful import marshal

from bean.dto.auth_dto import AuthDTO
from core.response.generic_json_response import GenericJSONResponse
from util.jwt_util import JWTUtil
from util.string_util import StringUtil


class TokenHandler:

    @staticmethod
    def token_handler(token_dict: str):
        e_token = eval(token_dict)
        p_access_token = e_token["access"]
        p_refresh_token = e_token["refresh"]
        access_token = StringUtil.smart_trim(p_access_token)
        refresh_token = StringUtil.smart_trim(p_refresh_token)
        result_access_token = JWTUtil.verify_token(access_token)
        result_refresh_token = JWTUtil.verify_token(refresh_token)
        if result_access_token == 'Token过期':
            if result_refresh_token == 'Token过期':
                return GenericJSONResponse(data=marshal({"access_token": result_refresh_token}, fields=AuthDTO.fields),
                                           message="RefreshToken过期, 重新登录", code="20000").build()
            elif result_refresh_token == '无效Token':
                return GenericJSONResponse(data=marshal({"access_token": result_refresh_token}, fields=AuthDTO.fields),
                                           message="RefreshToken失效, 重新登录", code="30000").build()
            return GenericJSONResponse(data=marshal({"access_token": result_access_token}, fields=AuthDTO.fields),
                                       message="AccessToken过期, 重新获取", code="15000").build()
        elif result_access_token == '无效Token':
            if result_refresh_token == 'Token过期':
                return GenericJSONResponse(data=marshal({"access_token": result_refresh_token}, fields=AuthDTO.fields),
                                           message="RefreshToken过期, 重新登录", code="20000").build()
            elif result_refresh_token == '无效Token':
                return GenericJSONResponse(data=marshal({"access_token": result_refresh_token}, fields=AuthDTO.fields),
                                           message="RefreshToken失效, 重新登录", code="30000").build()
            return GenericJSONResponse(data=marshal({"access_token": result_access_token}, fields=AuthDTO.fields),
                                       message="AccessToken失效, 重新获取", code="15000").build()
