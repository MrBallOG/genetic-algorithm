import random
from typing import Tuple
from typing_extensions import Self


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
    def set_class_vars(cls, max_val: int, min_val: int, function_string: str) -> None:
        cls.max_val = max_val
        cls.min_val = min_val
        cls.offset = 0 - cls.min_val if cls.min_val < 0 else 0
        cls.bin_str_len = len(bin(cls.max_val + cls.offset)) - 2
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

    @classmethod
    def crossover(cls, ind_1: Self, ind_2: Self) -> Tuple[Self, Self]:
        crossover_point = random.randrange(1, cls.bin_str_len)
        ind_1_str = ind_1.chromosome_bin_str
        ind_2_str = ind_2.chromosome_bin_str
        bin_str_1 = ind_1_str[:crossover_point] + ind_2_str[crossover_point:]
        bin_str_2 = ind_2_str[:crossover_point] + ind_1_str[crossover_point:]

        return cls(bin_str_1), cls(bin_str_2)

    def mutate(self) -> None:
        index = random.randrange(Individual.bin_str_len)
        bit = self.chromosome_bin_str[index]
        bin_str = self.chromosome_bin_str
        pre = bin_str[:index]
        suf = bin_str[index + 1:]

        if bit == "1":
            self.chromosome_bin_str = pre + "0" + suf
        else:
            self.chromosome_bin_str = pre + "1" + suf

        self._set_chromosome_from_chromosome_bin_str()
