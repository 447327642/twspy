modulePrologueHandlers = [
    'from ..lang.java import Date, DateFormat, Double',
    'from .AnyWrapperMsgGenerator import AnyWrapperMsgGenerator',
    'from .EClientSocket import EClientSocket',
    'from .MarketDataType import MarketDataType',
    'from .TickType import TickType',
    'from .Util import Util',
]

moduleOutputSubs = [
    ('(?<!def)([ \(])(%s\()' % name, r'\1cls.\2') for name in [
        'contractMsg',
        'contractDetailsMsg',
        'contractDetailsSecIdList',
    ]
]
