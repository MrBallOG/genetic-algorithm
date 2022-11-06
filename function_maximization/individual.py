import random
from typing import Callable


class Individual:
    def __init__(self, max_val: int, min_val: int, offset: int, bin_str_len: int, fitness_function: Callable[[int], float], chromosome_bin_str: str = None) -> None:
        self.max_val = max_val
        self.min_val = min_val
        self.offset = offset
        self.bin_str_len = bin_str_len
        self.calc_fitness = fitness_function

        if chromosome_bin_str is None:
            self._draw_chromosome_val()
            self._set_chromosome_bin_str_from_chromosome()
            self.set_fitness()
        else:
            self.chromosome_bin_str = chromosome_bin_str
            self._set_chromosome_from_chromosome_bin_str()

    def _draw_chromosome_val(self) -> None:
        self.chromosome = random.randint(self.min_val, self.max_val)

    def _set_chromosome_from_chromosome_bin_str(self) -> None:
        chromosome = int(self.chromosome_bin_str, 2) - self.offset
        self.chromosome = max(self.min_val, min(self.max_val, chromosome))

        if self.chromosome != chromosome:
            self._set_chromosome_bin_str_from_chromosome()

    def _set_chromosome_bin_str_from_chromosome(self) -> None:
        self.chromosome_bin_str = f"{self.chromosome + self.offset:0{self.bin_str_len}b}"

    def set_fitness(self) -> None:
        self.fitness = max(0.0, self.calc_fitness(self.chromosome))

    def mutate(self) -> None:
        index = random.randrange(self.bin_str_len)
        bit = self.chromosome_bin_str[index]

        if bit == "1":
            self.chromosome_bin_str[index] = "0"
        else:
            self.chromosome_bin_str[index] = "1"

        self._set_chromosome_from_chromosome_bin_str()
