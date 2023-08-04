from park.polynomial.reed_solomon import compute_reed_soloman_evaluations
from park.field.prime_field import PrimeField, PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial


def test_univariate_evaluation1():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(1, p)])
    evals = [u(PrimeFieldValue(i, p)) for i in range(p)]

    # Taken from Thaler's book. There is a typo in his, the second to last
    # value should be 4, not 0 in Figure 2.1.
    assert evals == compute_reed_soloman_evaluations(u, PrimeField(p))


def test_univariate_evaluation2():
    p = 11
    u = UnivariatePolynomial([PrimeFieldValue(2, p), PrimeFieldValue(1, p), PrimeFieldValue(0, p)])
    evals = [u(PrimeFieldValue(i, p)) for i in range(p)]
    assert evals == compute_reed_soloman_evaluations(u, PrimeField(p))
