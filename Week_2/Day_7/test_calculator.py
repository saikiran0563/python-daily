import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(5, 0) == 5


def test_add_negative():
    assert add(-2, 3) == 1

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert divide(10, 0)


        