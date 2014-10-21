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

Listener = namedtuple('Listener', 'func args options')


class Dispatcher(EWrapper):
    def __init__(self, dispatch):
        self._dispatch = dispatch

    def make(name, spec):
        def func(self, *args):
            self._dispatch(name, args)
        return func

    for name, value in messages.items():
        locals()[name] = make(name, value._fields)

    del make, name, value

    def error(self, *args):
        self._dispatch('error', (None,) * (3 - len(args)) + args)


class Connection(object):
    def __init__(self, host='localhost', port=7496, clientId=0, **options):
        self.host, self.port, self.clientId = host, port, clientId
        self.client = EClientSocket(Dispatcher(self._dispatch))
        self.listeners = {}
        self.options = options

    def connect(self):
        self.client.eConnect(self.host, self.port, self.clientId)
        return self.client.isConnected()

    def disconnect(self):
        if self.client.isConnected():
            self.client.eDisconnect()
            return True
        return False

    def _dispatch(self, name, args):
        try:
            listeners = self.listeners[name]
        except KeyError:
            return
        msg = messages[name]._make(args)
        for listener in listeners:
            try:
                ret = listener.func(msg, *listener.args)
            except:
                try:
                    exceptions = listener.options['exceptions']
                except KeyError:
                    exceptions = self.options.get('exceptions', 'raise')
                if exceptions == 'unregister':
                    self.unregister(name, listener.func)
                elif exceptions == 'raise':
                    raise
                elif exceptions == 'pass':
                    pass
                else:
                    assert False, exceptions
            else:
                if ret is not None:
                    msg = ret

    @staticmethod
    def _getName(type_):
        if not isinstance(type_, str):
            name = type_.__name__
        else:
            name = type_
        if name not in messages:
            raise ValueError(type_)
        return name

    @classmethod
    def _getNames(cls, types):
        if isinstance(types, (str, type)):
            types = (types,)
        return [cls._getName(type_) for type_ in types]

    def getListeners(self, type_):
        name = self._getName(type_)
        return [listener.func for listener in self.listeners.get(name, [])]

    def listener(self, types, **options):
        def decorator(func):
            self.register(types, func, **options)
            return func
        return decorator

    def register(self, types, func, *args, **options):
        count = 0
        for name in self._getNames(types):
            listeners = self.listeners.setdefault(name, [])
            for listener in listeners:
                if listener.func is func:
                    break
            else:
                listeners.append(Listener(func, args, options))
                count += 1
        return count > 0

    def unregister(self, types, func):
        count = 0
        for name in self._getNames(types):
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
        return self.register(messages.keys(), func)

    def unregisterAll(self, func):
        return self.unregister(messages.keys(), func)

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
