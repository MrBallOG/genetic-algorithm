import random
from typing import List, Tuple
from individual import Individual


class Population:
    def __init__(self, max_val: int = None, min_val: int = None, function_string: str = None, crossover_prob: float = 0.5, mutation_prob: float = 0.02, size: int = 100) -> None:
        Individual.set_class_params(max_val, min_val, function_string)
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.size = size
        self.population: List[Individual] = []
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

    def select_using_roulette_selection(self) -> None:
        weights: List[float] = [
            self.population[i].fitness for i in range(self.size)]
        self.population = random.choices(
            self.population, weights=weights, k=self.size)

    def _remove_random_individual(self) -> Individual:
        return self.population.pop(random.randrange(len(self.population)))

    def crossover(self) -> None:
        new_population: List[Individual] = []

        while len(self.population) > 2:
            ind_1 = self._remove_random_individual()
            ind_2 = self._remove_random_individual()

            if self.crossover_prob > random.random():
                ind_1, ind_2 = Individual.crossover(ind_1, ind_2)

            new_population.append(ind_1)
            new_population.append(ind_2)

        if len(self.population) == 1:
            new_population.append(self.population[0])

        self.population = new_population

    def mutate(self) -> None:
        for i in range(self.size):
            ind = self.population[i]

            if self.mutation_prob > random.random():
                ind.mutate()

            ind.set_fitness()
