import random


class RandomUtil:

    @staticmethod
    def get_random() -> str:
        code = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            code += ch
        return code
