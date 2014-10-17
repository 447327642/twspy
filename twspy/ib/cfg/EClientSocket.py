modulePrologueHandlers = [
    'from ..lang.python import long, overloaded',
    'from ..lang.java import DataInputStream, DataOutputStream, Double, Integer, Socket, StringBuilder',
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
        'startAPI',
    ]
] + [
    (r'EOL = \[0\]', r'EOL = chr(0).encode()'),
    (r'str_\.getBytes\(\)', r'str_.encode()'),

    (r'print\("Server Version:" \+ self\.m_serverVersion\)',
     r'print("Server Version:" + str(self.m_serverVersion))',),
]

typeSubs = {'char': 'chr'}
