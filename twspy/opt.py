from . import Connection, message, messages

class message(message):
    pass
for name, value in messages.items():
    setattr(message, name[0].upper() + name[1:], value)

class ibConnection(Connection):
    @staticmethod
    def getName(arg):
        if not isinstance(arg, str):
            name = arg.__name__
        else:
            name = arg[0].lower() + arg[1:]
        assert name in messages
        return name
