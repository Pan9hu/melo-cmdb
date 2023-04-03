import datetime
import json
import jwt
from util.date_encoder import DateEncoder


class JWTUtile:

    @staticmethod
    def generate_token(_id: str, login_time: datetime.datetime):
        """
        生成认证Token
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
        secret_key = "6d52e21d599841d0b8c690efa9748ce4"  # 密钥下面jwt-encode时需要
        try:
            payload = {
                'iss': 'melo',
                'exp': eval(json.dumps(datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=4),
                                       cls=DateEncoder)),
                'iat': eval(json.dumps(datetime.datetime.utcnow(),
                                       cls=DateEncoder)),
                'data': {  # 内容，一般存放该用户id和开始时间
                    'id': _id,
                    'login_time': eval(json.dumps(login_time,
                                                  cls=DateEncoder)),
                }
            }
            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            print(e)
