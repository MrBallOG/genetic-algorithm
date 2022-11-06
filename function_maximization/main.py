from typing import Callable
import matplotlib.pyplot as plt
from population import Population


# x = 2
# y = eval("x**2")
# print(y)


# x = 34
# string_len = 6
# s = f"{x:0{string_len}b}"
# # s is '100010'
# s2 = '000001'
# s = s[0:5] + s2[5:6]
# # s is '100011'
# xi = int(s, 2)
# print(xi)

def get_fitness_function(function_string: str = None) -> Callable[[int], float]:
    if function_string is None:
        return lambda x: -0.1 * x**2 + 3 * x + 9
    else:
        return lambda x: eval(function_string)


def main() -> None:
    min_val = -2
    max_val = 32
    fitness_function = get_fitness_function("-0.1 * x**2 + 3 * x + 9")

    population = Population(max_val, min_val, fitness_function, size=3)
    print(population.get_max_min_avg_fitness())
    for i in range(3):
        ind = population.population[i]
        print(ind.fitness, ind.chromosome, ind.chromosome_bin_str)


if __name__ == "__main__":
    main()
