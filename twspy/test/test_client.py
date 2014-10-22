from __future__ import print_function

import collections
import inspect
import sys

import pytest

from twspy.ib.EClientSocket import EClientSocket
from twspy.ib.EWrapper import EWrapper
from twspy.ib.ExecutionFilter import ExecutionFilter

from .support import config, HAS_TWS, sleep_until


@pytest.mark.xfail(not HAS_TWS, reason="no TWS", raises=IOError)
def test_client():
    functions = {}
    predicate = (inspect.ismethod if sys.version_info[0] < 3
                 else inspect.isfunction)
    for name, func in inspect.getmembers(EWrapper, predicate):
        functions[name] = inspect.getargspec(func).args[1:]
    functions['error'] = ['id', 'errorCode', 'errorMsg']

    seen = {}

    class MyWrapper(EWrapper):
        def make(name, spec):
            def default(self, *args):
                print(name, *args)
                assert len(spec) == len(args)
                values = collections.OrderedDict(zip(spec, args))
                seen[name] = values
            return default

        for name, spec in functions.items():
            locals()[name] = make(name, spec)

    con = EClientSocket(MyWrapper())
    con.eConnect(*config)
    if not con.isConnected():
        raise IOError

    assert sleep_until(lambda: 'nextValidId' in seen, 1.0)
    assert seen['nextValidId']['orderId'] > 0

    con.reqCurrentTime()
    assert sleep_until(lambda: 'currentTime' in seen, 1.0)
    assert seen['currentTime']['time'] > 0

    con.reqAccountUpdates(True, '')
    assert sleep_until(lambda: 'accountDownloadEnd' in seen, 1.0)

    con.reqExecutions(1, ExecutionFilter)
    assert sleep_until(lambda: 'execDetailsEnd' in seen, 1.0)

    reader = con.reader()
    con.eDisconnect()
    assert not con.isConnected()
    assert sleep_until(lambda: not reader.is_alive(), 1.0)
