import pytest

from park.field.prime_field import PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial


@pytest.fixture
def coeffs():
    return [PrimeFieldValue(value=1, p=5), PrimeFieldValue(value=4, p=5), PrimeFieldValue(value=2, p=5)]


def test_univariate_polynomial_init(coeffs):
    u = UnivariatePolynomial(coeffs)

    assert u is not None
    assert u.coeffs == coeffs


def test_univariate_polynomial_init_fails_when_not_prime():
    with pytest.raises(ValueError):
        UnivariatePolynomial([1, 2, 3])  # type: ignore


def test_zero_univariate_polynomial_init():
    u = UnivariatePolynomial()

    assert u is not None
    assert u.coeffs == []
    assert u.degree == 0


def test_univariate_polymial_repr():
    coeffs = [PrimeFieldValue(1, 5), PrimeFieldValue(2, 5), PrimeFieldValue(3, 5)]
    u = UnivariatePolynomial(coeffs)
    assert repr(u) == "1 + 2x + 3x^2"


def test_univariate_polynomial_degree(coeffs):
    u = UnivariatePolynomial(coeffs)
    assert u.degree == len(coeffs) - 1


def test_univariate_evaluation1():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(1, p)])
    evals = [u(PrimeFieldValue(i, p)) for i in range(p)]

    # Taken from Thaler's book. There is a typo in his, the second to last
    # value should be 4, not 0 in Figure 2.1.
    assert evals == [2, 4, 8, 3, 0, 10, 0, 3, 8, 4, 2]


def test_univariate_evaluation2():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(0, p)])
    evals = [u(PrimeFieldValue(i, p)) for i in range(p)]
    assert evals == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1]
