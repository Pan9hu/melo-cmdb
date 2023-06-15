from flask import Blueprint
from flask_restful import marshal, fields

from bean.dto.version_dto import VersionDTO
from core.response.generic_json_response import GenericJSONResponse


class VersionAPI:
    api = Blueprint("api", __name__, url_prefix="/api")

    @staticmethod
    @api.route("/version", methods=("GET",))
    def get_version():
        version_dto = VersionDTO(version="1.0")
        return GenericJSONResponse(data=marshal(version_dto, fields=VersionDTO.fields)).build()
