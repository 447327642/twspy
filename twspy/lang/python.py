import sys

from .overloading import overloaded  # noqa

if sys.version_info[0] >= 3:
    cmp = lambda x, y: (x > y) - (x < y)
    long = int
else:
    from __builtin__ import cmp, long  # noqa


class classmethod(classmethod):
    def __getattr__(self, name):
        return getattr(self.__func__, name)
