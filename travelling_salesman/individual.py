import random
from typing import Tuple, List
from typing_extensions import Self
from gene import Gene


class Individual:
    def __init__(self, chromosome: List[Gene] = None) -> None:
        if chromosome is None:
            self._draw_chromosome_val()
            self.set_fitness()
        else:
            self.chromosome = chromosome

    def __str__(self) -> str:
        return "".join([str(gene) for gene in self.chromosome])

    @classmethod
    def set_class_vars(cls, default_chromosome: List[Gene]) -> None:
        cls.default_chromosome = default_chromosome
        cls.chromosome_len = len(default_chromosome)
        cls._calc_all_dists_and_fitness_const()

    @classmethod
    def _calc_all_dists_and_fitness_const(cls) -> None:
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

    def set_fitness(self) -> None:
        dist = 0

        for i in range(1, Individual.chromosome_len):
            gene_1 = self.chromosome[i - 1]
            gene_2 = self.chromosome[i]
            name = "".join(sorted([gene_1.name, gene_2.name]))

            dist += Individual.dist_dict[name]

        self.fitness = Individual.fitness_const - dist

    @classmethod
    def crossover(cls, ind_1: Self, ind_2: Self) -> Tuple[Self, Self]:
        cp_1 = random.randrange(0, cls.chromosome_len)
        if cp_1 == 0:
            cp_2 = random.randrange(1, cls.chromosome_len)
        elif cp_1 == cls.chromosome_len - 1:
            cp_2 = cls.chromosome_len
        else:
            cp_2 = random.randrange(cp_1 + 1, cls.chromosome_len + 1)

        ind_1_part = ind_1.chromosome[cp_1: cp_2]
        ind_2_part = ind_2.chromosome[cp_1: cp_2]

        ind_1_part_names = [gene.name for gene in ind_1_part]
        ind_2_part_names = [gene.name for gene in ind_2_part]

        child_1: List[Gene] = []
        child_2: List[Gene] = []
        n_1 = 0
        n_2 = 0

        for i in range(cls.chromosome_len):
            gene_1 = ind_1.chromosome[i]
            gene_2 = ind_2.chromosome[i]

            if gene_1.name in ind_2_part_names:
                if i < cp_2:
                    n_1 += 1
            else:
                child_1.append(gene_1)

            if gene_2.name in ind_1_part_names:
                if i < cp_2:
                    n_2 += 1
            else:
                child_2.append(gene_2)

        rot_1 = cp_2 - cp_1 - n_1
        rot_2 = cp_2 - cp_1 - n_2

        child_1 = child_1[rot_1:] + child_1[:rot_1]
        child_2 = child_2[rot_2:] + child_2[:rot_2]

        child_1 = child_1[:cp_1] + ind_2_part + child_1[cp_1:]
        child_2 = child_2[:cp_1] + ind_1_part + child_2[cp_1:]

        return cls(child_1), cls(child_2)

    def mutate(self) -> None:
        indexes = random.sample(range(Individual.chromosome_len), k=2)

        gene = self.chromosome[indexes[0]]
        self.chromosome[indexes[0]] = self.chromosome[indexes[1]]
        self.chromosome[indexes[1]] = gene
