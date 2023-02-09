class GenericJSONResponse:
    """
    通过 Json 对象
    调用 GenericJSONResponse 对象的 build 方法可以返回 JSON 对象
    """

    def __init__(self, data: object, message: str = None, code: str = "10000"):
        self.data = data
        self.message = message
        self.code = code

    def build(self):
        result = None

        if hasattr(self.data, "to_json"):
            if callable(self.data.to_json):
                result = self.data.to_json()
        else:
            if type(self.data).__name__ in ["str", "dict", "list", "tuple"]:
                result = self.data

        return {
            "code": self.code,
            "message": self.message,
            "data": result
        }
