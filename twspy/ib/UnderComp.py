""" generated source for module UnderComp """
from __future__ import print_function
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class UnderComp(object):
    """ generated source for class UnderComp """
    m_conId = int()
    m_delta = float()
    m_price = float()

    def __init__(self):
        """ generated source for method __init__ """
        self.m_conId = 0
        self.m_delta = 0
        self.m_price = 0

    def equals(self, p_other):
        """ generated source for method equals """
        if self == p_other:
            return True
        if p_other == None or not (isinstance(p_other, (UnderComp, ))):
            return False
        l_theOther = p_other
        if self.m_conId != l_theOther.m_conId:
            return False
        if self.m_delta != l_theOther.m_delta:
            return False
        if self.m_price != l_theOther.m_price:
            return False
        return True
