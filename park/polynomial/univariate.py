from __future__ import annotations
from functools import reduce

from typing import Iterator, List

from park.field.prime_field import PrimeFieldValue


class UnivariatePolynomial:
    """Univariate polynomial defined over a prime field."""

    def __init__(self, coeffs: List[PrimeFieldValue] = []):
        # Make sure that the coefficients are sampled from a prime field.
        if not all([isinstance(c, PrimeFieldValue) for c in coeffs]):
            raise ValueError("Coefficients must be sampled from a prime field")

        # The coefficient of `x^i` is stored at location `i` in the list.
        self.coeffs = coeffs

    def __repr__(self) -> str:
        terms = []
        for i, coeff in enumerate(self.coeffs):
            if i == 0:
                terms.append(str(coeff))
                continue

            # If the coefficient is zero, don't print it.
            if coeff == 0:
                continue

            # If the degree (i) is one, don't print the exponent.
            if i == 1:
                terms.append(f"{coeff}x" if coeff != 1 else "x")
                continue

            # If a value is one, only print the variable.
            if coeff == 1:
                terms.append(f"x^{i}")
            else:
                terms.append(f"{coeff}x^{i}")

        return " + ".join(terms)

    def __len__(self) -> int:
        """The number of coefficients in the polynomial. To get
        the degree, use the degree property.

        Returns:
            int: The number of coefficients of the polynomial.
        """
        return len(self.coeffs)

    def __iter__(self) -> Iterator[PrimeFieldValue]:
        return iter(self.coeffs)

    def __call__(self, __value: PrimeFieldValue) -> PrimeFieldValue:
        """Evaluate the polynomial on an input via Horner's Method.

        Args:
            __value (int): The input

        Returns:
            PrimeFieldValue: The polynomial evaluation.
        """
        return reduce(
            lambda acc, cur: acc + cur[1] * (__value ** cur[0]), enumerate(self.coeffs), PrimeFieldValue(0, self.p)
        )

    @property
    def p(self):
        return self.coeffs[0].p if len(self) > 0 else 0

    @property
    def degree(self):
        return len(self) - 1 if len(self) > 0 else 0
