"""Based heavily on arkworks' implementation of polynomials
    source: https://github.com/arkworks-rs/algebra/blob/master/poly/src/polynomial/multivariate/mod.rs
"""


from __future__ import annotations

from dataclasses import dataclass, astuple
from typing import List, Tuple

from park.field.prime_field import PrimeFieldValue


@dataclass
class Variable:
    var: PrimeFieldValue
    power: int

    def __iter__(self):
        return iter(astuple(self))


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

    def _combine_variables(self):
        """Combines variables with the same power. Assumes self.__term is sorted"""
        dedup: List[Variable] = []
        for var, power in self.__term:
            if len(dedup) == 0 or dedup[-1].var != var:
                dedup.append(Variable(var, power))
            else:
                dedup[-1] = Variable(dedup[-1].var, dedup[-1].power + power)

        self.__term = dedup
