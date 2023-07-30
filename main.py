"""Testing only
"""

from park.field.prime_field import PrimeFieldValue, PrimeField
from park.polynomial.multivariate import Term, Variable, MultivariatePolynomial

if __name__ == "__main__":
    t1 = Term(
        [
            Variable(1, 1),
            Variable(1, 1),
            Variable(2, 2),
            Variable(3, 1),
        ]
    )

    t2 = Term(
        [
            Variable(2, 1),
            Variable(0, 1),
        ]
    )

    t3 = Term([Variable(0, 10), Variable(1, 5)])
    t3 = Term([Variable(3, 1)])

    p = 5

    m = MultivariatePolynomial(
        3,
        [
            (PrimeFieldValue(3, p), t3),
            (PrimeFieldValue(3, p), t1),
            (PrimeFieldValue(1, p), t2),
        ],
    )
    print(m)
