from park.field.prime_field import PrimeFieldValue
from park.polynomial.multivariate import MultivariatePolynomial
from park.polynomial.univariate import UnivariatePolynomial
from typing import List
import itertools


def generate_boolean_hypercube(n: int, p: int) -> List[List[PrimeFieldValue]]:
    """Generates the boolean hypercube entries over n variables.

    Args:
        n (int): The number of variables.
        p (int): The prime value for the finite field.

    Returns:
        List[List[PrimeFieldValue]]: The boolean hypercube entries.
    """
    boolean_values = [PrimeFieldValue(0, p), PrimeFieldValue(1, p)]
    hypercube_evaluations = list(itertools.product(boolean_values, repeat=n))
    # Technically a list of tuples, but let's pretend it's a list of lists.
    return hypercube_evaluations  # type: ignore


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


class MultilinearExtensionPolynomial:
    def __init__(self, p: MultivariatePolynomial):
        """Maps the function p : {0, 1}^v -> F into its unique multilinear extension
        form \tilde{p}.

        Args:
            p (MultivariatePolynomial): The multivariate polynomial.
        """
        self.__polynomial = p
        self.__interpolating_set = generate_boolean_hypercube(self.__polynomial.num_vars, self.__polynomial.p)

    def __call__(self, x: List[PrimeFieldValue]) -> PrimeFieldValue:
        output = PrimeFieldValue(0, self.__polynomial.p)
        for w in self.__interpolating_set:
            # Get the polynomial evaluation
            evaluation = self.__polynomial(w)
            output += evaluation * self._compute_lagrange_basis(w, x)
        return output

    def _compute_lagrange_basis(self, w: List[PrimeFieldValue], x: List[PrimeFieldValue]) -> PrimeFieldValue:
        """Computes the set of multilinear Lagrange basis polynomials with interpolating set
        w in {0, 1}^v.

        Args:
            w (List[PrimeFieldValue]): The interpolating set for the lagrange basis polynomial.
            x (List[PrimeFieldValue]): The inputs to evaluate the polynomial on.

        Returns:
            PrimeFieldValue: The evaluation of lagrange basis polynomial.
        """
        output = PrimeFieldValue(1, self.__polynomial.p)
        for i in range(len(w)):
            output *= x[i] * w[i] + (1 - x[i]) * (1 - w[i])  # type: ignore
        return output
