from twspy.lang.python import overloaded


class TestOverloading():
    def test_simple(self):
        @overloaded
        def func(arg):
            return "default"

        @func.register(int)
        def func_int(arg):
            return "int"

        assert func('abc') == "default"
        assert func(0.5) == "default"
        assert func(None) == "default"
        assert func(123) == "int"

    def test_complex(self):
        @overloaded
        def func(arg):
            return "default"

        @func.register(int, int)
        def func_int(arg1, arg2):
            return "int"

        @func.register(int, float)
        def func_mixed(arg1, arg2):
            return "mixed"

        class sub(int):
            pass

        @func.register(sub, sub)
        def func_sub(arg1, arg2):
            return "sub"

        assert func('abc') == "default"
        assert func(123) == "default"
        assert func(None) == "default"
        assert func(123, 123) == "int"
        assert func(None, 123) == "int"
        assert func(None, 0.5) == "mixed"
        assert func(None, sub(123)) == "sub"
        assert func(123, sub(123)) == "int"
        assert func(sub(123), sub(123)) == "sub"
