from __future__ import print_function

import inspect
import sys
import traceback
from collections import namedtuple

from twspy.ib.EClientSocket import EClientSocket
from twspy.ib.EWrapper import EWrapper

sentinel = object()

functions = dict((name, inspect.getargspec(func).args[1:])
                 for name, func in inspect.getmembers(EWrapper, callable)
                 if not name.startswith('error') and not name.startswith('_'))
functions['error'] = ['id', 'errorCode', 'errorMsg']

messages = dict((name, namedtuple(name, args))
                for name, args in functions.items())


class Connection(object):
    Listener = namedtuple('Listener', 'func args options')

    def __init__(self, host='localhost', port=7496, clientId=0, **options):
        self.host, self.port, self.clientId = host, port, clientId
        self.client = EClientSocket(Dispatcher(self))
        self.listeners = {}
        self.options = options

    def connect(self):
        self.client.eConnect(self.host, self.port, self.clientId)
        if not self.client.isConnected():
            raise IOError

    def close(self):
        self.client.eDisconnect()

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
        listeners.append(self.Listener(func, args, options))

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

    def getListeners(self, name):
        if name not in messages:
            raise KeyError(name)
        return [listener.func for listener in self.listeners.get(name, [])]

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


class Dispatcher(EWrapper):
    def __init__(self, con):
        self.con = con

    def make(name):
        def func(self, *args):
            self._dispatch(name, args)
        return func

    for name in messages:
        locals()[name] = make(name)

    del make, name

    def error(self, *args):
        self._dispatch('error', (None,) * (3 - len(args)) + args)

    error_0 = error_1 = None

    def _dispatch(self, name, args):
        try:
            listeners = self.con.listeners[name]
        except KeyError:
            return
        msg = messages[name]._make(args)
        for listener in listeners:
            try:
                ret = listener.func(msg, *listener.args)
            except Exception:
                traceback.print_exc()
                exceptions = listener.options.get('exceptions', sentinel)
                if exceptions is sentinel:
                    exceptions = self.con.options.get('exceptions', 'raise')
                if exceptions == 'unregister':
                    self.con.unregister(name, listener.func)
                elif exceptions == 'raise':
                    raise
                elif exceptions == 'pass':
                    pass
                else:
                    assert False, exceptions
            else:
                if ret is not None:
                    msg = ret
