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

Listener = namedtuple('Listener', 'func options')


class Dispatcher(EWrapper):
    def __init__(self, dispatch):
        self.dispatch = dispatch

    def make(name, spec):
        def func(self, *args):
            self.dispatch(name, args)
        return func

    for name, value in messages.items():
        locals()[name] = make(name, value._fields)

    def error(self, *args):
        self.dispatch('error', (None,) * (3 - len(args)) + args)


class Connection(object):
    def __init__(self, host='localhost', port=7496, clientId=0):
        self.host, self.port, self.clientId = host, port, clientId
        self.client = EClientSocket(Dispatcher(self.dispatch))
        self.listeners = {}

    def connect(self):
        self.client.eConnect(self.host, self.port, self.clientId)
        return self.client.isConnected()

    def disconnect(self):
        if self.client.isConnected():
            self.client.eDisconnect()
            return True
        return False

    def dispatch(self, name, args):
        try:
            listeners = self.listeners[name]
        except KeyError:
            return
        msg = messages[name]._make(args)
        self._dispatch(name, msg, listeners)

    def _dispatch(self, name, msg, listeners):
        for listener in listeners:
            try:
                listener.func(msg)
            except:
                exceptions = listener.options.get('exceptions', 'raise')
                if exceptions == 'unregister':
                    self.unregister(listener.func, name)
                elif exceptions == 'raise':
                    raise
                elif exceptions == 'pass':
                    pass
                else:
                    assert False, exceptions

    @staticmethod
    def getName(arg):
        if not isinstance(arg, str):
            name = arg.__name__
        else:
            name = arg
        if name not in messages:
            raise ValueError(arg)
        return name

    def getListeners(self, arg):
        name = self.getName(arg)
        return [listener.func for listener in self.listeners.get(name, [])]

    def register(self, func, *args, **options):
        count = 0
        for arg in args:
            name = self.getName(arg)
            listeners = self.listeners.setdefault(name, [])
            for listener in listeners:
                if listener.func is func:
                    break
            else:
                listeners.append(Listener(func, options))
                count += 1
        return count > 0

    def unregister(self, func, *args):
        count = 0
        for arg in args:
            name = self.getName(arg)
            try:
                listeners = self.listeners[name]
            except KeyError:
                continue
            for listener in listeners:
                if listener.func is func:
                    listeners.remove(listener)
                    count += 1
                    break
        return count > 0

    def registerAll(self, func):
        return self.register(func, *messages.keys())

    def unregisterAll(self, func):
        return self.unregister(func, *messages.keys())

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
