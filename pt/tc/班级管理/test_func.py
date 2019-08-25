def add1(x):
    return x+1

class TestCase:
    def test_add1(self):
        assert add1(3)==4

    def test_add2(self):
        assert add1(1)==4