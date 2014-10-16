import pytest

from twspy import Connection, message

from .support import config, sleep_until

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

def test_basic(capsys):
    seen = {}
    def callback(msg):
        seen[type(msg).__name__] = msg

    con = Connection(*config)
    assert con.registerAll(callback)
    assert con.enableLogging()

    assert not con.disconnect()
    assert con.connect()
    assert sleep_until(lambda: 'nextValidId' in seen, 1.0)
    assert seen['nextValidId'].orderId > 0

    con.reqCurrentTime()
    assert sleep_until(lambda: 'currentTime' in seen, 1.0)
    assert seen['currentTime'].time > 0

    assert con.disconnect()
    assert not con.disconnect()
    assert not con.enableLogging(False)

    out, err = capsys.readouterr()
    assert 'currentTime' in err

def test_exception_in_handler():
    seen = []
    def callback(msg):
        seen.append(True)
        raise Exception('test')

    con = Connection(*config)
    assert con.register(callback, 'nextValidId')

    assert con.connect()
    assert sleep_until(lambda: seen, 1.0)
    assert not con.isConnected()
    assert not con.disconnect()
    assert con.unregister(callback, 'nextValidId')
