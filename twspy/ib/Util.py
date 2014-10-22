""" generated source for module Util """
from __future__ import print_function
from ..lang.python import cmp
from ..lang.java import Double, Integer
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class Util(object):
    """ generated source for class Util """
    @classmethod
    def StringIsEmpty(cls, str_):
        """ generated source for method StringIsEmpty """
        return str_ is None or 0 == len(str_)

    @classmethod
    def NormalizeString(cls, str_):
        """ generated source for method NormalizeString """
        return str_ if str_ is not None else ""

    @classmethod
    def StringCompare(cls, lhs, rhs):
        """ generated source for method StringCompare """
        return cmp(str(lhs), str(rhs))

    @classmethod
    def StringCompareIgnCase(cls, lhs, rhs):
        """ generated source for method StringCompareIgnCase """
        return cmp(str(lhs).lower(), str(rhs).lower())

    @classmethod
    def VectorEqualsUnordered(cls, lhs, rhs):
        """ generated source for method VectorEqualsUnordered """
        if lhs == rhs:
            return True
        lhsCount = 0 if lhs is None else len(lhs)
        rhsCount = 0 if rhs is None else len(rhs)
        if lhsCount != rhsCount:
            return False
        if lhsCount == 0:
            return True
        matchedRhsElems = [None] * rhsCount
        lhsIdx = 0
        while lhsIdx < lhsCount:
            lhsElem = lhs[lhsIdx]
            rhsIdx = 0
            while rhsIdx < rhsCount:
                if matchedRhsElems[rhsIdx]:
                    rhsIdx += 1
                    continue 
                if lhsElem == rhs[rhsIdx]:
                    matchedRhsElems[rhsIdx] = True
                    break
                rhsIdx += 1
            if rhsIdx >= rhsCount:
                #  no matching elem found
                return False
            lhsIdx += 1
        return True

    @classmethod
    def IntMaxString(cls, value):
        """ generated source for method IntMaxString """
        return "" if (value == Integer.MAX_VALUE) else str(value)

    @classmethod
    def DoubleMaxString(cls, value):
        """ generated source for method DoubleMaxString """
        return "" if (value == Double.MAX_VALUE) else str(value)

