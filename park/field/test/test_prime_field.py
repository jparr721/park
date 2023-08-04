import pytest

from park.field.prime_field import PrimeFieldValue


def test_addition():
    p = 11
    a = PrimeFieldValue(5, p)
    b = PrimeFieldValue(7, p)
    c = a + b
    assert c == 1


def test_subtraction():
    p = 11
    a = PrimeFieldValue(10, p)
    b = PrimeFieldValue(3, p)
    c = a - b
    assert c == 7


def test_multiplication():
    p = 11
    a = PrimeFieldValue(3, p)
    b = PrimeFieldValue(4, p)
    c = a * b
    assert c == 1


def test_multiplication_int():
    p = 11
    a = PrimeFieldValue(3, p)
    b = 4
    c = a * b
    assert c == 1


def test_division():
    p = 11
    a = PrimeFieldValue(10, p)
    b = PrimeFieldValue(2, p)
    c = a / b
    assert c == 5


def test_division_by_zero():
    p = 11
    a = PrimeFieldValue(3, p)
    b = PrimeFieldValue(0, p)
    with pytest.raises(ZeroDivisionError):
        a / b


def test_modulus():
    p = 11
    a = PrimeFieldValue(15, p)
    b = PrimeFieldValue(4, p)
    c = a % b
    assert c == 0


def test_modulus_by_zero():
    p = 11
    a = PrimeFieldValue(3, p)
    b = 0
    with pytest.raises(ZeroDivisionError):
        a % b


def test_power():
    p = 11
    a = PrimeFieldValue(2, p)
    b = PrimeFieldValue(3, p)
    c = a**b
    assert c == 8


def test_comparison():
    p = 11
    a = PrimeFieldValue(5, p)
    b = PrimeFieldValue(8, p)
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    assert a == 5
    assert a != 8


def test_str_representation():
    p = 11
    a = PrimeFieldValue(10, p)
    assert str(a) == "10"


def test_repr_representation():
    p = 11
    a = PrimeFieldValue(15, p)
    assert repr(a) == "PrimeFieldValue(value=4, p=11)"
