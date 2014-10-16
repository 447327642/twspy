""" generated source for module CommissionReport """
from __future__ import print_function
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class CommissionReport(object):
    """ generated source for class CommissionReport """
    m_execId = None
    m_commission = float()
    m_currency = None
    m_realizedPNL = float()
    m_yield = float()
    m_yieldRedemptionDate = int()

    #  YYYYMMDD format
    def __init__(self):
        """ generated source for method __init__ """
        self.m_commission = 0
        self.m_realizedPNL = 0
        self.m_yield = 0
        self.m_yieldRedemptionDate = 0

    def __eq__(self, p_other):
        """ generated source for method equals """
        l_bRetVal = False
        if p_other is None:
            l_bRetVal = False
        elif self is p_other:
            l_bRetVal = True
        else:
            l_theOther = p_other
            l_bRetVal = self.m_execId == l_theOther.m_execId
        return l_bRetVal

