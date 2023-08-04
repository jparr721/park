from park.field.prime_field import PrimeFieldValue
from park.polynomial.univariate import UnivariatePolynomial


class UnivariateExtensionPolynomial:
    def __init__(self, p: UnivariatePolynomial, f: int):
        """Computes Univariate lagrange interpolation polynomial q_a as evaluations over
        the canonical set of inputs defined over the prime field f.

        Args:
            p (UnivariatePolynomial): p The univariate polynomial
            f (int): f The prime field length
        """
        if p.degree >= f:
            raise ValueError(f"Prime field F_{f} must be >> the polynomial degree: {p.degree}")
        self.p = p
        self.f = f

    def __call__(self, inp: PrimeFieldValue) -> PrimeFieldValue:
        output = PrimeFieldValue(0, self.f)
        for i, coeff in enumerate(self.p):
            output += coeff * self._compute_lagrange_basis_polynomial(PrimeFieldValue(i, self.f), inp)
        return output

    def _compute_lagrange_basis_polynomial(self, i: PrimeFieldValue, inp: PrimeFieldValue) -> PrimeFieldValue:
        """Computes the univariate lagrange basis polynomial for a given indicator, i.
        The indicator polynomial maps some input i to 1 and kills all other inputs on
        {0, 1, ..., n - 1} which corresponds to the degree of the source univariate polynomial p.

        Args:
            i (int): The indicator associated with this polynomial.
            inp (PrimeFieldValue): The input to the lagrange basis polynomial.
        Returns:
            PrimeFieldValue: The evaluation of the lagrange basis polynomial
        """
        output = PrimeFieldValue(1, self.f)
        for k in range(self.p.degree):
            if k == i:
                continue
            output *= (inp - k) / (i - k)
        return output
