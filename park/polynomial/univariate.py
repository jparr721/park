from typing import List, Tuple

from park.field.prime_field import PrimeFieldValue


class UnivariatePolynomial:
    """Univariate polynomial defined over a prime field."""

    def __init__(self, coeffs: List[PrimeFieldValue] | Tuple[PrimeFieldValue] = ()):
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
                terms.append(f"{coeff}x")
                continue

            # If a value is one, only print the variable.
            if coeff == 1:
                terms.append(f"x^{i}")
                continue
            else:
                terms.append(f"{coeff}x^{i}")

        return " + ".join(terms[::-1])

    def __len__(self) -> int:
        """The number of coefficients in the polynomial. To get
        the degree, use the degree property.

        Returns:
            int: The number of coefficients of the polynomial.
        """
        return len(self.coeffs)

    # def __call__(self, __value: PrimeFieldValue) -> PrimeFieldValue:
    #     """Evaluate the polynomial on an input. Not suitable for SNARKs.

    #     Args:
    #         __value (int): The input

    #     Returns:
    #         int: The polynomial evaluation.
    #     """
    #     return sum([c * __value ** (self.degree - i) for i, c in enumerate(self.coeffs)])

    @property
    def degree(self):
        return len(self) - 1 if len(self) > 0 else 0
