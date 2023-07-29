from park.field.finite_field import FieldValue


def test_addition():
    a = FieldValue(5)
    b = FieldValue(7)
    c = a + b
    assert c == 12


def test_subtraction():
    a = FieldValue(10)
    b = FieldValue(3)
    c = a - b
    assert c == 7


def test_multiplication():
    a = FieldValue(3)
    b = FieldValue(4)
    c = a * b
    assert c == 12


def test_division():
    a = FieldValue(10)
    b = FieldValue(2)
    c = a / b
    assert c == 5


def test_modulus():
    a = FieldValue(15)
    b = FieldValue(4)
    c = a % b
    assert c == 3


def test_power():
    a = FieldValue(2)
    b = FieldValue(3)
    c = a**b
    assert c == 8


def test_comparison():
    a = FieldValue(5)
    b = FieldValue(8)
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    assert a == 5
    assert a != 8


def test_str_representation():
    a = FieldValue(10)
    assert str(a) == "10"


def test_repr_representation():
    a = FieldValue(15)
    assert repr(a) == "FieldValue(15)"
