from __future__ import print_function
import collections
import inspect
import os
import sys
import time

from twspy.ib.EClientSocket import EClientSocket
from twspy.ib.EWrapper import EWrapper

TWS_HOST = os.environ.get('TWS_HOST', '127.0.0.1')
TWS_PORT = int(os.environ.get('TWS_PORT', 7496))
TWS_CLID = int(os.environ.get('TWS_CLID', 0))

def test_client():
    functions = {}
    predicate = inspect.ismethod if sys.version_info[0] < 3 else inspect.isfunction
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
    con.eConnect(TWS_HOST, TWS_PORT, TWS_CLID)
    assert con.isConnected()
    for i in range(10):
        if 'nextValidId' in seen:
            break
        time.sleep(0.1)
    assert seen['nextValidId']['orderId'] > 0
    con.eDisconnect()
    assert not con.isConnected()
