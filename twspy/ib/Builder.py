""" generated source for module Builder """
from __future__ import print_function
from ._lang.python import overloaded
from ._lang.java import Double, Integer, StringBuilder
from .IApiEnum import IApiEnum
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
#  This class is used to build messages so the entire message can be
#  *  sent to the socket in a single write. 
class Builder(object):
    """ generated source for class Builder """
    SEP = chr(0)
    m_sb = StringBuilder(4096)

    @overloaded
    def send(self, a):
        """ generated source for method send """
        self.send("" if a == Integer.MAX_VALUE else str(a))

    @send.register(object, float)
    def send_0(self, a):
        """ generated source for method send_0 """
        self.send("" if a == Double.MAX_VALUE else str(a))

    @send.register(object, bool)
    def send_1(self, a):
        """ generated source for method send_1 """
        self.send(1 if a else 0)

    @send.register(object, IApiEnum)
    def send_2(self, a):
        """ generated source for method send_2 """
        self.send(a.getApiString())

    @send.register(object, str)
    def send_3(self, a):
        """ generated source for method send_3 """
        if a is not None:
            self.m_sb.append(a)
        self.m_sb.append(self.SEP)

    def __str__(self):
        """ generated source for method toString """
        return self.m_sb.__str__()

    def getBytes(self):
        """ generated source for method getBytes """
        return self.m_sb.__str__().encode()

