from __future__ import print_function

import inspect
import sys
from collections import namedtuple

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
        if not self.client.isConnected():
            raise IOError

    def close(self):
        self.client.eDisconnect()

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

    def getListeners(self, name):
        if name not in messages:
            raise KeyError(name)
        return [listener.func for listener in self.listeners.get(name, [])]

    def listener(self, *names, **options):
        def decorator(func):
            for name in names:
                self.register(name, func, **options)
            return func
        return decorator

    def register(self, name, func, *args, **options):
        if name not in messages:
            raise KeyError(name)
        if not callable(func):
            raise TypeError(func)
        listeners = self.listeners.setdefault(name, [])
        for listener in listeners:
            if listener.func is func:
                raise ValueError(name, func)
        listeners.append(Listener(func, args, options))

    def unregister(self, name, func):
        if name not in messages:
            raise KeyError(name)
        if not callable(func):
            raise TypeError(func)
        listeners = self.listeners.get(name, [])
        for listener in listeners:
            if listener.func is func:
                return listeners.remove(listener)
        raise ValueError(name, func)

    def registerAll(self, func):
        for name in messages.keys():
            try:
                self.register(name, func)
            except ValueError:
                pass

    def unregisterAll(self, func):
        for name in messages.keys():
            try:
                self.unregister(name, func)
            except ValueError:
                pass

    def enableLogging(self, enable=True):
        if enable:
            self.registerAll(self.logMessage)
        else:
            self.unregisterAll(self.logMessage)

    @staticmethod
    def logMessage(msg):
        print(msg, file=sys.stderr)

    def __getattr__(self, name):
        return getattr(self.client, name)
