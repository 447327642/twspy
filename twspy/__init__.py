from __future__ import print_function
from collections import namedtuple
import inspect
import sys

from twspy.ib.EClientSocket import EClientSocket
from twspy.ib.EWrapper import EWrapper

functions = {}
predicate = inspect.ismethod if sys.version_info[0] < 3 else inspect.isfunction
for name, func in inspect.getmembers(EWrapper, predicate):
    functions[name] = inspect.getargspec(func).args[1:]
functions['error'] = ['id', 'errorCode', 'errorMsg']

messages = {}
for name, args in functions.items():
    messages[name] = namedtuple(name, args)

message = type('message', (object,), messages)


class Dispatcher(EWrapper):
    def __init__(self, dispatch):
        self.dispatch = dispatch

    def make(name, spec):
        def func(self, *args):
            self.dispatch(name, args)
        return func

    for name, value in messages.items():
        locals()[name] = make(name, value._fields)


class Connection(object):
    def __init__(self, host='localhost', port=7496, clientId=0):
        self.host, self.port, self.clientId = host, port, clientId
        self.client = None
        self.listeners = {}

    def connect(self):
        client = self.client = EClientSocket(Dispatcher(self.dispatch))
        client.eConnect(self.host, self.port, self.clientId)
        return client.isConnected()

    def disconnect(self):
        client = self.client
        if client and client.isConnected():
            client.eDisconnect()
            return not client.isConnected()
        return False

    def dispatch(self, name, args):
        try:
            listeners = self.listeners[name]
        except KeyError:
            return
        msg = messages[name]._make(args)
        for listener in listeners:
            listener(msg)

    def register(self, listener, *args):
        count = 0
        for arg in args:
            if not isinstance(arg, str):
                name = arg.__name__
            else:
                name = arg
            assert name in messages
            listeners = self.listeners.setdefault(name, [])
            if listener not in listeners:
                listeners.append(listener)
                count += 1
        return count > 0

    def unregister(self, listener, *args):
        count = 0
        for arg in args:
            if not isinstance(arg, str):
                name = arg.__name__
            else:
                name = arg
            assert name in messages
            try:
                self.listeners[name].remove(listener)
            except (KeyError, ValueError):
                pass
            else:
                count += 1
        return count > 0

    def registerAll(self, listener):
        return self.register(listener, *messages.keys())

    def unregisterAll(self, listener):
        return self.unregister(listener, *messages.keys())

    def enableLogging(self, enable=True):
        if enable:
            self.registerAll(self.logMessage)
        else:
            self.unregisterAll(self.logMessage)
        return enable

    @staticmethod
    def logMessage(msg):
        print(msg, file=sys.stderr)

    def __getattr__(self, name):
        return getattr(self.client, name)
