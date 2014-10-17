twspy
=====
twspy is an unofficial Python implementation of the Interactive Brokers Trader Workstation API. It is similar to ibpy in that it uses java2python to translate the official Java API to Python. On top of the standard API, a new implementation of a "Pythonic" wrapper is included.

Reasons to use twspy
--------------------
- Implements TWS API 971.01
- Generated using an updated fork of java2python instead of manually applied changes
- Supports both Python 2.x and Python 3.x
- Simpler implementation of the "Pythonic" wrapper
- Tested using added test suite based on pytest

Design changes in new wrapper
-----------------------------
- Message names are validated during register/unregister to avoid silent errors.
- Messages are represented using namedtuples rather than regular class instances.
- Exceptions in callbacks aren't swallowed with a log message by default. Instead they are left alone, allowing them to pass back to the TWS API resulting in a disconnect. If you want a different behavior, you can write a wrapper for your callbacks that swallows/handles exceptions.

Using twspy
-----------
.. code-block:: python

    from twspy import Connection, message
    con = Connection(host, port, client_id)
    def my_callback(msg):
        assert msg.orderId > 0
    con.register(message.nextValidId, my_callback)
    con.connect()
    ...

See ``twspy/test/test_api.py`` for additional examples.

Additionally, one can use the TWS API without the "Pythonic" wrapper. See ``twspy/test/test_client.py`` for examples.

Note: in TWS API 971.01, many EClientSocket request methods now require an additional options parameter which can be None.

Using the ibpy compatibility wrapper
------------------------------------
If you want to stick with the ibpy design choices, you can use the optional wrapper, which should act as a drop-in replacement.

.. code-block:: python

    from ib.opt import ibConnection, message ->
    from twspy.opt import ibConnection, message

    from ib.ext.{} import {} ->
    from twspy.ib.{} import {}
