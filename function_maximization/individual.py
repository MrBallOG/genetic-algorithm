import random
from typing import Callable


class Individual:
    def __init__(self, chromosome_bin_str: str = None) -> None:
        if chromosome_bin_str is None:
            self._draw_chromosome_val()
            self._set_chromosome_bin_str_from_chromosome()
            self.set_fitness()
        else:
            self.chromosome_bin_str = chromosome_bin_str
            self._set_chromosome_from_chromosome_bin_str()

    @classmethod
    def set_class_params(cls, max_val: int, min_val: int, function_string: str = None) -> None:
        cls.max_val = max_val if max_val is not None else 32
        cls.min_val = min_val if min_val is not None else -2
        cls.offset = 0 - cls.min_val if cls.min_val < 0 else 0
        cls.bin_str_len = len(bin(cls.max_val + cls.offset)) - 2

        if function_string is None:
            cls.calc_fitness = lambda x: -0.1 * x**2 + 3 * x + 9
        else:
            cls.calc_fitness = lambda x: eval(function_string)

    def _draw_chromosome_val(self) -> None:
        self.chromosome = random.randint(
            Individual.min_val, Individual.max_val)

    def _set_chromosome_from_chromosome_bin_str(self) -> None:
        chromosome = int(self.chromosome_bin_str, 2) - Individual.offset
        self.chromosome = max(Individual.min_val, min(
            Individual.max_val, chromosome))

        if self.chromosome != chromosome:
            self._set_chromosome_bin_str_from_chromosome()

    def _set_chromosome_bin_str_from_chromosome(self) -> None:
        self.chromosome_bin_str = f"{self.chromosome + Individual.offset:0{Individual.bin_str_len}b}"

    def set_fitness(self) -> None:
        self.fitness = max(0.0, Individual.calc_fitness(self.chromosome))

    def mutate(self) -> None:
        index = random.randrange(Individual.bin_str_len)
        bit = self.chromosome_bin_str[index]

        if bit == "1":
            self.chromosome_bin_str[index] = "0"
        else:
            self.chromosome_bin_str[index] = "1"

        self._set_chromosome_from_chromosome_bin_str()
