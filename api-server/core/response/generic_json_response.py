class GenericJSONResponse:
    """
    通过 Json 对象
    调用 GenericJSONResponse 对象的 build 方法可以返回 JSON 对象
    """

    def __init__(self, data: object | None, message: str = "完成", code: str = "10000"):
        self.data = data
        self.message = message
        self.code = code

    def build(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }
