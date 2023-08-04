"""Testing only
"""

from park.field.prime_field import PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial

if __name__ == "__main__":
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(1, p)])
    # u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(0, p)])

    for i in range(p):
        print(u(PrimeFieldValue(i, p)))
