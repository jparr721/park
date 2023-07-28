import random


class PrimeField:
    def __init__(self, p: int):
        self.p = p

        # The values of the finite field
        self.__vals = list(range(self.p))

    def __len__(self):
        return self.p

    def __call__(self, __value: int) -> int:
        return __value % self.p

    def sample(self) -> int:
        """Sample randomly from the finite field

        Returns:
            int: The random sample.
        """
        return random.choice(self.__vals)
