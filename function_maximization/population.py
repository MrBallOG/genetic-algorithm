from collections import deque
import random
from typing import Callable, Tuple, Deque
from individual import Individual


class Population:
    def __init__(self, max_val: int = None, min_val: int = None, function_string: str = None, crossover_prob: float = 0.5, mutation_prob: float = 0.02, size: int = 100) -> None:
        Individual.set_class_params(
            max_val, min_val, function_string)
        # może nie potrzebne jesli zrobie class methody w individual
        self.bin_str_len = Individual.bin_str_len
        ############################################################
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.size = size
        self.population: Deque[Individual] = deque([])
        self._initialize_population()

    def _initialize_population(self) -> None:
        for _ in range(self.size):
            ind = Individual()
            self.population.append(ind)

    def get_max_min_avg_fitness(self) -> Tuple[float, float, float]:
        fitness_sum = self.population[0].fitness
        fitness_max = fitness_sum
        fitness_min = fitness_sum

        for i in range(1, self.size):
            fitness = self.population[i].fitness
            fitness_sum += fitness

            if fitness_max < fitness:
                fitness_max = fitness
            elif fitness_min > fitness:
                fitness_max = fitness

        return fitness_max, fitness_min, fitness_sum / self.size

    # po mutacji obliczyc fitness dla kazdego
    def mutate():
        pass
