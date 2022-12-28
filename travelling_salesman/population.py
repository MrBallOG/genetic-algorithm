import random
from typing import List
from individual import Individual
from gene import Gene


class Population:
    def __init__(self, size: int, mutation_prob: float, default_chromosome: List[Gene]) -> None:
        Individual.set_class_vars(default_chromosome)
        self.size = size
        self.mutation_prob = mutation_prob
        self.population: List[Individual] = []
        self._initialize_population()
        self.max_path_individual: Individual = None
        self.min_path_individual: Individual = None
        self.best_fitness_per_gen = []
        self.worst_fitness_per_gen = []
        self.average_fitness_per_gen = []

    def _initialize_population(self) -> None:
        for _ in range(self.size):
            ind = Individual()
            self.population.append(ind)

    def save_fitness_and_individual_stats(self) -> None:
        fitness_sum = self.population[0].fitness
        fitness_max = fitness_sum
        fitness_min = fitness_sum
        index_max = 0
        index_min = 0

        for i in range(1, self.size):
            fitness = self.population[i].fitness
            fitness_sum += fitness

            if fitness_max < fitness:
                fitness_max = fitness
                index_max = i
            elif fitness_min > fitness:
                fitness_min = fitness
                index_min = i

        if self.max_path_individual is None or self.max_path_individual.fitness > fitness_min:
            self.max_path_individual = self.population[index_min]
        if self.min_path_individual is None or self.min_path_individual.fitness < fitness_max:
            self.min_path_individual = self.population[index_max]

        self.best_fitness_per_gen.append(
            Individual.fitness_const - fitness_max)
        self.worst_fitness_per_gen.append(
            Individual.fitness_const - fitness_min)
        self.average_fitness_per_gen.append(
            Individual.fitness_const - fitness_sum / self.size)

    def select_using_roulette_selection(self) -> None:
        weights: List[float] = [
            (self.population[i].fitness / 2) ** 5 for i in range(self.size)]
        self.population = random.choices(
            self.population, weights=weights, k=self.size)

    def _remove_random_individual(self) -> Individual:
        return self.population.pop(random.randrange(len(self.population)))

    def crossover(self) -> None:
        new_population: List[Individual] = []

        while len(self.population) >= 2:
            ind_1 = self._remove_random_individual()
            ind_2 = self._remove_random_individual()

            if 0.5 > random.random():
                ind_1, ind_2 = Individual.crossover(ind_1, ind_2)
            # ind_1, ind_2 = Individual.crossover(ind_1, ind_2)

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
