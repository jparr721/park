from park.field.prime_field import PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial
from park.polynomial.extension import UnivariateExtensionPolynomial


def test_univariate_extension_init():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(1, p)])
    ue = UnivariateExtensionPolynomial(u, p)
    assert ue is not None


def test_univariate_extension_eval1():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(1, p)])

    ue = UnivariateExtensionPolynomial(u, p)
    evals = [ue(PrimeFieldValue(i, p)) for i in range(p)]

    # Taken from Thaler's book Figure 2.2
    assert evals == [2, 1, 1, 2, 4, 7, 0, 5, 0, 7, 4]


def test_univariate_extension_eval2():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(0, p)])

    ue = UnivariateExtensionPolynomial(u, p)
    evals = [ue(PrimeFieldValue(i, p)) for i in range(p)]

    # Taken from Thaler's book Figure 2.2
    assert evals == [2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3]
