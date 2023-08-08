"""Testing only
"""

from park.field.prime_field import PrimeFieldValue
from park.polynomial.multivariate import Term, Variable

if __name__ == "__main__":
    t1 = Term(
        [
            Variable(0, 1),
            Variable(1, 1),
        ]
    )
    print(t1([PrimeFieldValue(2, 5), PrimeFieldValue(2, 5)]))
