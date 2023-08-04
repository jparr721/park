"""Testing only
"""

from park.field.prime_field import PrimeFieldValue
from park.polynomial.multivariate import (
    MultivariatePolynomialTerm,
    Term,
    Variable,
    MultivariatePolynomial,
)

if __name__ == "__main__":
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
    print(t1)
    print(t2)
    print(t3)
    print(m, m.degree)
