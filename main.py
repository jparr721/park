"""Testing only
"""

from park.field.prime_field import PrimeFieldValue
from park.polynomial.multivariate import Term, Variable

if __name__ == "__main__":
    T = Term(
        [
            Variable(PrimeFieldValue(1, 5), 1),
            Variable(PrimeFieldValue(1, 5), 1),
            Variable(PrimeFieldValue(2, 5), 2),
        ]
    )
    print(T)
