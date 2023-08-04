from typing import List

from park.field.prime_field import PrimeField, PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial


def compute_reed_soloman_evaluations(p: UnivariatePolynomial, f: PrimeField) -> List[PrimeFieldValue]:
    """Interprets the coefficients of p and computes the ECC extension over the field.

    Args:
        p (UnivariatePolynomial): The polynomial to extend.
        f (PrimeField): The prime field
    Returns:
        List[int]: The evaluations of the polynomial.
    """
    if len(f) < len(p):
        raise ValueError(f"Prime field is too small for the polynomial, expected something >> {len(p)}, got {len(f)}")
    return [p(v) for v in f]
