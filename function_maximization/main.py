import matplotlib.pyplot as plt
from individual import Individual
from population import Population


def main() -> None:
    min_val = -2
    max_val = 32
    generation_count = 50
    best = []
    worst = []
    average = []

    population = Population(
        function_string="-0.1 * x**2 + 3 * x + 9",  size=100)

    temp = population.get_max_min_avg_fitness()
    best.append(temp[0])
    worst.append(temp[1])
    average.append(temp[2])

    for _ in range(generation_count - 1):
        population.select_using_roulette_selection()
        population.crossover()
        population.mutate()
        temp = population.get_max_min_avg_fitness()
        best.append(temp[0])
        worst.append(temp[1])
        average.append(temp[2])

    x = [i + 1 for i in range(generation_count)]
    plt.figure(figsize=(14, 8), dpi=75)
    plt.plot(x, best, "o-", label="maksymalne przystosowanie")
    plt.plot(x, average, "o-",  label="średnie przystosowanie")
    plt.plot(x, worst, "o-",  label="minimalne przystosowanie")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel("Pokolenie")
    plt.ylabel("Przystosowanie")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
