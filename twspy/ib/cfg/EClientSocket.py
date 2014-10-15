modulePrologueHandlers = [
    'from ..lang.python import overloaded',
    'from ..lang.java import DataInputStream, DataOutputStream, Double, Integer, Socket',
    'from .Builder import Builder',
    'from .EClientErrors import EClientErrors',
    'from .EReader import EReader',
    'from .Util import Util',
]

moduleOutputSubs = [
    ('(?<!def)([ \(])(%s\()' % name, r'\1self.\2') for name in [
        'checkConnected',
        'close',
        'connectionError',
        'error',
        'eDisconnect',
        'IsEmpty',
        'isNull',
        'notConnected',
        'send',
        'sendEOL',
        'sendMax',
    ]
]
