import os
import time
from collections import namedtuple

config = namedtuple('config', 'TWS_HOST TWS_PORT TWS_CLID')(
    os.environ.get('TWS_HOST', '127.0.0.1'),
    int(os.environ.get('TWS_PORT', 7496)),
    int(os.environ.get('TWS_CLID', 0)),
)


def check_for_tws():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((config.TWS_HOST, config.TWS_PORT))
    except socket.error:
        return False
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    return True

HAS_TWS = check_for_tws()


def sleep_until(func, secs):
    start = time.time()
    while not func():
        if time.time() - start >= secs:
            return False
        time.sleep(0.1)
    return True
