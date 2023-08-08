from park.polynomial.multivariate import MultivariatePolynomial, MultivariatePolynomialTerm, Variable, Term
from park.field.prime_field import PrimeFieldValue
import pytest


def test_varible_init():
    one = 1
    v = Variable(one, 5)

    assert v is not None
    assert v.var == 1
    assert v.power == 5


def test_term_init():
    one = 1
    two = 2

    v1 = Variable(one, 1)
    v2 = Variable(one, 2)
    v3 = Variable(two, 2)

    t = Term([v1, v2, v3])

    assert t is not None
    assert t.degree == 5
    assert t.powers == [3, 2]


def test_term_repr():
    one = 1
    two = 2

    v1 = Variable(one, 1)
    v2 = Variable(one, 2)
    v3 = Variable(two, 2)

    t = Term([v1, v2, v3, Variable(3, 5), Variable(3, 10)])
    assert repr(t) == " * x_1^3 * x_2^2 * x_3^15"


@pytest.fixture
def arith_terms():
    t1 = Term(
        [
            Variable(1, 1),
        ]
    )

    t2 = Term(
        [
            Variable(2, 1),
        ]
    )
    return t1, t2


def test_term_gte(arith_terms):
    t1, t2 = arith_terms
    assert t1 >= t2
    assert t1 >= t1


def test_term_gt(arith_terms):
    t1, t2 = arith_terms
    assert t1 > t2


def test_term_lte(arith_terms):
    t1, t2 = arith_terms
    assert t1 <= t1
    assert not (t1 <= t2)


def test_term_lt(arith_terms):
    t1, t2 = arith_terms
    assert not (t1 < t1)
    assert not (t1 < t2)
    assert t2 < t1


def test_term_eq(arith_terms):
    t1, t2 = arith_terms
    assert not (t1 == t2)
    assert t2 == t2


def test_term_evaluate1():
    t1 = Term(
        [
            Variable(0, 1),
            Variable(1, 1),
        ]
    )
    assert t1([PrimeFieldValue(2, 5), PrimeFieldValue(2, 5)]) == 4


def test_term_evaluate2():
    t1 = Term(
        [
            Variable(0, 2),
            Variable(1, 1),
        ]
    )

    val = t1([PrimeFieldValue(2, 5), PrimeFieldValue(2, 5)])
    assert val == 3


def test_term_evaluate3():
    t1 = Term(
        [
            Variable(0, 2),
            Variable(1, 1),
        ]
    )

    val = t1([PrimeFieldValue(2, 11), PrimeFieldValue(2, 11)])
    assert val == 8


def test_multivariate_init():
    t1 = Term(
        [
            Variable(1, 1),
            Variable(2, 1),
        ]
    )

    t2 = Term(
        [
            Variable(0, 1),
            Variable(2, 1),
        ]
    )

    t3 = Term([Variable(0, 3)])

    p = 11

    m = MultivariatePolynomial(
        3,
        [
            MultivariatePolynomialTerm(PrimeFieldValue(2, p), t3),
            MultivariatePolynomialTerm(PrimeFieldValue(1, p), t1),
            MultivariatePolynomialTerm(PrimeFieldValue(1, p), t2),
            MultivariatePolynomialTerm(PrimeFieldValue(5, p), Term([])),
        ],
    )
    assert m is not None


def test_multivariate_repr():
    t1 = Term(
        [
            Variable(1, 1),
            Variable(2, 1),
        ]
    )

    t2 = Term(
        [
            Variable(0, 1),
            Variable(2, 1),
        ]
    )

    t3 = Term([Variable(0, 3)])

    p = 11

    m = MultivariatePolynomial(
        3,
        [
            MultivariatePolynomialTerm(PrimeFieldValue(2, p), t3),
            MultivariatePolynomialTerm(PrimeFieldValue(1, p), t1),
            MultivariatePolynomialTerm(PrimeFieldValue(1, p), t2),
            MultivariatePolynomialTerm(PrimeFieldValue(5, p), Term([])),
        ],
    )
    assert repr(m) == "5 +  * x_1 * x_2 +  * x_0 * x_2 + 2 * x_0^3"


def test_multivariate_degree():
    t1 = Term(
        [
            Variable(1, 1),
            Variable(2, 1),
        ]
    )

    t2 = Term(
        [
            Variable(0, 1),
            Variable(2, 1),
        ]
    )

    t3 = Term([Variable(0, 3)])

    p = 11

    m = MultivariatePolynomial(
        3,
        [
            MultivariatePolynomialTerm(PrimeFieldValue(2, p), t3),
            MultivariatePolynomialTerm(PrimeFieldValue(1, p), t1),
            MultivariatePolynomialTerm(PrimeFieldValue(1, p), t2),
            MultivariatePolynomialTerm(PrimeFieldValue(5, p), Term([])),
        ],
    )
    assert m.degree == 3
