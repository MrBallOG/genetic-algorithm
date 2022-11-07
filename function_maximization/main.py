import matplotlib.pyplot as plt
from individual import Individual
from population import Population


def main() -> None:
    min_val = -2
    max_val = 32
    generation_count = 10

    population = Population(
        function_string="-0.1 * x**2 + 3 * x + 9",  size=10)
    print(population.get_max_min_avg_fitness())

    for i in range(generation_count - 1):
        population.select_using_roulette_selection()
        population.crossover()
        population.mutate()
        print(population.get_max_min_avg_fitness())


if __name__ == "__main__":
    main()
