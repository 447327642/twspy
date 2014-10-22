import pytest

from twspy import Connection

from .support import config, HAS_TWS, sleep_until


@pytest.fixture
def con(request):
    con = Connection(*config)
    con.enableLogging()
    request.addfinalizer(lambda: con.close())
    return con


class TestBasic:
    def test_version(self):
        import re
        from twspy import __version__
        assert re.match('[0-9]+\.[0-9]+\.[0-9]+', __version__)

    def test_messages(self):
        from twspy import messages
        assert 'error_0' not in messages
        assert 'nextValidId' in messages
        assert issubclass(messages['error'], tuple)

    def test_dispatcher(self):
        from twspy import Dispatcher
        from twspy.ib.EWrapper import EWrapper
        assert set(dir(Dispatcher)) - set(dir(EWrapper)) == {'_dispatch'}

    def test_connection_attributes(self, con):
        assert not con.isConnected()

    def test_register_decorator(self, con):
        @con.listener('nextValidId', 'openOrderEnd', exceptions='raise')
        def callback(msg):
            pass
        assert callback in con.getListeners('nextValidId')
        assert callback in con.getListeners('openOrderEnd')

    def test_register_unregister(self, con):
        callback = lambda msg: None

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

    def test_register_extra_args(self, con):
        seen = []
        callback = lambda msg, arg: seen.append(arg)
        con.register('nextValidId', callback, con)
        con.client.wrapper().nextValidId(42)
        assert sleep_until(lambda: seen, 1.0)
        assert seen[0] is con

    def test_modify_msg(self, con):
        def callback1(msg):
            return "test"

        def callback2(msg):
            assert msg == "test"
            seen.append(True)

        seen = []
        con.register('nextValidId', callback1)
        con.register('nextValidId', callback2)
        con.client.wrapper().nextValidId(42)
        assert sleep_until(lambda: seen, 1.0)

    def test_logging(self, con, capsys):
        con.wrapper().error("test1")
        con.enableLogging()
        con.wrapper().error(Exception("test2"))
        con.enableLogging(False)
        con.wrapper().error("test3")
        out, err = capsys.readouterr()
        assert err.splitlines() == [
            "error(id=None, errorCode=None, errorMsg='test1')",
            "error(id=None, errorCode=None, errorMsg=Exception('test2',))",
        ]

    def test_failing_request(self, con):
        from twspy.ib.EClientErrors import EClientErrors
        seen = []
        callback = lambda msg: seen.append(msg)
        con.register('error', callback)
        # fake a connection
        con.client.m_connected = True
        con.client.m_serverVersion = 42
        con.reqScannerParameters()
        expected = EClientErrors.FAIL_SEND_REQSCANNERPARAMETERS.m_errorCode
        # reader thread might fail first, check all errors
        for msg in seen:
            if msg.errorCode == expected:
                return
        assert False, seen


@pytest.mark.xfail(not HAS_TWS, reason="no TWS", raises=IOError)
class TestConnected:
    def test_connect_multiple(self, con):
        def callback(msg):
            seen.append(True)
        con.register('nextValidId', callback)

        for i in range(2):
            seen = []
            con.connect()
            assert con.isConnected()
            assert sleep_until(lambda: seen, 1.0)

            reader = con.reader()
            con.close()
            assert not con.isConnected()
            assert sleep_until(lambda: not reader.is_alive(), 1.0)

    def test_basic_requests(self, con):
        from twspy.ib.ExecutionFilter import ExecutionFilter

        def callback(msg):
            seen[type(msg).__name__] = msg

        seen = {}
        con.registerAll(callback)

        con.connect()
        assert sleep_until(lambda: 'nextValidId' in seen, 1.0)
        assert seen['nextValidId'].orderId > 0

        con.reqCurrentTime()
        assert sleep_until(lambda: 'currentTime' in seen, 1.0)
        assert seen['currentTime'].time > 0

        con.reqAccountUpdates(True, '')
        assert sleep_until(lambda: 'accountDownloadEnd' in seen, 1.0)

        con.reqExecutions(1, ExecutionFilter)
        assert sleep_until(lambda: 'execDetailsEnd' in seen, 1.0)

    def test_historical_data(self, con):
        import time
        from twspy.ib.Contract import Contract

        def callback(msg):
            if msg.date.startswith('finished'):
                seen.append(True)

        def error(msg):
            if msg.errorCode == 2105:
                seen.append(msg)

        seen = []
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

    def test_exception_in_handler_register(self, con):
        def callback(msg):
            seen.append(True)
            raise Exception('test')

        def error(msg):
            errors.append(msg)

        con.register('error', error)
        for options in [{}, {'exceptions': 'raise'}]:
            seen = []
            errors = []
            con.register('nextValidId', callback, **options)
            con.connect()
            assert sleep_until(lambda: errors, 1.0)
            assert type(errors[0].errorMsg) is Exception
            assert str(errors[0].errorMsg) == 'test'
            assert not con.isConnected()
            con.unregister('nextValidId', callback)
        con.unregister('error', error)

        seen = []
        con.register('nextValidId', callback, exceptions='unregister')
        con.connect()
        assert sleep_until(lambda: seen, 1.0)
        assert con.isConnected()
        assert callback not in con.getListeners('nextValidId')

    def test_exception_in_handler_constructor(self, request, capsys):
        def callback(msg):
            seen.append(True)
            raise Exception('test')

        seen = []
        con = Connection(*config, exceptions='pass')
        request.addfinalizer(lambda: con.close())
        con.register('nextValidId', callback)
        con.connect()
        assert sleep_until(lambda: seen, 1.0)
        assert con.isConnected()
        assert callback in con.getListeners('nextValidId')

        out, err = capsys.readouterr()
        assert 'Traceback' in err
        assert 'callback' in err
