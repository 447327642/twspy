import pytest

from twspy import Connection, message

from .support import config, sleep_until

@pytest.fixture
def con(request):
    con = Connection(*config)
    con.enableLogging()
    request.addfinalizer(lambda: con.disconnect())
    return con

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
        assert callback in con.getListeners(arg)
        assert con.unregister(callback, arg)
        assert not con.unregister(callback, arg)
    with pytest.raises(ValueError):
        con.register(callback, 'NextValidId')

def test_attributes_before_connect():
    con = Connection()
    assert not con.isConnected()

def test_basic(con, capsys):
    seen = {}
    def callback(msg):
        seen[type(msg).__name__] = msg

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
    assert not con.enableLogging(False)

    out, err = capsys.readouterr()
    assert 'currentTime' in err

def test_connect_multiple(con):
    def callback(msg):
        seen.append(True)
    assert con.register(callback, 'nextValidId')
    for i in range(2):
        seen = []
        assert con.connect()
        assert con.isConnected()
        assert sleep_until(lambda: seen, 1.0)
        assert con.disconnect()
        assert not con.isConnected()

def test_exception_in_handler(con):
    def callback(msg):
        seen.append(True)
        raise Exception('test')

    for options in [{}, {'exceptions': 'raise'}]:
        seen = []
        assert con.register(callback, 'nextValidId', **options)
        assert con.connect()
        assert sleep_until(lambda: seen, 1.0)
        assert not con.isConnected()
        assert not con.disconnect()
        assert con.unregister(callback, 'nextValidId')

    seen = []
    assert con.register(callback, 'nextValidId', exceptions='unregister')
    assert con.connect()
    assert sleep_until(lambda: seen, 1.0)
    assert con.isConnected()
    assert callback not in con.getListeners('nextValidId')

def test_historical_data(con):
    import time
    from twspy.ib.Contract import Contract

    seen = []
    def callback(msg):
        if msg.date.startswith('finished'):
            seen.append(True)
    def error(msg):
        if msg.errorCode == 2105:
            seen.append(msg)

    assert con.register(callback, 'historicalData')
    assert con.register(error, 'error')
    assert con.connect()

    c = Contract()
    c.m_symbol = 'AAPL'
    c.m_secType = 'STK'
    c.m_exchange = 'SMART'
    c.m_primaryExch = 'NYSE'
    e = time.strftime('%Y%m%d %H:%M:%S')
    con.reqHistoricalData(1, c, e, "5 D", "1 hour", "TRADES", 1, 1, None)

    assert sleep_until(lambda: seen, 5.0)
    if seen[0] is not True:
        pytest.xfail(seen[0].errorMsg)
    assert con.disconnect()

def test_failing_request(con):
    from twspy.ib.EClientErrors import EClientErrors
    seen = []
    def callback(msg):
        seen.append(msg)
    con.register(callback, 'error')
    assert con.connect()
    con.m_dos.close()
    con.reqScannerParameters()
    # reader thread might fail first, check all errors
    for msg in seen:
        if msg.errorCode == EClientErrors.FAIL_SEND_REQSCANNERPARAMETERS.m_errorCode:
            return
    assert False
