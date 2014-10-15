def test_builder():
    from twspy.ib.Builder import Builder
    b = Builder()
    b.send(42)
    b.send("test")
    b.send(-0.5)
    b.send(True)
    assert b.getBytes() == b"42\x00test\x00-0.5\x001\x00"
