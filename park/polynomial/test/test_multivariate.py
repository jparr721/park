from park.polynomial.multivariate import Variable
from park.field.prime_field import PrimeFieldValue


def test_varible_init():
    one = PrimeFieldValue(1, 5)
    v = Variable(one, 5)
    assert v.var == 1
    assert v.power == 5
