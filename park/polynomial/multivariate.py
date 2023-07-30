"""Based heavily on arkworks' implementation of polynomials
    source: https://github.com/arkworks-rs/algebra/blob/master/poly/src/polynomial/multivariate/mod.rs
"""


from __future__ import annotations

from dataclasses import dataclass, astuple
from typing import List, Tuple
from park.field.prime_field import PrimeFieldValue


@dataclass
class Variable:
    """
    Corrsponds to a variable in a Term of a polynomial.

    Args:
        var (int): The variable, denoted as "x_{var}"
        power (int): The power of the variable, denoted as "x_{var}^{power}"
    """

    var: int
    power: int

    def __iter__(self):
        return iter(astuple(self))

    def __repr__(self):
        return f"{self.__class__.__name__}(var={self.var}, power={self.power})"

    def __str__(self) -> str:
        if self.power == 0:
            return "0"
        elif self.power > 1 or self.power < 0:
            return f"x_{self.var}^{self.power}"
        else:
            return f"x_{self.var}"


class Term:
    """Stores a term of a multivariate polynomial."""

    def __init__(self, term: List[Variable] | Tuple[Variable]):
        # Initialize the term.
        self.__term = term

        # Remove all terms with zero power
        self.__term = [t for t in self.__term if t.power != 0]

        # If we have more than variable with the same power, combine them.
        if len(self.__term) > 1:
            self.__term = sorted(self.__term, key=lambda x: x.var)
            self._combine_variables()

    def __repr__(self) -> str:
        out = ""
        for var in self.__term:
            if var.power == 1:
                out += f" * x_{var.var}"
            else:
                out += f" * x_{var.var}^{var.power}"
        return out

    def __len__(self) -> int:
        return len(self.__term)

    # def __call__(self, __point: PrimeField) -> PrimeFieldValue:
    #     return prod([__point[t.var] ** t.power for t in self.__term])  # type: ignore

    def __eq__(self, other: Term):
        if self.degree == other.degree:
            for t1, t2 in zip(self, other):
                if t1.var == t2.var:
                    if t1.power != t2.power:
                        return False
                else:
                    return False
            else:
                return True
        return False

    def __gt__(self, other: Term):
        if self.degree == other.degree:
            for t1, t2 in zip(self, other):
                if t1.var == t2.var:
                    if t1.power != t2.power:
                        return t1.power > t2.power
                else:
                    # x_0 takes precedence to x_1, etc
                    return t1.var < t2.var

            # They're the same
            return False

        else:
            # Degrees aren't equal, return the highest one
            return self.degree > other.degree

    def __lt__(self, other: Term):
        if self.degree == other.degree:
            for t1, t2 in zip(self, other):
                if t1.var == t2.var:
                    if t1.power != t2.power:
                        return t1.power < t2.power
                else:
                    # x_0 takes precedence to x_1, etc
                    return t1.var > t2.var

            # They're the same
            return False

        else:
            # Degrees aren't equal, return the highest one
            return self.degree < other.degree

    def __ge__(self, other: Term):
        if self.degree == other.degree:
            for t1, t2 in zip(self, other):
                if t1.var == t2.var:
                    if t1.power != t2.power:
                        return t1.power >= t2.power
                else:
                    return t1.var <= t2.var
            # They're the same, thus equal
            return True
        else:
            return self.degree >= other.degree

    def __le__(self, other: Term):
        if self.degree == other.degree:
            for t1, t2 in zip(self, other):
                if t1.var == t2.var:
                    if t1.power != t2.power:
                        return t1.power <= t2.power
                else:
                    # x_0 takes precedence to x_1, etc
                    return t1.var >= t2.var

            # They're the same, thus equal
            return True

        else:
            # Degrees aren't equal, return the highest one
            return self.degree <= other.degree

    def __iter__(self):
        return iter(self.__term)

    @property
    def degree(self) -> int:
        """Returns the degree of the monomial term.

        Returns:
            int: The degree of the polynomial term.
        """
        return sum(self.powers)

    @property
    def powers(self) -> List[int]:
        return [t.power for t in self.__term]

    @property
    def is_constant(self) -> bool:
        return len(self) == 0 or self.degree == 0

    def _combine_variables(self):
        """Combines variables with the same power. Assumes self.__term is sorted"""
        dedup: List[Variable] = []
        for var, power in self.__term:
            if len(dedup) == 0 or dedup[-1].var != var:
                dedup.append(Variable(var, power))
            else:
                dedup[-1] = Variable(dedup[-1].var, dedup[-1].power + power)

        self.__term = dedup


@dataclass
class MultivariatePolynomialTerm:
    coefficient: PrimeFieldValue
    term: Term

    def __iter__(self):
        return iter(astuple(self))


class MultivariatePolynomial:
    def __init__(self, num_vars: int, terms: List[MultivariatePolynomialTerm]):
        self.num_vars = num_vars

        # Sort the terms in ascending order
        self.__terms = sorted(terms, key=lambda t: t.term)

        # If any terms are duplicated, combine them
        dedup: List[MultivariatePolynomialTerm] = []
        for term in self.__terms:
            # If the dedup list is empty, or the terms are not equal, insert
            if len(dedup) == 0 or dedup[-1].term != term.term:
                dedup.append(term)
            else:
                # Otherwise, combine
                dedup[-1] = MultivariatePolynomialTerm(
                    dedup[-1].coefficient + term.coefficient, dedup[-1].term
                )

        # Remove zero entries
        self.__terms: List[MultivariatePolynomialTerm] = list(
            filter(lambda x: not x.coefficient.is_zero, dedup)
        )

    def __repr__(self):
        # out = ""
        out = []

        for coeff, term in self.__terms:
            if coeff.is_zero:
                continue

            if term.is_constant:
                # out += f"\n{coeff}"
                out.append(str(coeff))
            else:
                out.append(f"{coeff}{term}")
                # out += f"\n{coeff}{term}"

        return " + ".join(out)
