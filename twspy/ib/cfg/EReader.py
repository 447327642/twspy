modulePrologueHandlers = [
    'from ..lang.python import overloaded',
    'from ..lang.java import Boolean, Double, Integer, Long, StringBuffer, Thread, Vector',
    'from .ComboLeg import ComboLeg',
    'from .CommissionReport import CommissionReport',
    'from .Contract import Contract',
    'from .ContractDetails import ContractDetails',
    'from .EClientErrors import EClientErrors',
    'from .Execution import Execution',
    'from .Order import Order',
    'from .OrderComboLeg import OrderComboLeg',
    'from .OrderState import OrderState',
    'from .TagValue import TagValue',
    'from .TickType import TickType',
    'from .UnderComp import UnderComp',
    'from .Util import Util',
]

moduleOutputSubs = [
    ('(?<!def)([ \(])(%s\()' % name, r'\1self.\2') for name in [
        'isInterrupted',
        'processMsg',
        'readBoolFromInt',
        'readDouble',
        'readDoubleMax',
        'readInt',
        'readIntMax',
        'readLong',
        'readStr',
        'setName',
    ]
]

typeSubs = {'EClientSocket': 'object', 'DataInputStream': 'object'}
