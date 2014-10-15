""" generated source for module AnyWrapper """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
from ..lang.python import overloaded
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class AnyWrapper(object):
    """ generated source for interface AnyWrapper """
    __metaclass__ = ABCMeta
    @abstractmethod
    @overloaded
    def error(self, e):
        """ generated source for method error """

    @abstractmethod
    @error.register(object, str)
    def error_0(self, str_):
        """ generated source for method error_0 """

    @abstractmethod
    @error.register(object, int, int, str)
    def error_1(self, id, errorCode, errorMsg):
        """ generated source for method error_1 """

    @abstractmethod
    def connectionClosed(self):
        """ generated source for method connectionClosed """

