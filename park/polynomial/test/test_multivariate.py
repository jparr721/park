from park.field.prime_field import PrimeField
from park.polynomial.multivariate import Variable, Term
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


# def test_term_evaluate():
#     one = 1
#     two = 2

#     v1 = Variable(one, 1)
#     v2 = Variable(one, 2)
#     v3 = Variable(two, 2)

#     t = Term([v1, v2, v3, Variable(3, 5), Variable(3, 10)])
#     p = PrimeField(5)
#     print(t(p))
