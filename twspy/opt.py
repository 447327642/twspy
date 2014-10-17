import traceback

from . import Connection, messages

upper = lambda name: name[0].upper() + name[1:]
messages = {name: type(upper(name), (object,), {'__slots__': value._fields})
            for name, value in messages.items()}

message = type('message', (object,), messages)


class ibConnection(Connection):
    def dispatch(self, name, args):
        try:
            listeners = self.listeners[upper(name)]
        except KeyError:
            return
        msg = messages[name]()
        for i, arg in enumerate(msg.__slots__):
            setattr(msg, arg, args[i])
        for listener in listeners:
            try:
                listener(msg)
            except:
                traceback.print_exc()

    @staticmethod
    def getName(arg):
        if not isinstance(arg, str):
            name = arg.__name__
        else:
            name = arg
        return name

    def registerAll(self, listener):
        return self.register(listener, *(upper(name) for name in messages.keys()))

    def unregisterAll(self, listener):
        return self.unregister(listener, *(upper(name) for name in messages.keys()))