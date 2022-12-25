import matplotlib.pyplot as plt
from individual import Individual
from population import Population


def main() -> None:
    message = "Proszę podać argumenty oddzielone średnikiem w kolejności:\n"
    message += "-liczba pokoleń\n"
    message += "-liczba osobników w populacji\n"
    message += "-prawdopodobieństwo krzyżowania\n"
    message += "-prawdopodobieństwo mutacji\n"
    message += "-początek przedziału\n"
    message += "-koniec przedziału\n"
    message += "-funkcja dopasowania\n"
    message += "np.: 50;100;0.5;0.01;-2;32;-0.1 * x**2 + 3 * x + 9\n"
    message += "Powyższy przykład przedstawia wartości domyślne\n"
    message += "Argumenty można zostawiać puste, z czego na końcu nie trzeba pamiętać o średnikach\n"
    message += "np.: 50;;0.5;0.01\n"

    arg_list_default = [50, 100, 0.5, 0.01, -2, 32, "-0.1 * x**2 + 3 * x + 9"]
    arg_list_final = [None] * 7
    arg_str = input(message)
    arg_list = arg_str.split(";")
    n = len(arg_list)

    try:
        if n > 0 and arg_list[0] != "":
            arg_list_final[0] = int(arg_list[0])
        if n > 1 and arg_list[1] != "":
            arg_list_final[1] = int(arg_list[1])
        if n > 2 and arg_list[2] != "":
            arg_list_final[2] = float(arg_list[2])
        if n > 3 and arg_list[3] != "":
            arg_list_final[3] = float(arg_list[3])
        if n > 4 and arg_list[4] != "":
            arg_list_final[4] = int(arg_list[4])
        if n > 5 and arg_list[5] != "":
            arg_list_final[5] = int(arg_list[5])
        if n > 6 and arg_list[6] != "":
            func_str = arg_list[6]
            x = arg_list_final[4] if arg_list_final[4] is not None else arg_list_default[4]
            y = eval(func_str)

            if isinstance(y, float) == False and isinstance(y, int) == False:
                raise TypeError

            arg_list_final[6] = arg_list[6]
    except ValueError:
        print("Błąd w podanych argumentach")
        return
    except TypeError:
        print("Błąd w podanej funkcji")
        return
    except NameError:
        print("Błąd w podanej funkcji")
        return

    for i in range(len(arg_list_default)):
        if arg_list_final[i] is None:
            arg_list_final[i] = arg_list_default[i]

    generation_count = arg_list_final[0]
    population = Population(arg_list_final[5], arg_list_final[4], arg_list_final[6],
                            arg_list_final[2], arg_list_final[3], arg_list_final[1])

    best = []
    worst = []
    average = []
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
    plt.title("Przystosowanie osobników w kolejnych pokoleniach")
    plt.tight_layout()

    x = [i for i in range(Individual.min_val, Individual.max_val + 1)]
    y = [Individual.calc_fitness(x_val) for x_val in x]
    plt.figure(figsize=(14, 8), dpi=75)
    plt.plot(x, y, "o-")
    plt.xlabel("Wartość osobnika")
    plt.ylabel("Przystosowanie")
    plt.title("Przystosowanie dla kolejnych wartości osobników")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
