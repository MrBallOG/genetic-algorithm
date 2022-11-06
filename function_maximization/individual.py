import random
from typing import Callable


class Individual:
    def __init__(self, max_val: int, min_val: int, offset: int, bin_len: int, fitness_function: Callable[[int], float], chromosome: int = None) -> None:
        self.max_val = max_val
        self.min_val = min_val
        self.offset = offset
        self.bin_len = bin_len
        self.calc_fitness = fitness_function

        if chromosome is None:
            self._draw_chromosome_val()
        else:
            self.chromosome = chromosome

    def _draw_chromosome_val(self) -> None:
        self.chromosome = random.randint(self.min_val, self.max_val)
