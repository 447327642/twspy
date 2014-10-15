import sys


class Boolean(object):
    pass


class Double(object):
    MAX_VALUE = sys.float_info.max


class Integer(object):
    MAX_VALUE = sys.maxsize


class Long(object):
    pass


class Cloneable(object):
    pass


class Date(object):
    pass


class DateFormat(object):
    pass


class DataInputStream(object):
    pass


class DataOutputStream(object):
    pass


class Socket(object):
    pass


class StringBuffer(object):
    pass


class StringBuilder(list):
    def __init__(self, capacity):
        pass

    def __str__(self):
        return ''.join(self)


class Vector(object):
    pass


class Thread(object):
    pass
