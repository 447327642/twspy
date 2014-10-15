""" generated source for module TagValue """
from __future__ import print_function
from ..lang.python import overloaded
from .Util import Util
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class TagValue(object):
    """ generated source for class TagValue """
    m_tag = None
    m_value = None

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, str, str)
    def __init___0(self, p_tag, p_value):
        """ generated source for method __init___0 """
        self.m_tag = p_tag
        self.m_value = p_value

    def equals(self, p_other):
        """ generated source for method equals """
        if self == p_other:
            return True
        if p_other == None:
            return False
        l_theOther = p_other
        if Util.StringCompare(self.m_tag, l_theOther.m_tag) != 0 or Util.StringCompare(self.m_value, l_theOther.m_value) != 0:
            return False
        return True

