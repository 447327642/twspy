import pytest

from twspy import Connection

from .support import config, sleep_until


@pytest.fixture
def con(request):
    con = Connection(*config)
    con.enableLogging()
    request.addfinalizer(lambda: con.close())
    return con

def test_dispatcher():
    from twspy import Dispatcher
    from twspy.ib.EWrapper import EWrapper
    assert set(dir(Dispatcher)) - set(dir(EWrapper)) == {'_dispatch'}

def test_constructor():
    assert Connection() is not None
    assert Connection(clientId=0) is not None
    assert Connection(host='test', port=12345, clientId=0) is not None
    assert Connection(host='test', port=12345, clientId=0, exceptions='raise') is not None

def test_register():
    def callback(msg): pass
    con = Connection()

    with pytest.raises(ValueError):
        con.unregister('nextValidId', callback)
    con.register('nextValidId', callback)
    with pytest.raises(ValueError):
        con.register('nextValidId', callback)
    assert callback in con.getListeners('nextValidId')
    con.unregister('nextValidId', callback)
    with pytest.raises(ValueError):
        con.unregister('nextValidId', callback)

    with pytest.raises(KeyError):
        con.getListeners(123)
    for func in [con.register, con.unregister]:
        with pytest.raises(KeyError):
            func(123, callback)
        with pytest.raises(KeyError):
            func('NextValidId', callback)
        with pytest.raises(TypeError):
            func('nextValidId', 'test')

def test_decorator():
    con = Connection()
    @con.listener('nextValidId', 'openOrderEnd', exceptions='raise')
    def callback(msg):
        pass
    assert callback in con.getListeners('nextValidId')

def test_attributes_before_connect():
    con = Connection()
    assert not con.isConnected()

def test_basic(con, capsys):
    seen = {}
    def callback(msg):
        seen[type(msg).__name__] = msg

    con.registerAll(callback)

    assert not con.isConnected()
    con.connect()
    assert sleep_until(lambda: 'nextValidId' in seen, 1.0)
    assert seen['nextValidId'].orderId > 0

    con.reqCurrentTime()
    assert sleep_until(lambda: 'currentTime' in seen, 1.0)
    assert seen['currentTime'].time > 0

    assert con.isConnected()
    con.close()
    assert not con.isConnected()
    con.enableLogging(False)

    out, err = capsys.readouterr()
    assert 'currentTime' in err

def test_connect_multiple(con):
    def callback(msg):
        seen.append(True)
    con.register('nextValidId', callback)
    for i in range(2):
        seen = []
        con.connect()
        assert con.isConnected()
        assert sleep_until(lambda: seen, 1.0)
        con.close()
        assert not con.isConnected()

def test_modify_msg(con):
    def callback1(msg):
        return "test"
    def callback2(msg):
        assert msg == "test"
        seen.append(True)

    seen = []
    con.register('nextValidId', callback1)
    con.register('nextValidId', callback2)
    con.connect()
    assert sleep_until(lambda: seen, 1.0)

def test_exception_in_handler(con):
    def callback(msg):
        seen.append(True)
        raise Exception('test')

    for options in [{}, {'exceptions': 'raise'}]:
        seen = []
        con.register('nextValidId', callback, **options)
        con.connect()
        assert sleep_until(lambda: seen, 1.0)
        assert not con.isConnected()
        con.unregister('nextValidId', callback)

    seen = []
    con.register('nextValidId', callback, exceptions='unregister')
    con.connect()
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

    con.register('historicalData', callback)
    con.register('error', error)
    con.connect()

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

def test_failing_request(con):
    from twspy.ib.EClientErrors import EClientErrors
    seen = []
    def callback(msg):
        seen.append(msg)
    con.register('error', callback)
    con.connect()
    con.m_dos.close()
    con.reqScannerParameters()
    # reader thread might fail first, check all errors
    for msg in seen:
        if msg.errorCode == EClientErrors.FAIL_SEND_REQSCANNERPARAMETERS.m_errorCode:
            return
    assert False

def test_callback_extra_args(con):
    seen = []
    def callback(msg, arg):
        seen.append(arg)
    con.register('nextValidId', callback, con)
    con.connect()
    assert sleep_until(lambda: seen, 1.0)
    assert seen[0] is con
