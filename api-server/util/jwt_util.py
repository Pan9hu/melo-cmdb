import datetime
import json
import jwt
from util.date_encoder import DateEncoder


class JWTUtil:
    __secret_key = "6d52e21d599841d0b8c690efa9748ce4"  # 密钥下面jwt-encode和jwt-decode时需要
    headers = {'typ': 'jwt', 'alg': 'HS256'}

    @staticmethod
    def generate_token(_id: str, login_time: datetime.datetime, long: bool) -> str | Exception:
        """
        生成认证Token
        :param long: bool
        :param _id: int
        :param login_time: datetime
        :return: string
        """
        # 签发人(issuer)
        # 过期时间(expiration time)
        # 主题(subject)
        # 受众(audience)
        # 生效时间(Not Before)
        # 签发时间(Issued At)
        # 编号(JWT ID)
        if long:
            exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=0, hours=2)
        else:
            exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=30)

        try:
            payload = {
                'iss': 'melo',
                'exp': exp,
                'iat': datetime.datetime.now(tz=datetime.timezone.utc),
                'data': {  # 内容，一般存放该用户id和开始时间
                    'id': _id,
                    'login_time': int(eval(json.dumps(login_time,
                                                      cls=DateEncoder))),
                }
            }
            return jwt.encode(
                payload,
                JWTUtil.__secret_key,
                'HS256',
                JWTUtil.headers,
            )
        except Exception as e:
            return e

    @staticmethod
    def verify_token(token) -> str:
        try:
            verified_payload = jwt.decode(token, JWTUtil.__secret_key, algorithms='HS256')
            if 'data' in verified_payload and 'id' in verified_payload['data']:
                # TODO 验证username是否与token中的username一致
                return verified_payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    @staticmethod
    def refresh_token(token):
        try:
            verified_payload = jwt.decode(token, JWTUtil.__secret_key, algorithms='HS256',
                                          options={"verify_exp": False})
            if 'data' in verified_payload and 'id' in verified_payload['data']:
                verified_payload["exp"] = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=0,
                                                                                                               hours=2)
                verified_payload["iat"] = datetime.datetime.now(tz=datetime.timezone.utc)
                return jwt.encode(
                    verified_payload,
                    JWTUtil.__secret_key,
                    'HS256',
                    JWTUtil.headers,
                )
            else:
                raise jwt.InvalidTokenError
        except jwt.InvalidTokenError:
            return '无效Token'
