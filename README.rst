twspy
=====
.. image:: https://travis-ci.org/bdkearns/twspy.svg?branch=master
    :target: https://travis-ci.org/bdkearns/twspy

twspy is an unofficial Python implementation of the Interactive Brokers Trader Workstation API. It is similar to ibpy in that it uses java2python to translate the official Java API to Python. On top of the standard API, a new implementation of a "Pythonic" wrapper is included.

Reasons to use twspy
--------------------
- Implements TWS API 971.01
- Generated using an updated version of java2python instead of manually applied changes
- Supports both Python 2.6+ and Python 3.2+
- Simpler implementation of the "Pythonic" wrapper
- Tested using added test suite based on pytest

Design changes in new wrapper
-----------------------------
- Exceptions are used to indicate errors instead of return values.
- Message names are validated during register/unregister to avoid silent errors.
- Messages are represented using namedtuples rather than regular class instances.
- Exceptions in callbacks aren't swallowed with a log message by default. Instead they are left alone, allowing them to pass back to the TWS API resulting in a disconnect. To get a different behavior, specify the 'exceptions' option when creating a connection or registering a listener.

Using twspy
-----------
.. code-block:: python

    from twspy import Connection
    con = Connection(host, port, clientId)

    @con.listener('nextValidId')
    def my_callback(msg):
        assert msg.orderId > 0

    def my_other_callback(msg, extra):
        assert extra == 123
    con.register('openOrder', my_other_callback, 123, exceptions='unregister')

    con.connect()
    ...
