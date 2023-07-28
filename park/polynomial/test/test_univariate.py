from park.polynomial.univariate import UnivariatePolynomial


def test_univariate_polynomial_init():
    u = UnivariatePolynomial(1, 2, 3)

    assert u is not None
    assert u.coeffs == (1, 2, 3)


def test_zero_univariate_polynomial_init():
    u = UnivariatePolynomial()

    assert u is not None
    assert u.coeffs == ()
    assert u.degree == 0


def test_univariate_polymial_repr():
    u = UnivariatePolynomial(1, 2, 3)
    assert repr(u) == "3x^2 + 2x + 1"


def test_univariate_polynomial_degree():
    u = UnivariatePolynomial(1, 2, 3)
    assert u.degree == 2
