from flask_restful import fields


class AuthDTO:
    fields = {
        "access_token": fields.String,
        "refresh_token": fields.String,
        "username": fields.String,
        "auth_method": fields.String,
        "sms_code": fields.String,
    }
