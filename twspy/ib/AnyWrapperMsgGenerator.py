""" generated source for module AnyWrapperMsgGenerator """
from __future__ import print_function
from ._lang.python import classmethod, overloaded
from ._lang.java import Integer
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class AnyWrapperMsgGenerator(object):
    """ generated source for class AnyWrapperMsgGenerator """
    @classmethod
    @overloaded
    def error(cls, ex):
        """ generated source for method error """
        return "Error - " + ex

    @classmethod
    @error.register(object, str)
    def error_0(cls, str_):
        """ generated source for method error_0 """
        return str_

    @classmethod
    @error.register(object, int, int, str)
    def error_1(cls, id, errorCode, errorMsg):
        """ generated source for method error_1 """
        err = Integer.toString(id)
        err += " | "
        err += Integer.toString(errorCode)
        err += " | "
        err += errorMsg
        return err

    @classmethod
    def connectionClosed(cls):
        """ generated source for method connectionClosed """
        return "Connection Closed"

