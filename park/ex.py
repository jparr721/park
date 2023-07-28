import itertools
from typing import List

import numpy as np


class FiniteFieldModP:
    def __init__(self, p: int):
        self.p = p

    def __len__(self):
        return self.p

    def __call__(self, __value: int) -> int:
        return __value % self.p

    def sample(self):
        return np.random.choice(range(self.p))


def generate_boolean_hypercube(n: int) -> List[List[int]]:
    """Generates the boolean hypercube entries over n variables.

    Args:
        n (int): The number of variables.

    Returns:
        List[List[int]]: The boolean hypercube entries.
    """
    boolean_values = [0, 1]
    hypercube_evaluations = list(itertools.product(boolean_values, repeat=n))
    return hypercube_evaluations


def evaluate_lagrange_basis(w: List[int], x: List[int]):
    return np.prod([x[i] * w[i] + (1 - x[i]) * (1 - w[i]) for i in range(len(w))])


def evaluate_multilinear_extension(evaluations: np.ndarray, x: List[int]):
    """Evaluates the multilinear extension of a polynomial created via lagrange interpolation.

    Args:
        evaluations (np.ndarray): The evaluations of the polynomial.
        x (List[int]): The inputs to evaluate the polynomial on.

    Returns:
        int: The evaluation of the multilinear extension.
    """
    if not isinstance(evaluations, np.ndarray):
        raise ValueError(f"Mismatched type for coeff_matrix, expected 'np.ndarray', got {type(evaluations)}")

    if evaluations.shape[0] != evaluations.shape[1]:
        raise ValueError(f"Invalid shape for coeff_matrix, expected square matrix, got {evaluations.shape}")

    if not np.all(np.linalg.eigvals(evaluations) > 0):
        raise ValueError(f"Invalid shape for coeff_matrix, expected positive definite matrix, got {evaluations}")

    n = evaluations.shape[0]
    boolean_hypercube = generate_boolean_hypercube(n)
    finite_field = FiniteFieldModP(5)

    return finite_field(
        np.sum(
            [
                evaluations[w] * np.prod([x[i] * w[i] + (1 - x[i]) * (1 - w[i]) for i in range(n)])
                for w in boolean_hypercube
            ]
        )
    )


if __name__ == "__main__":
    m = np.array([[1, 2], [1, 4]])
    evals = np.empty((5, 5), dtype=np.int32)
    for i in range(5):
        for j in range(5):
            evals[i, j] = evaluate_multilinear_extension(m, [i, j])
    print(evals)
