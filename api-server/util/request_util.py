class RequestUtil:

    @staticmethod
    def get_param_from_body_raw_json(request, name):
        """
        获取body中的内容
        判断name字段参数的内容是否为空，如为空抛出异常
        """
        request_content = request.json

        value = None

        try:
            value = request_content[name]
        except KeyError:
            pass
        return value

    @staticmethod
    def get_param_from_body_raw_json_as_list(request):
        """
        判断请求体是否为list类型，如果是则返回json形式数据，如果不是则返回空字典
        """
        if type(request.json) is list:
            return request.json

        return []

    @staticmethod
    def get_param_from_url_query_param(request, name):
        """"
        获取url中的参数来查找数据
        """
        request_value = request.values

        value = request_value.get(name)

        return value

    @staticmethod
    def get_param_from_headers(request, name):
        """"
        获取headers中的参数来查找数据
        """
        request_headers = request.headers

        value = None

        try:
            value = request_headers[name]
        except KeyError:
            pass

        return value
