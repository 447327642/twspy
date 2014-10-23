""" generated source for module EWrapperMsgGenerator """
from __future__ import print_function
from ._lang.java import Date, DateFormat, Double
from .AnyWrapperMsgGenerator import AnyWrapperMsgGenerator
from .EClientSocket import EClientSocket
from .MarketDataType import MarketDataType
from .TickType import TickType
from .Util import Util
#  Copyright (C) 2013 Interactive Brokers LLC. All rights reserved.  This code is subject to the terms
#  * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. 
# package: com.ib.client
class EWrapperMsgGenerator(AnyWrapperMsgGenerator):
    """ generated source for class EWrapperMsgGenerator """
    SCANNER_PARAMETERS = "SCANNER PARAMETERS:"
    FINANCIAL_ADVISOR = "FA:"

    @classmethod
    def tickPrice(cls, tickerId, field, price, canAutoExecute):
        """ generated source for method tickPrice """
        return "id=" + tickerId + "  " + TickType.getField(field) + "=" + price + " " + (" canAutoExecute" if (canAutoExecute != 0) else " noAutoExecute")

    @classmethod
    def tickSize(cls, tickerId, field, size):
        """ generated source for method tickSize """
        return "id=" + tickerId + "  " + TickType.getField(field) + "=" + size

    @classmethod
    def tickOptionComputation(cls, tickerId, field, impliedVol, delta, optPrice, pvDividend, gamma, vega, theta, undPrice):
        """ generated source for method tickOptionComputation """
        toAdd = "id=" + tickerId + "  " + TickType.getField(field) + ": vol = " + (Double.toString(impliedVol) if (impliedVol >= 0 and impliedVol != Double.MAX_VALUE) else "N/A") + " delta = " + (Double.toString(delta) if (abs(delta) <= 1) else "N/A") + " gamma = " + (Double.toString(gamma) if (abs(gamma) <= 1) else "N/A") + " vega = " + (Double.toString(vega) if (abs(vega) <= 1) else "N/A") + " theta = " + (Double.toString(theta) if (abs(theta) <= 1) else "N/A") + " optPrice = " + (Double.toString(optPrice) if (optPrice >= 0 and optPrice != Double.MAX_VALUE) else "N/A") + " pvDividend = " + (Double.toString(pvDividend) if (pvDividend >= 0 and pvDividend != Double.MAX_VALUE) else "N/A") + " undPrice = " + (Double.toString(undPrice) if (undPrice >= 0 and undPrice != Double.MAX_VALUE) else "N/A")
        return toAdd

    @classmethod
    def tickGeneric(cls, tickerId, tickType, value):
        """ generated source for method tickGeneric """
        return "id=" + tickerId + "  " + TickType.getField(tickType) + "=" + value

    @classmethod
    def tickString(cls, tickerId, tickType, value):
        """ generated source for method tickString """
        return "id=" + tickerId + "  " + TickType.getField(tickType) + "=" + value

    @classmethod
    def tickEFP(cls, tickerId, tickType, basisPoints, formattedBasisPoints, impliedFuture, holdDays, futureExpiry, dividendImpact, dividendsToExpiry):
        """ generated source for method tickEFP """
        return "id=" + tickerId + "  " + TickType.getField(tickType) + ": basisPoints = " + basisPoints + "/" + formattedBasisPoints + " impliedFuture = " + impliedFuture + " holdDays = " + holdDays + " futureExpiry = " + futureExpiry + " dividendImpact = " + dividendImpact + " dividends to expiry = " + dividendsToExpiry

    @classmethod
    def orderStatus(cls, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld):
        """ generated source for method orderStatus """
        return "order status: orderId=" + orderId + " clientId=" + clientId + " permId=" + permId + " status=" + status + " filled=" + filled + " remaining=" + remaining + " avgFillPrice=" + avgFillPrice + " lastFillPrice=" + lastFillPrice + " parent Id=" + parentId + " whyHeld=" + whyHeld

    @classmethod
    def openOrder(cls, orderId, contract, order, orderState):
        """ generated source for method openOrder """
        msg = "open order: orderId=" + orderId + " action=" + order.m_action + " quantity=" + order.m_totalQuantity + " conid=" + contract.m_conId + " symbol=" + contract.m_symbol + " secType=" + contract.m_secType + " expiry=" + contract.m_expiry + " strike=" + contract.m_strike + " right=" + contract.m_right + " multiplier=" + contract.m_multiplier + " exchange=" + contract.m_exchange + " primaryExch=" + contract.m_primaryExch + " currency=" + contract.m_currency + " localSymbol=" + contract.m_localSymbol + " tradingClass=" + contract.m_tradingClass + " type=" + order.m_orderType + " lmtPrice=" + Util.DoubleMaxString(order.m_lmtPrice) + " auxPrice=" + Util.DoubleMaxString(order.m_auxPrice) + " TIF=" + order.m_tif + " localSymbol=" + contract.m_localSymbol + " client Id=" + order.m_clientId + " parent Id=" + order.m_parentId + " permId=" + order.m_permId + " outsideRth=" + order.m_outsideRth + " hidden=" + order.m_hidden + " discretionaryAmt=" + order.m_discretionaryAmt + " displaySize=" + order.m_displaySize + " triggerMethod=" + order.m_triggerMethod + " goodAfterTime=" + order.m_goodAfterTime + " goodTillDate=" + order.m_goodTillDate + " faGroup=" + order.m_faGroup + " faMethod=" + order.m_faMethod + " faPercentage=" + order.m_faPercentage + " faProfile=" + order.m_faProfile + " shortSaleSlot=" + order.m_shortSaleSlot + " designatedLocation=" + order.m_designatedLocation + " exemptCode=" + order.m_exemptCode + " ocaGroup=" + order.m_ocaGroup + " ocaType=" + order.m_ocaType + " rule80A=" + order.m_rule80A + " allOrNone=" + order.m_allOrNone + " minQty=" + Util.IntMaxString(order.m_minQty) + " percentOffset=" + Util.DoubleMaxString(order.m_percentOffset) + " eTradeOnly=" + order.m_eTradeOnly + " firmQuoteOnly=" + order.m_firmQuoteOnly + " nbboPriceCap=" + Util.DoubleMaxString(order.m_nbboPriceCap) + " optOutSmartRouting=" + order.m_optOutSmartRouting + " auctionStrategy=" + order.m_auctionStrategy + " startingPrice=" + Util.DoubleMaxString(order.m_startingPrice) + " stockRefPrice=" + Util.DoubleMaxString(order.m_stockRefPrice) + " delta=" + Util.DoubleMaxString(order.m_delta) + " stockRangeLower=" + Util.DoubleMaxString(order.m_stockRangeLower) + " stockRangeUpper=" + Util.DoubleMaxString(order.m_stockRangeUpper) + " volatility=" + Util.DoubleMaxString(order.m_volatility) + " volatilityType=" + order.m_volatilityType + " deltaNeutralOrderType=" + order.m_deltaNeutralOrderType + " deltaNeutralAuxPrice=" + Util.DoubleMaxString(order.m_deltaNeutralAuxPrice) + " deltaNeutralConId=" + order.m_deltaNeutralConId + " deltaNeutralSettlingFirm=" + order.m_deltaNeutralSettlingFirm + " deltaNeutralClearingAccount=" + order.m_deltaNeutralClearingAccount + " deltaNeutralClearingIntent=" + order.m_deltaNeutralClearingIntent + " deltaNeutralOpenClose=" + order.m_deltaNeutralOpenClose + " deltaNeutralShortSale=" + order.m_deltaNeutralShortSale + " deltaNeutralShortSaleSlot=" + order.m_deltaNeutralShortSaleSlot + " deltaNeutralDesignatedLocation=" + order.m_deltaNeutralDesignatedLocation + " continuousUpdate=" + order.m_continuousUpdate + " referencePriceType=" + order.m_referencePriceType + " trailStopPrice=" + Util.DoubleMaxString(order.m_trailStopPrice) + " trailingPercent=" + Util.DoubleMaxString(order.m_trailingPercent) + " scaleInitLevelSize=" + Util.IntMaxString(order.m_scaleInitLevelSize) + " scaleSubsLevelSize=" + Util.IntMaxString(order.m_scaleSubsLevelSize) + " scalePriceIncrement=" + Util.DoubleMaxString(order.m_scalePriceIncrement) + " scalePriceAdjustValue=" + Util.DoubleMaxString(order.m_scalePriceAdjustValue) + " scalePriceAdjustInterval=" + Util.IntMaxString(order.m_scalePriceAdjustInterval) + " scaleProfitOffset=" + Util.DoubleMaxString(order.m_scaleProfitOffset) + " scaleAutoReset=" + order.m_scaleAutoReset + " scaleInitPosition=" + Util.IntMaxString(order.m_scaleInitPosition) + " scaleInitFillQty=" + Util.IntMaxString(order.m_scaleInitFillQty) + " scaleRandomPercent=" + order.m_scaleRandomPercent + " hedgeType=" + order.m_hedgeType + " hedgeParam=" + order.m_hedgeParam + " account=" + order.m_account + " settlingFirm=" + order.m_settlingFirm + " clearingAccount=" + order.m_clearingAccount + " clearingIntent=" + order.m_clearingIntent + " notHeld=" + order.m_notHeld + " whatIf=" + order.m_whatIf
        if "BAG" == contract.m_secType:
            if contract.m_comboLegsDescrip is not None:
                msg += " comboLegsDescrip=" + contract.m_comboLegsDescrip
            msg += " comboLegs={"
            if contract.m_comboLegs is not None:
                i = 0
                while i < len(contract.m_comboLegs):
                    comboLeg = contract.m_comboLegs[i]
                    msg += " leg " + (i + 1) + ": "
                    msg += "conId=" + comboLeg.m_conId
                    msg += " ratio=" + comboLeg.m_ratio
                    msg += " action=" + comboLeg.m_action
                    msg += " exchange=" + comboLeg.m_exchange
                    msg += " openClose=" + comboLeg.m_openClose
                    msg += " shortSaleSlot=" + comboLeg.m_shortSaleSlot
                    msg += " designatedLocation=" + comboLeg.m_designatedLocation
                    msg += " exemptCode=" + comboLeg.m_exemptCode
                    if order.m_orderComboLegs is not None and len(contract.m_comboLegs) == len(order.m_orderComboLegs):
                        orderComboLeg = order.m_orderComboLegs[i]
                        msg += " price=" + Util.DoubleMaxString(orderComboLeg.m_price)
                    msg += ";"
                    i += 1
            msg += "}"
            if order.m_basisPoints != Double.MAX_VALUE:
                msg += " basisPoints=" + Util.DoubleMaxString(order.m_basisPoints)
                msg += " basisPointsType=" + Util.IntMaxString(order.m_basisPointsType)
        if contract.m_underComp is not None:
            underComp = contract.m_underComp
            msg += " underComp.conId =" + underComp.m_conId + " underComp.delta =" + underComp.m_delta + " underComp.price =" + underComp.m_price
        if not Util.StringIsEmpty(order.m_algoStrategy):
            msg += " algoStrategy=" + order.m_algoStrategy
            msg += " algoParams={"
            if order.m_algoParams is not None:
                algoParams = order.m_algoParams
                i = 0
                while i < len(algoParams):
                    param = algoParams.elementAt(i)
                    if i > 0:
                        msg += ","
                    msg += param.m_tag + "=" + param.m_value
                    i += 1
            msg += "}"
        if "BAG" == contract.m_secType:
            msg += " smartComboRoutingParams={"
            if order.m_smartComboRoutingParams is not None:
                smartComboRoutingParams = order.m_smartComboRoutingParams
                i = 0
                while i < len(smartComboRoutingParams):
                    param = smartComboRoutingParams.elementAt(i)
                    if i > 0:
                        msg += ","
                    msg += param.m_tag + "=" + param.m_value
                    i += 1
            msg += "}"
        orderStateMsg = " status=" + orderState.m_status + " initMargin=" + orderState.m_initMargin + " maintMargin=" + orderState.m_maintMargin + " equityWithLoan=" + orderState.m_equityWithLoan + " commission=" + Util.DoubleMaxString(orderState.m_commission) + " minCommission=" + Util.DoubleMaxString(orderState.m_minCommission) + " maxCommission=" + Util.DoubleMaxString(orderState.m_maxCommission) + " commissionCurrency=" + orderState.m_commissionCurrency + " warningText=" + orderState.m_warningText
        return msg + orderStateMsg

    @classmethod
    def openOrderEnd(cls):
        """ generated source for method openOrderEnd """
        return " =============== end ==============="

    @classmethod
    def updateAccountValue(cls, key, value, currency, accountName):
        """ generated source for method updateAccountValue """
        return "updateAccountValue: " + key + " " + value + " " + currency + " " + accountName

    @classmethod
    def updatePortfolio(cls, contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, accountName):
        """ generated source for method updatePortfolio """
        msg = "updatePortfolio: " + cls.contractMsg(contract) + position + " " + marketPrice + " " + marketValue + " " + averageCost + " " + unrealizedPNL + " " + realizedPNL + " " + accountName
        return msg

    @classmethod
    def updateAccountTime(cls, timeStamp):
        """ generated source for method updateAccountTime """
        return "updateAccountTime: " + timeStamp

    @classmethod
    def accountDownloadEnd(cls, accountName):
        """ generated source for method accountDownloadEnd """
        return "accountDownloadEnd: " + accountName

    @classmethod
    def nextValidId(cls, orderId):
        """ generated source for method nextValidId """
        return "Next Valid Order ID: " + orderId

    @classmethod
    def contractDetails(cls, reqId, contractDetails):
        """ generated source for method contractDetails """
        contract = contractDetails.m_summary
        msg = "reqId = " + reqId + " ===================================\n" + " ---- Contract Details begin ----\n" + cls.contractMsg(contract) + cls.contractDetailsMsg(contractDetails) + " ---- Contract Details End ----\n"
        return msg

    @classmethod
    def contractDetailsMsg(cls, contractDetails):
        """ generated source for method contractDetailsMsg """
        msg = "marketName = " + contractDetails.m_marketName + "\n" + "minTick = " + contractDetails.m_minTick + "\n" + "price magnifier = " + contractDetails.m_priceMagnifier + "\n" + "orderTypes = " + contractDetails.m_orderTypes + "\n" + "validExchanges = " + contractDetails.m_validExchanges + "\n" + "underConId = " + contractDetails.m_underConId + "\n" + "longName = " + contractDetails.m_longName + "\n" + "contractMonth = " + contractDetails.m_contractMonth + "\n" + "industry = " + contractDetails.m_industry + "\n" + "category = " + contractDetails.m_category + "\n" + "subcategory = " + contractDetails.m_subcategory + "\n" + "timeZoneId = " + contractDetails.m_timeZoneId + "\n" + "tradingHours = " + contractDetails.m_tradingHours + "\n" + "liquidHours = " + contractDetails.m_liquidHours + "\n" + "evRule = " + contractDetails.m_evRule + "\n" + "evMultiplier = " + contractDetails.m_evMultiplier + "\n" + cls.contractDetailsSecIdList(contractDetails)
        return msg

    @classmethod
    def contractMsg(cls, contract):
        """ generated source for method contractMsg """
        msg = "conid = " + contract.m_conId + "\n" + "symbol = " + contract.m_symbol + "\n" + "secType = " + contract.m_secType + "\n" + "expiry = " + contract.m_expiry + "\n" + "strike = " + contract.m_strike + "\n" + "right = " + contract.m_right + "\n" + "multiplier = " + contract.m_multiplier + "\n" + "exchange = " + contract.m_exchange + "\n" + "primaryExch = " + contract.m_primaryExch + "\n" + "currency = " + contract.m_currency + "\n" + "localSymbol = " + contract.m_localSymbol + "\n" + "tradingClass = " + contract.m_tradingClass + "\n"
        return msg

    @classmethod
    def bondContractDetails(cls, reqId, contractDetails):
        """ generated source for method bondContractDetails """
        contract = contractDetails.m_summary
        msg = "reqId = " + reqId + " ===================================\n" + " ---- Bond Contract Details begin ----\n" + "symbol = " + contract.m_symbol + "\n" + "secType = " + contract.m_secType + "\n" + "cusip = " + contractDetails.m_cusip + "\n" + "coupon = " + contractDetails.m_coupon + "\n" + "maturity = " + contractDetails.m_maturity + "\n" + "issueDate = " + contractDetails.m_issueDate + "\n" + "ratings = " + contractDetails.m_ratings + "\n" + "bondType = " + contractDetails.m_bondType + "\n" + "couponType = " + contractDetails.m_couponType + "\n" + "convertible = " + contractDetails.m_convertible + "\n" + "callable = " + contractDetails.m_callable + "\n" + "putable = " + contractDetails.m_putable + "\n" + "descAppend = " + contractDetails.m_descAppend + "\n" + "exchange = " + contract.m_exchange + "\n" + "currency = " + contract.m_currency + "\n" + "marketName = " + contractDetails.m_marketName + "\n" + "tradingClass = " + contract.m_tradingClass + "\n" + "conid = " + contract.m_conId + "\n" + "minTick = " + contractDetails.m_minTick + "\n" + "orderTypes = " + contractDetails.m_orderTypes + "\n" + "validExchanges = " + contractDetails.m_validExchanges + "\n" + "nextOptionDate = " + contractDetails.m_nextOptionDate + "\n" + "nextOptionType = " + contractDetails.m_nextOptionType + "\n" + "nextOptionPartial = " + contractDetails.m_nextOptionPartial + "\n" + "notes = " + contractDetails.m_notes + "\n" + "longName = " + contractDetails.m_longName + "\n" + "evRule = " + contractDetails.m_evRule + "\n" + "evMultiplier = " + contractDetails.m_evMultiplier + "\n" + cls.contractDetailsSecIdList(contractDetails) + " ---- Bond Contract Details End ----\n"
        return msg

    @classmethod
    def contractDetailsSecIdList(cls, contractDetails):
        """ generated source for method contractDetailsSecIdList """
        msg = "secIdList={"
        if contractDetails.m_secIdList is not None:
            secIdList = contractDetails.m_secIdList
            i = 0
            while i < len(secIdList):
                param = secIdList.elementAt(i)
                if i > 0:
                    msg += ","
                msg += param.m_tag + "=" + param.m_value
                i += 1
        msg += "}\n"
        return msg

    @classmethod
    def contractDetailsEnd(cls, reqId):
        """ generated source for method contractDetailsEnd """
        return "reqId = " + reqId + " =============== end ==============="

    @classmethod
    def execDetails(cls, reqId, contract, execution):
        """ generated source for method execDetails """
        msg = " ---- Execution Details begin ----\n" + "reqId = " + reqId + "\n" + "orderId = " + execution.m_orderId + "\n" + "clientId = " + execution.m_clientId + "\n" + cls.contractMsg(contract) + "execId = " + execution.m_execId + "\n" + "time = " + execution.m_time + "\n" + "acctNumber = " + execution.m_acctNumber + "\n" + "executionExchange = " + execution.m_exchange + "\n" + "side = " + execution.m_side + "\n" + "shares = " + execution.m_shares + "\n" + "price = " + execution.m_price + "\n" + "permId = " + execution.m_permId + "\n" + "liquidation = " + execution.m_liquidation + "\n" + "cumQty = " + execution.m_cumQty + "\n" + "avgPrice = " + execution.m_avgPrice + "\n" + "orderRef = " + execution.m_orderRef + "\n" + "evRule = " + execution.m_evRule + "\n" + "evMultiplier = " + execution.m_evMultiplier + "\n" + " ---- Execution Details end ----\n"
        return msg

    @classmethod
    def execDetailsEnd(cls, reqId):
        """ generated source for method execDetailsEnd """
        return "reqId = " + reqId + " =============== end ==============="

    @classmethod
    def updateMktDepth(cls, tickerId, position, operation, side, price, size):
        """ generated source for method updateMktDepth """
        return "updateMktDepth: " + tickerId + " " + position + " " + operation + " " + side + " " + price + " " + size

    @classmethod
    def updateMktDepthL2(cls, tickerId, position, marketMaker, operation, side, price, size):
        """ generated source for method updateMktDepthL2 """
        return "updateMktDepth: " + tickerId + " " + position + " " + marketMaker + " " + operation + " " + side + " " + price + " " + size

    @classmethod
    def updateNewsBulletin(cls, msgId, msgType, message, origExchange):
        """ generated source for method updateNewsBulletin """
        return "MsgId=" + msgId + " :: MsgType=" + msgType + " :: Origin=" + origExchange + " :: Message=" + message

    @classmethod
    def managedAccounts(cls, accountsList):
        """ generated source for method managedAccounts """
        return "Connected : The list of managed accounts are : [" + accountsList + "]"

    @classmethod
    def receiveFA(cls, faDataType, xml):
        """ generated source for method receiveFA """
        return cls.FINANCIAL_ADVISOR + " " + EClientSocket.faMsgTypeName(faDataType) + " " + xml

    @classmethod
    def historicalData(cls, reqId, date, open, high, low, close, volume, count, WAP, hasGaps):
        """ generated source for method historicalData """
        return "id=" + reqId + " date = " + date + " open=" + open + " high=" + high + " low=" + low + " close=" + close + " volume=" + volume + " count=" + count + " WAP=" + WAP + " hasGaps=" + hasGaps

    @classmethod
    def realtimeBar(cls, reqId, time, open, high, low, close, volume, wap, count):
        """ generated source for method realtimeBar """
        return "id=" + reqId + " time = " + time + " open=" + open + " high=" + high + " low=" + low + " close=" + close + " volume=" + volume + " count=" + count + " WAP=" + wap

    @classmethod
    def scannerParameters(cls, xml):
        """ generated source for method scannerParameters """
        return cls.SCANNER_PARAMETERS + "\n" + xml

    @classmethod
    def scannerData(cls, reqId, rank, contractDetails, distance, benchmark, projection, legsStr):
        """ generated source for method scannerData """
        contract = contractDetails.m_summary
        return "id = " + reqId + " rank=" + rank + " symbol=" + contract.m_symbol + " secType=" + contract.m_secType + " expiry=" + contract.m_expiry + " strike=" + contract.m_strike + " right=" + contract.m_right + " exchange=" + contract.m_exchange + " currency=" + contract.m_currency + " localSymbol=" + contract.m_localSymbol + " marketName=" + contractDetails.m_marketName + " tradingClass=" + contract.m_tradingClass + " distance=" + distance + " benchmark=" + benchmark + " projection=" + projection + " legsStr=" + legsStr

    @classmethod
    def scannerDataEnd(cls, reqId):
        """ generated source for method scannerDataEnd """
        return "id = " + reqId + " =============== end ==============="

    @classmethod
    def currentTime(cls, time):
        """ generated source for method currentTime """
        return "current time = " + time + " (" + DateFormat.getDateTimeInstance().format(Date(time * 1000)) + ")"

    @classmethod
    def fundamentalData(cls, reqId, data):
        """ generated source for method fundamentalData """
        return "id  = " + reqId + " len = " + len(data) + '\n' + data

    @classmethod
    def deltaNeutralValidation(cls, reqId, underComp):
        """ generated source for method deltaNeutralValidation """
        return "id = " + reqId + " underComp.conId =" + underComp.m_conId + " underComp.delta =" + underComp.m_delta + " underComp.price =" + underComp.m_price

    @classmethod
    def tickSnapshotEnd(cls, tickerId):
        """ generated source for method tickSnapshotEnd """
        return "id=" + tickerId + " =============== end ==============="

    @classmethod
    def marketDataType(cls, reqId, marketDataType):
        """ generated source for method marketDataType """
        return "id=" + reqId + " marketDataType = " + MarketDataType.getField(marketDataType)

    @classmethod
    def commissionReport(cls, commissionReport):
        """ generated source for method commissionReport """
        msg = "commission report:" + " execId=" + commissionReport.m_execId + " commission=" + Util.DoubleMaxString(commissionReport.m_commission) + " currency=" + commissionReport.m_currency + " realizedPNL=" + Util.DoubleMaxString(commissionReport.m_realizedPNL) + " yield=" + Util.DoubleMaxString(commissionReport.m_yield) + " yieldRedemptionDate=" + Util.IntMaxString(commissionReport.m_yieldRedemptionDate)
        return msg

    @classmethod
    def position(cls, account, contract, position, avgCost):
        """ generated source for method position """
        msg = " ---- Position begin ----\n" + "account = " + account + "\n" + cls.contractMsg(contract) + "position = " + Util.IntMaxString(position) + "\n" + "avgCost = " + Util.DoubleMaxString(avgCost) + "\n" + " ---- Position end ----\n"
        return msg

    @classmethod
    def positionEnd(cls):
        """ generated source for method positionEnd """
        return " =============== end ==============="

    @classmethod
    def accountSummary(cls, reqId, account, tag, value, currency):
        """ generated source for method accountSummary """
        msg = " ---- Account Summary begin ----\n" + "reqId = " + reqId + "\n" + "account = " + account + "\n" + "tag = " + tag + "\n" + "value = " + value + "\n" + "currency = " + currency + "\n" + " ---- Account Summary end ----\n"
        return msg

    @classmethod
    def accountSummaryEnd(cls, reqId):
        """ generated source for method accountSummaryEnd """
        return "id=" + reqId + " =============== end ==============="

