""" generated source for module ContractDetails """
from __future__ import print_function
from ..lang.python import overloaded
from .Contract import Contract
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class ContractDetails(object):
    """ generated source for class ContractDetails """
    m_summary = None
    m_marketName = None
    m_minTick = float()
    m_priceMagnifier = int()
    m_orderTypes = None
    m_validExchanges = None
    m_underConId = int()
    m_longName = None
    m_contractMonth = None
    m_industry = None
    m_category = None
    m_subcategory = None
    m_timeZoneId = None
    m_tradingHours = None
    m_liquidHours = None
    m_evRule = None
    m_evMultiplier = float()
    m_secIdList = None

    #  CUSIP/ISIN/etc.
    #  BOND values
    m_cusip = None
    m_ratings = None
    m_descAppend = None
    m_bondType = None
    m_couponType = None
    m_callable = False
    m_putable = False
    m_coupon = 0
    m_convertible = False
    m_maturity = None
    m_issueDate = None
    m_nextOptionDate = None
    m_nextOptionType = None
    m_nextOptionPartial = False
    m_notes = None

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.m_summary = Contract()
        self.m_minTick = 0
        self.m_underConId = 0
        self.m_evMultiplier = 0

    @__init__.register(object, Contract, str, float, str, str, int, str, str, str, str, str, str, str, str, str, float)
    def __init___0(self, p_summary, p_marketName, p_minTick, p_orderTypes, p_validExchanges, p_underConId, p_longName, p_contractMonth, p_industry, p_category, p_subcategory, p_timeZoneId, p_tradingHours, p_liquidHours, p_evRule, p_evMultiplier):
        """ generated source for method __init___0 """
        self.m_summary = p_summary
        self.m_marketName = p_marketName
        self.m_minTick = p_minTick
        self.m_orderTypes = p_orderTypes
        self.m_validExchanges = p_validExchanges
        self.m_underConId = p_underConId
        self.m_longName = p_longName
        self.m_contractMonth = p_contractMonth
        self.m_industry = p_industry
        self.m_category = p_category
        self.m_subcategory = p_subcategory
        self.m_timeZoneId = p_timeZoneId
        self.m_tradingHours = p_tradingHours
        self.m_liquidHours = p_liquidHours
        self.m_evRule = p_evRule
        self.m_evMultiplier = p_evMultiplier

