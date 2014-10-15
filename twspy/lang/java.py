import socket
import sys
import threading

from .python import long


class Boolean(object):
    pass


class Double(object):
    MAX_VALUE = sys.float_info.max
    parseDouble = float


class Integer(object):
    MAX_VALUE = sys.maxsize
    parseInt = int


class Long(object):
    parseLong = long


class Cloneable(object):
    pass


class Date(object):
    pass


class DateFormat(object):
    pass


class DataInputStream(object):
    def __init__(self, in_):
        self.in_ = in_

    def readByte(self):
        return ord(self.in_.recv(1))

    def close(self):
        pass


class DataOutputStream(object):
    def __init__(self, out):
        self.out = out

    def write(self, b):
        self.out.send(b)

    def close(self):
        self.out.shutdown(socket.SHUT_RDWR)
        self.out.close()


class Socket(socket.socket):
    def __init__(self, host, port):
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

    getInputStream = getOutputStream = lambda self: self


class StringBuffer(list):
    def __str__(self):
        return ''.join(self)


class StringBuilder(list):
    def __init__(self, capacity):
        pass

    def __str__(self):
        return ''.join(self)


class Vector(list):
    add = list.append
    get = list.__getitem__


class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    isInterrupted = lambda self: False
