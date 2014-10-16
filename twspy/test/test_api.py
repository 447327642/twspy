import os

import pytest

from twspy import Connection, message

from .support import sleep_until

TWS_HOST = os.environ.get('TWS_HOST', '127.0.0.1')
TWS_PORT = int(os.environ.get('TWS_PORT', 7496))
TWS_CLID = int(os.environ.get('TWS_CLID', 0))

def test_constructor():
    assert Connection() is not None
    assert Connection(clientId=0) is not None
    assert Connection(host='test', port=12345, clientId=0) is not None

def test_register():
    def callback(msg): pass
    con = Connection()
    for arg in [message.nextValidId, 'nextValidId']:
        assert not con.unregister(callback, arg)
        assert con.register(callback, arg)
        assert not con.register(callback, arg)
        assert con.unregister(callback, arg)
        assert not con.unregister(callback, arg)
    with pytest.raises(AssertionError):
        con.register(callback, 'NextValidId')

def test_basic():
    seen = {}
    def callback(msg):
        seen[type(msg).__name__] = msg

    con = Connection(TWS_HOST, TWS_PORT, TWS_CLID)
    assert con.registerAll(callback)

    assert not con.disconnect()
    assert con.connect()
    assert sleep_until(lambda: 'nextValidId' in seen, 1.0)
    assert seen['nextValidId'].orderId > 0

    con.reqCurrentTime()
    assert sleep_until(lambda: 'currentTime' in seen, 1.0)
    assert seen['currentTime'].time > 0

    assert con.disconnect()
    assert not con.disconnect()
