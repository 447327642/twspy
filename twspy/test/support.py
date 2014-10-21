import os
import time
from collections import namedtuple

config = namedtuple('config', 'TWS_HOST TWS_PORT TWS_CLID')(
    os.environ.get('TWS_HOST', '127.0.0.1'),
    int(os.environ.get('TWS_PORT', 7496)),
    int(os.environ.get('TWS_CLID', 0)),
)

def sleep_until(func, secs):
    start = time.time()
    while not func():
        if time.time() - start >= secs:
            return False
        time.sleep(0.1)
    return True
