import ib.opt
import pytest

import twspy.opt

from .support import config, sleep_until

@pytest.mark.parametrize('message', [twspy.opt.message, ib.opt.message])
def test_message_namespace(message):
    assert message.nextValidId.__name__ == 'NextValidId'
    assert message.nextValidId.typeName == 'nextValidId'
    with pytest.raises(AttributeError):
        message.NextValidId

    msg = message.openOrderEnd()
    assert str(msg) == "<openOrderEnd>"

    msg = message.nextValidId()
    assert str(msg) == "<nextValidId orderId=None>"
    msg = message.nextValidId(orderId=42)
    assert str(msg) == "<nextValidId orderId=42>"
    pytest.raises(TypeError, message.nextValidId, 42)
    pytest.raises(AssertionError, message.nextValidId, orderId=42, extraArg=None)

    msg = message.orderStatus()
    assert str(msg) == "<orderStatus orderId=None, status=None, filled=None, remaining=None, avgFillPrice=None, permId=None, parentId=None, lastFillPrice=None, clientId=None, whyHeld=None>"

@pytest.fixture(params=[twspy.opt.ibConnection, ib.opt.ibConnection])
def con(request):
    con = request.param(*config)
    con.enableLogging()
    request.addfinalizer(lambda: con.disconnect())
    return con

def test_accept_names(con):
    def callback(msg): pass
    for arg in ['NextValidId', 'NEXTVALIDID', 'INVALID NAME']:
        assert con.register(callback, arg)
        assert con.unregister(callback, arg)

def test_basic(con):
    seen = {}
    def callback(msg):
        seen[type(msg).__name__] = msg

    assert con.registerAll(callback)

    assert not con.disconnect()
    assert con.connect()
    assert sleep_until(lambda: 'NextValidId' in seen, 1.0)
    assert seen['NextValidId'].orderId > 0

    assert con.disconnect()

def test_which_names_work(con):
    from functools import partial
    seen = []
    def callback(arg, msg):
        seen.append(arg)

    for name in ['nextValidId', 'NextValidId', 'NEXTVALIDID']:
        assert con.register(partial(callback, name), name)

    assert con.connect()
    assert sleep_until(lambda: seen == ['NextValidId'], 1.0)

def test_exception_in_handler(con):
    seen = []
    def callback1(msg):
        raise Exception('test')
    def callback2(msg):
        seen.append(True)

    assert con.register(callback1, 'NextValidId')
    assert con.register(callback2, 'NextValidId')
    assert con.connect()
    assert sleep_until(lambda: seen, 1.0)

    assert con.isConnected()
    assert con.unregister(callback1, 'NextValidId')
    assert con.unregister(callback2, 'NextValidId')

def test_mutate_message(con):
    seen = []
    def callback1(msg):
        assert msg.orderId > 0
        msg.orderId = "test"
    def callback2(msg):
        if msg.orderId == "test":
            seen.append(True)

    assert con.register(callback1, 'NextValidId')
    assert con.register(callback2, 'NextValidId')
    assert con.connect()
    assert sleep_until(lambda: seen, 1.0)
