""" generated source for module EClientErrors """
from __future__ import print_function
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class EClientErrors(object):
    """ generated source for class EClientErrors """
    def __init__(self):
        """ generated source for method __init__ """

    class CodeMsgPair(object):
        """ generated source for class CodeMsgPair """
        #  members vars
        m_errorCode = int()
        m_errorMsg = None

        #  Get/Set methods
        def code_(self):
            """ generated source for method code_ """
            return self.m_errorCode

        def msg(self):
            """ generated source for method msg """
            return self.m_errorMsg

        #  Constructor 
        def __init__(self, i, errString):
            """ generated source for method __init__ """
            self.m_errorCode = i
            self.m_errorMsg = errString

    NO_VALID_ID = -1
    NOT_CONNECTED = CodeMsgPair(504, "Not connected")
    UPDATE_TWS = CodeMsgPair(503, "The TWS is out of date and must be upgraded.")
    ALREADY_CONNECTED = CodeMsgPair(501, "Already connected.")
    CONNECT_FAIL = CodeMsgPair(502, "Couldn't connect to TWS.  Confirm that \"Enable ActiveX and Socket Clients\" is enabled on the TWS \"Configure->API\" menu.")
    FAIL_SEND = CodeMsgPair(509, "Failed to send message - ")

    #  generic message; all future messages should use this
    UNKNOWN_ID = CodeMsgPair(505, "Fatal Error: Unknown message id.")
    FAIL_SEND_REQMKT = CodeMsgPair(510, "Request Market Data Sending Error - ")
    FAIL_SEND_CANMKT = CodeMsgPair(511, "Cancel Market Data Sending Error - ")
    FAIL_SEND_ORDER = CodeMsgPair(512, "Order Sending Error - ")
    FAIL_SEND_ACCT = CodeMsgPair(513, "Account Update Request Sending Error -")
    FAIL_SEND_EXEC = CodeMsgPair(514, "Request For Executions Sending Error -")
    FAIL_SEND_CORDER = CodeMsgPair(515, "Cancel Order Sending Error -")
    FAIL_SEND_OORDER = CodeMsgPair(516, "Request Open Order Sending Error -")
    UNKNOWN_CONTRACT = CodeMsgPair(517, "Unknown contract. Verify the contract details supplied.")
    FAIL_SEND_REQCONTRACT = CodeMsgPair(518, "Request Contract Data Sending Error - ")
    FAIL_SEND_REQMKTDEPTH = CodeMsgPair(519, "Request Market Depth Sending Error - ")
    FAIL_SEND_CANMKTDEPTH = CodeMsgPair(520, "Cancel Market Depth Sending Error - ")
    FAIL_SEND_SERVER_LOG_LEVEL = CodeMsgPair(521, "Set Server Log Level Sending Error - ")
    FAIL_SEND_FA_REQUEST = CodeMsgPair(522, "FA Information Request Sending Error - ")
    FAIL_SEND_FA_REPLACE = CodeMsgPair(523, "FA Information Replace Sending Error - ")
    FAIL_SEND_REQSCANNER = CodeMsgPair(524, "Request Scanner Subscription Sending Error - ")
    FAIL_SEND_CANSCANNER = CodeMsgPair(525, "Cancel Scanner Subscription Sending Error - ")
    FAIL_SEND_REQSCANNERPARAMETERS = CodeMsgPair(526, "Request Scanner Parameter Sending Error - ")
    FAIL_SEND_REQHISTDATA = CodeMsgPair(527, "Request Historical Data Sending Error - ")
    FAIL_SEND_CANHISTDATA = CodeMsgPair(528, "Request Historical Data Sending Error - ")
    FAIL_SEND_REQRTBARS = CodeMsgPair(529, "Request Real-time Bar Data Sending Error - ")
    FAIL_SEND_CANRTBARS = CodeMsgPair(530, "Cancel Real-time Bar Data Sending Error - ")
    FAIL_SEND_REQCURRTIME = CodeMsgPair(531, "Request Current Time Sending Error - ")
    FAIL_SEND_REQFUNDDATA = CodeMsgPair(532, "Request Fundamental Data Sending Error - ")
    FAIL_SEND_CANFUNDDATA = CodeMsgPair(533, "Cancel Fundamental Data Sending Error - ")
    FAIL_SEND_REQCALCIMPLIEDVOLAT = CodeMsgPair(534, "Request Calculate Implied Volatility Sending Error - ")
    FAIL_SEND_REQCALCOPTIONPRICE = CodeMsgPair(535, "Request Calculate Option Price Sending Error - ")
    FAIL_SEND_CANCALCIMPLIEDVOLAT = CodeMsgPair(536, "Cancel Calculate Implied Volatility Sending Error - ")
    FAIL_SEND_CANCALCOPTIONPRICE = CodeMsgPair(537, "Cancel Calculate Option Price Sending Error - ")
    FAIL_SEND_REQGLOBALCANCEL = CodeMsgPair(538, "Request Global Cancel Sending Error - ")
    FAIL_SEND_REQMARKETDATATYPE = CodeMsgPair(539, "Request Market Data Type Sending Error - ")
    FAIL_SEND_REQPOSITIONS = CodeMsgPair(540, "Request Positions Sending Error - ")
    FAIL_SEND_CANPOSITIONS = CodeMsgPair(541, "Cancel Positions Sending Error - ")
    FAIL_SEND_REQACCOUNTDATA = CodeMsgPair(542, "Request Account Data Sending Error - ")
    FAIL_SEND_CANACCOUNTDATA = CodeMsgPair(543, "Cancel Account Data Sending Error - ")
    FAIL_SEND_VERIFYREQUEST = CodeMsgPair(544, "Verify Request Sending Error - ")
    FAIL_SEND_VERIFYMESSAGE = CodeMsgPair(545, "Verify Message Sending Error - ")
    FAIL_SEND_QUERYDISPLAYGROUPS = CodeMsgPair(546, "Query Display Groups Sending Error - ")
    FAIL_SEND_SUBSCRIBETOGROUPEVENTS = CodeMsgPair(547, "Subscribe To Group Events Sending Error - ")
    FAIL_SEND_UPDATEDISPLAYGROUP = CodeMsgPair(548, "Update Display Group Sending Error - ")
    FAIL_SEND_UNSUBSCRIBEFROMGROUPEVENTS = CodeMsgPair(549, "Unsubscribe From Group Events Sending Error - ")
    FAIL_SEND_STARTAPI = CodeMsgPair(550, "Start API Sending Error - ")
