import pytest

from park.field.prime_field import PrimeField, PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial


@pytest.fixture
def coeffs():
    pf = PrimeField(5)
    return pf.sample(3)


def test_univariate_polynomial_init(coeffs):
    u = UnivariatePolynomial(coeffs)

    assert u is not None
    assert u.coeffs == coeffs


def test_univariate_polynomial_init_fails_when_not_prime():
    with pytest.raises(ValueError):
        UnivariatePolynomial((1, 2, 3))


def test_zero_univariate_polynomial_init():
    u = UnivariatePolynomial()

    assert u is not None
    assert u.coeffs == ()
    assert u.degree == 0


def test_univariate_polymial_repr():
    coeffs = (PrimeFieldValue(1, 5), PrimeFieldValue(2, 5), PrimeFieldValue(3, 5))
    u = UnivariatePolynomial(coeffs)
    assert repr(u) == "3x^2 + 2x + 1"


def test_univariate_polynomial_degree(coeffs):
    u = UnivariatePolynomial(coeffs)
    assert u.degree == len(coeffs) - 1
