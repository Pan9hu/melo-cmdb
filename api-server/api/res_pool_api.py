from flask import Blueprint

from service.res_pool_service import ResPoolService
from util.string_util import StringUtil


class ResPoolAPI:
    api = Blueprint("res_pool", __name__, url_prefix="/res-pool")


    @staticmethod
    @api.route("/<name>", methods="GET")
    def get_res_pool_by_name(name):
        ResPoolService.get_res_pool_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @api.route("/",methods="GET")
    def list_res_pool():
    p_usage = RequestUtil.get_param_from_url_query_param(request,"usage")
