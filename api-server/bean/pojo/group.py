class Group:

    def __init__(self, name, usage=None, create_time=None, update_time=None):
        self.__name = name
        self.__usage = usage
        self.__create_time = create_time
        self.__update_time = update_time

    def get_name(self):
        return self.__name

    def get_usage(self):
        return self.__usage

    def get_create_time(self):
        return self.__create_time

    def get_update_time(self):
        return self.__update_time

    def set_create_time(self, ctime):
        self.__create_time = ctime

    def set_update_time(self, utime):
        self.__update_time = utime
