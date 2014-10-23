""" generated source for module ComboLeg """
from __future__ import print_function
from ._lang.python import overloaded
from .Util import Util
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class ComboLeg(object):
    """ generated source for class ComboLeg """
    SAME = 0

    #  open/close leg value is same as combo
    OPEN = 1
    CLOSE = 2
    UNKNOWN = 3
    m_conId = int()
    m_ratio = int()
    m_action = None

    #  BUY/SELL/SSHORT/SSHORTX
    m_exchange = None
    m_openClose = int()

    #  for stock legs when doing short sale
    m_shortSaleSlot = int()

    #  1 = clearing broker, 2 = third party
    m_designatedLocation = None
    m_exemptCode = int()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.__init__(0, 0, None, None, 0, 0, None, -1)#  conId  ratio  action  exchange  openClose  shortSaleSlot  designatedLocation exemptCode 

    @__init__.register(object, int, int, str, str, int)
    def __init___0(self, p_conId, p_ratio, p_action, p_exchange, p_openClose):
        """ generated source for method __init___0 """
        self.__init__(p_conId, p_ratio, p_action, p_exchange, p_openClose, 0, None, -1)#  shortSaleSlot  designatedLocation exemptCode 

    @__init__.register(object, int, int, str, str, int, int, str)
    def __init___1(self, p_conId, p_ratio, p_action, p_exchange, p_openClose, p_shortSaleSlot, p_designatedLocation):
        """ generated source for method __init___1 """
        self.__init__(p_conId, p_ratio, p_action, p_exchange, p_openClose, p_shortSaleSlot, p_designatedLocation, -1)#  exemptCode 

    @__init__.register(object, int, int, str, str, int, int, str, int)
    def __init___2(self, p_conId, p_ratio, p_action, p_exchange, p_openClose, p_shortSaleSlot, p_designatedLocation, p_exemptCode):
        """ generated source for method __init___2 """
        self.m_conId = p_conId
        self.m_ratio = p_ratio
        self.m_action = p_action
        self.m_exchange = p_exchange
        self.m_openClose = p_openClose
        self.m_shortSaleSlot = p_shortSaleSlot
        self.m_designatedLocation = p_designatedLocation
        self.m_exemptCode = p_exemptCode

    def __eq__(self, p_other):
        """ generated source for method equals """
        if self is p_other:
            return True
        elif p_other is None:
            return False
        l_theOther = p_other
        if self.m_conId != l_theOther.m_conId or self.m_ratio != l_theOther.m_ratio or self.m_openClose != l_theOther.m_openClose or self.m_shortSaleSlot != l_theOther.m_shortSaleSlot or self.m_exemptCode != l_theOther.m_exemptCode:
            return False
        if Util.StringCompareIgnCase(self.m_action, l_theOther.m_action) != 0 or Util.StringCompareIgnCase(self.m_exchange, l_theOther.m_exchange) != 0 or Util.StringCompareIgnCase(self.m_designatedLocation, l_theOther.m_designatedLocation) != 0:
            return False
        return True

