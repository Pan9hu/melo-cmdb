import datetime
import json
import jwt
from util.date_encoder import DateEncoder


class JWTUtile:
    __secret_key = "6d52e21d599841d0b8c690efa9748ce4"  # 密钥下面jwt-encode和jwt-decode时需要

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
            exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=0, seconds=10)
        else:
            exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=0, seconds=60)

        try:
            headers = {'typ': 'jwt', 'alg': 'HS256'}
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
                JWTUtile.__secret_key,
                'HS256',
                headers,
            )
        except Exception as e:
            return e

    @staticmethod
    def verify_token(token) -> str:
        try:
            verified_payload = jwt.decode(token, JWTUtile.__secret_key, algorithms='HS256')
            print(verified_payload)
            if 'data' in verified_payload and 'id' in verified_payload['data']:
                return verified_payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'
