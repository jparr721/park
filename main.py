"""Testing only
"""

from park.field.prime_field import PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial
from park.polynomial.extension import UnivariateExtensionPolynomial

if __name__ == "__main__":
    p = 11
    u1 = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(1, p)])
    u2 = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(0, p)])

    ue1 = UnivariateExtensionPolynomial(u1, p)
    for i in range(p):
        print(ue1(PrimeFieldValue(i, p)))
