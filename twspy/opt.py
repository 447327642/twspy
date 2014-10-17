import traceback

from . import Connection, message, messages

class message(message):
    pass
for name, value in messages.items():
    setattr(message, name[0].upper() + name[1:], value)

class ibConnection(Connection):
    def dispatch(self, name, args):
        try:
            listeners = self.listeners[name]
        except KeyError:
            return
        msg = messages[name]._make(args)
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
            name = arg[0].lower() + arg[1:]
        assert name in messages
        return name
