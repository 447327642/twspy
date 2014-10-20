from . import Connection, messages


class Message(object):
    __slots__ = ()

    def __init__(self, **kwargs):
        for slot in self.__slots__:
            setattr(self, slot, kwargs.pop(slot, None))
        assert not kwargs

    def __repr__(self):
        items = ", ".join("%s=%s" % (slot, getattr(self, slot))
                          for slot in self.__slots__)
        if items:
            items = ' ' + items
        return "<%s%s>" % (self.typeName, items)

upper = lambda name: name[0].upper() + name[1:]
messages = {name:
            type(upper(name), (Message,),
                 {'__slots__': value._fields, 'typeName': name})
            for name, value in messages.items()}

message = type('message', (object,), messages)


class ibConnection(Connection):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('exceptions', 'pass')
        Connection.__init__(self, *args, **kwargs)

    def dispatch(self, name, args):
        try:
            listeners = self.listeners[upper(name)]
        except KeyError:
            return
        msg = messages[name]()
        for i, arg in enumerate(msg.__slots__):
            setattr(msg, arg, args[i])
        self._dispatch(name, msg, listeners)

    @staticmethod
    def getName(arg):
        if not isinstance(arg, str):
            name = arg.__name__
        else:
            name = arg
        return name

    def registerAll(self, func):
        return self.register(func, *(upper(name) for name in messages.keys()))

    def unregisterAll(self, func):
        return self.unregister(func, *(upper(name) for name in messages.keys()))
