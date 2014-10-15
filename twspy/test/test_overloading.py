# http://svn.python.org/projects/sandbox/trunk/overload/test_overloading.py

"""Unit tests for overloading.py."""

import unittest

from twspy.lang.overloading import overloaded

__metaclass__ = type # New-style classes by default

# Helper classes
class List(list):
    pass
class SubList(List):
    pass

# Sample test data
test_data = (
    "this is a string", [1, 2, 3, 4], ("more tuples",
    1.0, 2.3, 4.5), "this is yet another string", (99,)
    )

class OverloadingTests(unittest.TestCase):

    def test_1(self):
        @overloaded
        def pprint(obj):
            return repr(obj)
        @pprint.register(List)
        @pprint.register(list)
        def pprint_list(obj):
            if not obj:
                return "[]"
            s = "["
            for item in obj:
                s += pprint(item).replace("\n", "\n ") + ",\n "
            return s[:-3] + "]"
        @pprint.register(tuple)
        def pprint_tuple(obj):
            if not obj:
                return "()"
            s = "("
            for item in obj:
                s += pprint(item).replace("\n", "\n ") + ",\n "
            if len(obj) == 1:
                return s[:-2] + ")"
            return s[:-3] + ")"
        @pprint.register(dict)
        def pprint_dict(obj):
            if not obj:
                return "{}"
            s = "{"
            for key, value in obj.iteritems():
                s += (pprint(key).replace("\n", "\n ") + ": " +
                      pprint(value).replace("\n", "\n ") + ",\n ")
            return s[:-3] + "}"
        @pprint.register(set)
        def pprint_set(obj):
            if not obj:
                return "{/}"
            s = "{"
            for item in obj:
                s += pprint(item).replace("\n", "\n ") + ",\n "
            return s[:-3] + "}"
        # This is not a very good test
        a = pprint(test_data)
        b = pprint(List(test_data))
        c = pprint(SubList(test_data))
        self.assertEqual(a[1:-1], b[1:-1])
        self.assertEqual(b, c)

    def test_2(self):
        class A: pass
        class B: pass
        class C(A, B): pass
        def defaultfoo(x, y): return "default"
        @overloaded
        def foo(x, y): return defaultfoo(x, y)
        @foo.register(A, B)
        def fooAB(x, y): return "AB"
        @foo.register(A, C)
        def fooAC(A, C): return "AC"
        @foo.register(B, A)
        def fooBA(x, y): return "BA"
        @foo.register(C, B)
        def fooCB(x, y): return "CB"

        self.assertEqual(foo(A(), A()), "default")
        self.assertEqual(foo(A(), B()), "AB")
        self.assertEqual(foo(A(), C()), "AC")
        self.assertEqual(foo(A(), 123), "default")

        self.assertEqual(foo(B(), A()), "BA")
        self.assertEqual(foo(B(), B()), "default")
        self.assertEqual(foo(B(), C()), "BA")
        self.assertEqual(foo(B(), 123), "default")

        self.assertEqual(foo(C(), A()), "BA")
        self.assertEqual(foo(C(), B()), "CB")
        self.assertRaises(TypeError, foo, C(), C())
        self.assertEqual(foo(C(), 123), "default")

        self.assertEqual(foo("x", A()), "default")
        self.assertEqual(foo("x", B()), "default")
        self.assertEqual(foo("x", C()), "default")
        self.assertEqual(foo("x", 123), "default")

    def test_3(self):
        # Ensure that you can use @overloaded for regular methods
        class C:
            @overloaded
            def whatever(self, arg):
                return "whatever(%r)" % (arg,)
            @whatever.register(object, int)
            def whatever_int(self, arg):
                return "whatever(%x)" % arg
            @whatever.register(object, str)
            def whatever_str(self, arg):
                return "whatever(%s)" % arg
        a = C()
        self.assertEqual(a.whatever(10), "whatever(a)")
        self.assertEqual(a.whatever("abc"), "whatever(abc)")
        self.assertEqual(a.whatever([1]), "whatever([1])")
        self.assertEqual(C.whatever(a, 10), "whatever(a)")


if __name__ == "__main__":
    unittest.main()
