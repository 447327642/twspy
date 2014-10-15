""" generated source for module MarketDataType """
from __future__ import print_function
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class MarketDataType(object):
    """ generated source for class MarketDataType """
    #  constants - market data types
    REALTIME = 1
    FROZEN = 2

    @classmethod
    def getField(cls, marketDataType):
        """ generated source for method getField """
        if marketDataType == cls.REALTIME:
            return "Real-Time"
        elif marketDataType == cls.FROZEN:
            return "Frozen"
        else:
            return "Unknown"

    @classmethod
    def getFields(cls):
        """ generated source for method getFields """
        totalFields = int()
        fields = [None] * totalFields
        i = 0
        while i < totalFields:
            fields[i] = MarketDataType.getField(i + 1)
            i += 1
        return fields

