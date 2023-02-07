class RequestUtil:

    @staticmethod
    def get_param(request, name):
        request_content = request.json

        value = None

        try:
            value = request_content[name]
        except KeyError:
            pass
        return value

    @staticmethod
    def get_param_from_url_query_param(request, name):
        request_value = request.values
        value = request_value.get(name)

        return value
