from __future__ import print_function
import inspect
import os
import sys

from twspy.ib.EClientSocket import EClientSocket
from twspy.ib.EWrapper import EWrapper

TWS_HOST = os.environ.get('TWS_HOST', '127.0.0.1')
TWS_PORT = int(os.environ.get('TWS_PORT', 7496))
TWS_CLID = int(os.environ.get('TWS_CLID', 0))

def test_client():
    predicate = inspect.ismethod if sys.version_info[0] < 3 else inspect.isfunction
    functions = [name for name, func in inspect.getmembers(EWrapper, predicate)]
    functions.append('error')

    class MyWrapper(EWrapper):
        def make(name):
            def default(self, *args):
                print(name, *args)
            return default

        for name in functions:
            locals()[name] = make(name)

    con = EClientSocket(MyWrapper())
    con.eConnect(TWS_HOST, TWS_PORT, TWS_CLID)
    assert con.isConnected()
    con.eDisconnect()
    assert not con.isConnected()
