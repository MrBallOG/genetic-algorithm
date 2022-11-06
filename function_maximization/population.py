from collections import deque
import random
from typing import Callable, Tuple, Deque
from individual import Individual


class Population:
    def __init__(self, max_val: int, min_val: int, fitness_function: Callable[[int], float], crossover_prob: float = 0.5, mutation_prob: float = 0.02, size: int = 100) -> None:
        self.max_val = max_val
        self.min_val = min_val
        self.offset = 0 - min_val if min_val < 0 else 0
        self.bin_str_len = len(bin(max_val + self.offset)) - 2
        self.fitness_function = fitness_function
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.size = size
        self.population: Deque[Individual] = deque([])
        self._initialize_population()

    def _initialize_population(self) -> None:
        for _ in range(self.size):
            ind = Individual(self.max_val, self.min_val, self.offset,
                             self.bin_str_len, self.fitness_function)
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
