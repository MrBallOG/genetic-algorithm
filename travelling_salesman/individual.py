import random
from typing import Tuple, List
from typing_extensions import Self
from gene import Gene


class Individual:
    def __init__(self, chromosome: List[Gene] = None) -> None:
        if chromosome is None:
            self._draw_chromosome_val()
        else:
            self.chromosome = chromosome

    @classmethod
    def set_class_vars(cls, default_chromosome: List[Gene]) -> None:
        cls.default_chromosome = default_chromosome
        cls.chromosome_len = len(default_chromosome)
        cls._calc_all_dists()

    @classmethod
    def _calc_all_dists(cls) -> None:
        dist_dict = {}
        max_dist = 0

        for i in range(cls.chromosome_len):
            for j in range(cls.chromosome_len):
                if i == j or j < i:
                    continue

                g1 = cls.default_chromosome[i]
                g2 = cls.default_chromosome[j]

                dist = g1.calc_distance(g2)
                name = ''.join(sorted([g1.name, g2.name]))
                dist_dict[name] = dist

                if dist > max_dist:
                    max_dist = dist

        cls.dist_dict = dist_dict
        cls.fitness_const = max_dist * cls.chromosome_len

    def _draw_chromosome_val(self) -> None:
        self.chromosome = Individual.default_chromosome.copy()
        random.shuffle(self.chromosome)

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
