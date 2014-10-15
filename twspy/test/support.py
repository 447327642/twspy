import time

def sleep_until(func, secs):
    start = time.time()
    while not func():
        if time.time() - start >= secs:
            return False
        time.sleep(0.1)
    return True
