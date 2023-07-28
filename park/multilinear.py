from typing import List

import numpy as np


class MultilinearPolynomial:
    def __init__(self, coeff_matrix: np.ndarray, variables: List[str] = []):
        if not isinstance(variables, list):
            raise ValueError(f"Mismatched type for variables, expected 'list', got {type(variables)}")

        if len(variables) != len(coeff_matrix):
            raise ValueError(f"Invalid number of variables, wanted '{len(coeff_matrix)}', got '{len(variables)}")

        self.coeff_matrix = coeff_matrix
        self.var_matrix = []
        for ii in range(self.coeff_matrix.shape[0]):
            sub = []
            for jj in range(self.coeff_matrix.shape[1]):
                sub.append("")
            self.var_matrix.append(sub)

        for ii in range(self.coeff_matrix.shape[0]):
            vx = variables[ii]
            for jj in range(self.coeff_matrix.shape[1]):
                vy = variables[jj]
                if ii == 0 and jj == 0:
                    self.var_matrix[ii][jj] = ""
                else:
                    self.var_matrix[ii][jj] = f"{vx}{vy}"

        # self.var_matrix[0][0] = ""
        # self.var_matrix[1][0] = variables[0]
        # self.var_matrix[0][1] = variables[1]
        # self.var_matrix[1][1] = f"{variables[0]}{variables[1]}"
        self.var_matrix = np.asanyarray(self.var_matrix)

        # for ii in range(self.coeff_matrix.shape[0]):
        #     vd1 = variables[ii]
        #     for jj in range(self.coeff_matrix.shape[0]):
        #         vd2 = variables[jj]
        #         print(vd1, vd2)
        #         if ii == 0 and jj == 0:
        #             self.var_matrix[ii, jj] = ""
        #             continue

        print(self.var_matrix)

    def __repr__(self) -> str:
        degree = len(self.coeff_matrix)
        terms = []

        coeff_shape = self.coeff_matrix.shape

        for ii in range(coeff_shape[0]):
            for jj in range(coeff_shape[1]):
                term = self.coeff_matrix[ii, jj]

        return " + ".join(terms)


class MultivariatePolynomial:
    def __init__(self, sets_of_coeffs: List[List[float | int]], variables: List[str] = []):
        self.sets_of_coeffs = sets_of_coeffs

        # Die when a univariate polynomial is passed
        if len(sets_of_coeffs) == 1 or not isinstance(sets_of_coeffs[0], list):
            raise ValueError("Found Univariate Polynomial, expected Multivariate Polynomial")

        # Make sure they're all the same degree
        degrees = [len(c) for c in self.sets_of_coeffs]
        if all(d != degrees[0] for d in degrees):
            raise ValueError("Degree mismatch in input polynomials")

        # Make sure the variables line up
        self.variables = variables

        # No vars found, just do the default
        if len(self.variables) == 0:
            for d in range(len(self)):
                self.variables.append(f"x{d+1}")

        if (nvars := len(self.variables)) != len(self):
            raise ValueError(f"Mismatched varibles for the coefficients got: {nvars}, wanted: {len(self)}")

    def __repr__(self) -> str:
        terms = []
        degree = len(self)

        for i, term in enumerate(zip(*self.sets_of_coeffs)):
            # Append the term.
            s = ""
            for var_id, coeff in enumerate(term):
                # Throw away any ones when it's not the last term.
                if coeff == 1 and i != len(self):
                    coeff = ""

                if coeff == 0:
                    continue

                exp = degree - i
                var = self.variables[var_id] if i < self.degree else ""
                if exp > 1:
                    s += f"{coeff}{var}^{exp}"
                elif exp == 1:
                    s += f"{coeff}{var}"
                else:
                    s += f"{coeff}"

            print("s", s)

        return " + ".join(terms)

    def __len__(self):
        return len(self.sets_of_coeffs[0]) - 1

    def __call__(self, *__values):
        if (nvals := len(__values)) != len(self):
            raise ValueError(f"Invalid number of variable substitutions, wanted {len(self)}, got {nvals}")

    @property
    def degree(self):
        return len(self)


if __name__ == "__main__":
    p = UnivariatePolynomial(4, 1, 1)
    print(p, len(p), p(2))

    # m = MultivariatePolynomial([[1, 2, 3], [1, 2, 3]], variables=["x", "y"])
    # print(m)

    m = MultilinearPolynomial(np.array([[1, 1], [2, 4]]), variables=["x", "y"])
    # print(m.var_matrix)
