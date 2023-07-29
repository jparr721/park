from __future__ import annotations

import random


def extended_gcd(a, b):
    """
    Extended Euclidean algorithm to find gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b).
    Returns gcd(a, b), x, y.
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


class PrimeFieldValue:
    def __init__(self, value: int, p: int):
        self.__value = value % p
        self.__p = p

    def __add__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return PrimeFieldValue(self.__value + other.__value, self.__p)
        return PrimeFieldValue(self.__value + other, self.__p)

    def __sub__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return PrimeFieldValue(self.__value - other.__value, self.__p)
        return PrimeFieldValue(self.__value - other, self.__p)

    def __mul__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return PrimeFieldValue(self.__value * other.__value, self.__p)
        return PrimeFieldValue(self.__value * other, self.__p)

    def __truediv__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            # Modular inverse using extended Euclidean algorithm
            def mod_inv(a, m):
                g, x, y = extended_gcd(a, m)
                return x % m

            if other.__value == 0:
                raise ZeroDivisionError("Division by zero")
            inv = mod_inv(other.__value, self.__p)
            return PrimeFieldValue(self.__value * inv, self.__p)
        return PrimeFieldValue(self.__value // other, self.__p)

    def __mod__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            if other.__value == 0:
                raise ZeroDivisionError("Modulo by zero")
            return PrimeFieldValue(self.__value % other.__value, self.__p)
        if other == 0:
            raise ZeroDivisionError("Modulo by zero")
        return PrimeFieldValue(self.__value % other, self.__p)

    def __pow__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return PrimeFieldValue(self.__value**other.__value, self.__p)

        return PrimeFieldValue(self.__value**other, self.__p)

    def __eq__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return self.__value == other.__value

        return self.__value == other

    def __ne__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return self.__value != other.__value

        return self.__value != other

    def __lt__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return self.__value < other.__value

        return self.__value < other

    def __le__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return self.__value <= other.__value

        return self.__value <= other

    def __gt__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return self.__value > other.__value

        return self.__value > other

    def __ge__(self, other: int | PrimeFieldValue):
        if isinstance(other, PrimeFieldValue):
            return self.__value >= other.__value

        return self.__value >= other

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return f"FieldValueModP({self.__value}, {self.__p})"


class PrimeField:
    def __init__(self, p: int):
        self.p = p

        # The values of the finite field
        self.__vals = list(range(self.p))

    def __len__(self):
        return self.p

    def __call__(self, __value: int) -> int:
        return __value % self.p

    def sample(self) -> int:
        """Sample randomly from the finite field

        Returns:
            int: The random sample.
        """
        return random.choice(self.__vals)
