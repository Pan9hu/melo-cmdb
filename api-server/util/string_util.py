class StringUtil:

    @staticmethod
    def smart_trim(s: str):
        if s is None:
            return None

        ss = s.strip()

        if len(ss) <= 0:
            return None

        return ss
