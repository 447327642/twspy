from .overloading import overloaded


class classmethod(classmethod):
    def __getattr__(self, name):
        return getattr(self.__func__, name)
