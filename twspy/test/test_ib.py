def test_version():
    import re
    from twspy.ib import __version__
    assert re.match('[0-9]{3}\.[0-9]{2}$', __version__)


def test_builder():
    from twspy.ib.Builder import Builder
    b = Builder()
    b.send(42)
    b.send("test")
    b.send(-0.5)
    b.send(True)
    assert b.getBytes() == b"42\x00test\x00-0.5\x001\x00"


def test_order_state():
    from twspy.ib.OrderState import OrderState
    o1 = OrderState()
    o2 = OrderState()
    assert o1 == o2
    o2.m_commission = 0.5
    assert o1 != o2


class TestUtil:
    def test_string_compare(self):
        from twspy.ib.Util import Util
        assert Util.StringCompare("test", "test") == 0
        assert Util.StringCompare("TEST", "test") == -1
        assert Util.StringCompare("test", "blah") == 1

        assert Util.StringCompareIgnCase("test", "test") == 0
        assert Util.StringCompareIgnCase("TEST", "test") == 0
        assert Util.StringCompareIgnCase("test", "blah") == 1
        assert Util.StringCompareIgnCase("BLAH", "test") == -1

    def test_vector_equals_unordered(self):
        from twspy.ib._lang.java import Vector
        from twspy.ib.Util import Util
        a = [42*100, 2, 5, 1]
        b = [1, 2, 5, 42*100]
        c = [1, 2]
        assert Util.VectorEqualsUnordered(a, a)
        assert Util.VectorEqualsUnordered(a, Vector(a))
        assert Util.VectorEqualsUnordered(a, b)
        assert Util.VectorEqualsUnordered(a, Vector(b))
        assert Util.VectorEqualsUnordered(b, a)
        assert not Util.VectorEqualsUnordered(a, c)
        assert not Util.VectorEqualsUnordered(b, c)
        assert not Util.VectorEqualsUnordered(b, Vector(c))

    def test_max_string(self):
        from twspy.ib._lang.java import Integer, Double
        from twspy.ib.Util import Util
        assert Util.IntMaxString(2) == "2"
        assert Util.IntMaxString(Integer.MAX_VALUE) == ""
        assert Util.DoubleMaxString(-0.5) == "-0.5"
        assert Util.DoubleMaxString(Double.MAX_VALUE) == ""
