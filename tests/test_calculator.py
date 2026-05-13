from calculator import add, sqre, sub, divide, multiply, modulo


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(8, 2) == 4
    assert divide(20, 10) == 2


def test_sqre():
    assert sqre(5) == 25
    assert sqre(0) == 0


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(8, 2) == 0
