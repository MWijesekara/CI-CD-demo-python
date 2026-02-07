from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2

def test_add_negative():
    assert add(-1, -1) == -2

def test_subtract_negative():
    assert subtract(-1, -1) == 0

def test_add_fail():
    assert add(2, 2) == 5  # This test is expected to fail

def test_new():
    assert subtract(2,2) == 3