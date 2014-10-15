from java2python.lang import tokens
from java2python.lib import FS

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

typeSubs = {
    'char': 'chr',
    'DataInputStream': 'object',
    'EClientSocket': 'object',
}

def expressionCastHandler(expr, node):
    name = node.firstChildOfType(tokens.TYPE).firstChild()
    if name.type == tokens.QUALIFIED_TYPE_IDENT:
        name = name.firstChild()
    name = name.text
    if name == 'chr':
        expr.fs = name + '(' + FS.r + ')'
    else:
        expr.fs = FS.r
