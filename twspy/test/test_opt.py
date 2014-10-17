import pytest

from twspy.opt import ibConnection, message

from .support import config, sleep_until

@pytest.fixture
def con(request):
    con = ibConnection(*config)
    con.enableLogging()
    request.addfinalizer(lambda: con.disconnect())
    return con

def test_message_namespace():
    import twspy
    message.nextValidId
    message.NextValidId
    twspy.message.nextValidId
    with pytest.raises(AttributeError):
        twspy.message.NextValidId

def test_accept_capital_names():
    def callback(msg): pass
    con = ibConnection()
    for arg in [message.NextValidId, 'NextValidId']:
        assert con.register(callback, arg)
        assert con.unregister(callback, arg)
    with pytest.raises(AssertionError):
        con.register(callback, 'NEXTVALIDID')

def test_basic(con):
    seen = {}
    def callback(msg):
        seen[type(msg).__name__] = msg

    assert con.registerAll(callback)

    assert not con.disconnect()
    assert con.connect()
    assert sleep_until(lambda: 'nextValidId' in seen, 1.0)
    assert seen['nextValidId'].orderId > 0

    assert con.disconnect()

def test_exception_in_handler(con):
    seen = []
    def callback1(msg):
        raise Exception('test')
    def callback2(msg):
        seen.append(True)

    assert con.register(callback1, 'nextValidId')
    assert con.register(callback2, 'nextValidId')
    assert con.connect()
    assert sleep_until(lambda: seen, 1.0)

    assert con.isConnected()
    assert con.unregister(callback1, 'nextValidId')
    assert con.unregister(callback2, 'nextValidId')
