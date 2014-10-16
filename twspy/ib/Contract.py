""" generated source for module Contract """
from __future__ import print_function
from ..lang.python import overloaded
from ..lang.java import Cloneable, Vector
from .Util import Util
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class Contract(Cloneable):
    """ generated source for class Contract """
    m_conId = int()
    m_symbol = None
    m_secType = None
    m_expiry = None
    m_strike = float()
    m_right = None
    m_multiplier = None
    m_exchange = None
    m_currency = None
    m_localSymbol = None
    m_tradingClass = None
    m_primaryExch = None

    #  pick a non-aggregate (ie not the SMART exchange) exchange that the contract trades on.  DO NOT SET TO SMART.
    m_includeExpired = bool()

    #  can not be set to true for orders.
    m_secIdType = None

    #  CUSIP;SEDOL;ISIN;RIC
    m_secId = None

    #  COMBOS
    m_comboLegsDescrip = None

    #  received in open order version 14 and up for all combos
    m_comboLegs = Vector()

    #  delta neutral
    m_underComp = None

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(Contract, self).__init__()
        self.m_conId = 0
        self.m_strike = 0
        self.m_includeExpired = False

    def clone(self):
        """ generated source for method clone """
        retval = super(Contract, self).clone()
        retval.m_comboLegs = retval.m_comboLegs.clone()
        return retval

    @__init__.register(object, int, str, str, str, float, str, str, str, str, str, str, Vector, str, bool, str, str)
    def __init___0(self, p_conId, p_symbol, p_secType, p_expiry, p_strike, p_right, p_multiplier, p_exchange, p_currency, p_localSymbol, p_tradingClass, p_comboLegs, p_primaryExch, p_includeExpired, p_secIdType, p_secId):
        """ generated source for method __init___0 """
        super(Contract, self).__init__()
        self.m_conId = p_conId
        self.m_symbol = p_symbol
        self.m_secType = p_secType
        self.m_expiry = p_expiry
        self.m_strike = p_strike
        self.m_right = p_right
        self.m_multiplier = p_multiplier
        self.m_exchange = p_exchange
        self.m_currency = p_currency
        self.m_includeExpired = p_includeExpired
        self.m_localSymbol = p_localSymbol
        self.m_tradingClass = p_tradingClass
        self.m_comboLegs = p_comboLegs
        self.m_primaryExch = p_primaryExch
        self.m_secIdType = p_secIdType
        self.m_secId = p_secId

    def equals(self, p_other):
        """ generated source for method equals """
        if self == p_other:
            return True
        if p_other == None or not (isinstance(p_other, (Contract, ))):
            return False
        l_theOther = p_other
        if self.m_conId != l_theOther.m_conId:
            return False
        if Util.StringCompare(self.m_secType, l_theOther.m_secType) != 0:
            return False
        if Util.StringCompare(self.m_symbol, l_theOther.m_symbol) != 0 or Util.StringCompare(self.m_exchange, l_theOther.m_exchange) != 0 or Util.StringCompare(self.m_primaryExch, l_theOther.m_primaryExch) != 0 or Util.StringCompare(self.m_currency, l_theOther.m_currency) != 0:
            return False
        if not Util.NormalizeString(self.m_secType) == "BOND":
            if self.m_strike != l_theOther.m_strike:
                return False
            if Util.StringCompare(self.m_expiry, l_theOther.m_expiry) != 0 or Util.StringCompare(self.m_right, l_theOther.m_right) != 0 or Util.StringCompare(self.m_multiplier, l_theOther.m_multiplier) != 0 or Util.StringCompare(self.m_localSymbol, l_theOther.m_localSymbol) != 0 or Util.StringCompare(self.m_tradingClass, l_theOther.m_tradingClass) != 0:
                return False
        if Util.StringCompare(self.m_secIdType, l_theOther.m_secIdType) != 0:
            return False
        if Util.StringCompare(self.m_secId, l_theOther.m_secId) != 0:
            return False
        #  compare combo legs
        if not Util.VectorEqualsUnordered(self.m_comboLegs, l_theOther.m_comboLegs):
            return False
        if self.m_underComp != l_theOther.m_underComp:
            if self.m_underComp == None or l_theOther.m_underComp == None:
                return False
            if not self.m_underComp == l_theOther.m_underComp:
                return False
        return True
