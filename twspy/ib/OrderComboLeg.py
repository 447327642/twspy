""" generated source for module OrderComboLeg """
from __future__ import print_function
from ..lang.python import overloaded
from ..lang.java import Double
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class OrderComboLeg(object):
    """ generated source for class OrderComboLeg """
    m_price = float()

    #  price per leg
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.m_price = Double.MAX_VALUE

    @__init__.register(object, float)
    def __init___0(self, p_price):
        """ generated source for method __init___0 """
        self.m_price = p_price

    def __eq__(self, p_other):
        """ generated source for method equals """
        if self is p_other:
            return True
        elif p_other is None:
            return False
        l_theOther = p_other
        if self.m_price != l_theOther.m_price:
            return False
        return True

