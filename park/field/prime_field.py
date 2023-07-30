from __future__ import annotations

import random

from sympy import isprime
from typing import List


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
        if not isprime(p):
            raise ValueError("p must be prime")

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
                _, x, _ = extended_gcd(a, m)
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
        return f"{self.__class__.__name__}(p={self.__p}, value={self.__value})"

    def __hash__(self):
        return hash(self.__value)

    @property
    def is_zero(self):
        return self.__value == 0


class PrimeField:
    def __init__(self, p: int):
        if not isprime(p):
            raise ValueError("p must be prime")
        self.p = p

        # The values of the finite field
        self.__vals = [PrimeFieldValue(i, p) for i in range(p)]

    def __len__(self):
        return self.p

    def __call__(self, __value: int) -> PrimeFieldValue:
        return PrimeFieldValue(__value, self.p)

    def __repr__(self):
        return f"{self.__class__.__name__}(p={self.p}, vals={{{','.join([str(v) for v in self.__vals])}}})"

    def __str__(self):
        return repr(self)

    def __getitem__(self, __index: int) -> PrimeFieldValue:
        return self.__vals[__index]

    def sample(self, n: int | None = None) -> PrimeFieldValue | List[PrimeFieldValue]:
        """Sample randomly from the finite field

        Returns:
            PrimeFieldValue: The random sample.
        """
        if n is not None:
            if n > self.p:
                raise ValueError("n must be less than the size of the field")

            return random.sample(self.__vals, n)

        return random.choice(self.__vals)
