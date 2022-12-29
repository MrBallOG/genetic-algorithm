import matplotlib.pyplot as plt
from individual import Individual
from population import Population
from gene import Gene
import re
import ast


def main() -> None:
    message = "Proszę podać argumenty oddzielone średnikiem w kolejności:\n"
    message += "-liczba pokoleń\n"
    message += "-liczba osobników w populacji\n"
    message += "-prawdopodobieństwo mutacji\n"
    message += "-współrzędne miast\n"
    message += "np.: 50;100;0.01;A(4,4), B(1,1), C(8,9), D(2,10), E(4,10), F(6,9), G(5,6), H(1, 8), I(8,7), J(9,4)\n"
    message += "Powyższy przykład przedstawia wartości domyślne\n"
    message += "Argumenty można zostawiać puste, z czego na końcu nie trzeba pamiętać o średnikach\n"
    message += "np.: 50;;0.01\n"

    arg_list_default = [
        50, 100, 0.01, "A(4,4), B(1,1), C(8,9), D(2,10), E(4,10), F(6,9), G(5,6), H(1, 8), I(8,7), J(9,4)"]
    arg_list_final = [None] * 4
    arg_str = input(message)
    arg_list = arg_str.split(";")
    n = len(arg_list)

    try:
        if n > 0 and arg_list[0] != "":
            arg_list_final[0] = int(arg_list[0])
    except ValueError:
        print("Błąd w liczbie pokoleń")
        return

    try:
        if n > 1 and arg_list[1] != "":
            arg_list_final[1] = int(arg_list[1])
    except ValueError:
        print("Błąd w liczbie osobników")
        return

    try:
        if n > 2 and arg_list[2] != "":
            arg_list_final[2] = float(arg_list[2])
    except ValueError:
        print("Błąd w prawdopodobieństwie mutacji")
        return

    try:
        if n > 3 and arg_list[3] != "":
            cities_str = arg_list[3]
        else:
            cities_str = arg_list_default[3]

        cities_str = cities_str.replace(" ", "")
        cities_list = re.split("(\(\d+,\d+\))", cities_str)
        cities_list = [elem.strip(",")
                       for elem in cities_list if elem != ""]

        if len(cities_list) % 2 != 0:
            raise ValueError

        default_chromosome = []

        while (len(cities_list) > 1):
            name = cities_list.pop(0)
            x, y = ast.literal_eval(cities_list.pop(0))
            x = int(x)
            y = int(y)
            gene = Gene(name, x, y)
            default_chromosome.append(gene)

        arg_list_final[3] = default_chromosome
    except (ValueError, SyntaxError):
        print("Błąd we współrzędnych miast")
        return

    for i in range(len(arg_list_default)):
        if arg_list_final[i] is None:
            arg_list_final[i] = arg_list_default[i]

    generation_count = arg_list_final[0]
    population = Population(
        arg_list_final[1], arg_list_final[2], arg_list_final[3])
    population.save_dist_and_individual_stats()

    for _ in range(generation_count - 1):
        population.select_using_roulette_selection()
        population.crossover()
        population.mutate()
        population.save_dist_and_individual_stats()

    best = population.best_dist_per_gen
    worst = population.worst_dist_per_gen
    average = population.average_dist_per_gen
    best_individual = population.min_path_individual
    worst_individual = population.max_path_individual

    x = [i + 1 for i in range(generation_count)]
    plt.figure(figsize=(14, 8), dpi=75)
    plt.plot(x, best, "o-", label="minimalna droga")
    plt.plot(x, average, "o-",  label="średnia droga")
    plt.plot(x, worst, "o-",  label="maksymalna droga")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel("Pokolenie")
    plt.ylabel("Długość")
    plt.title("Długość drogi w kolejnych pokoleniach")
    plt.tight_layout()

    x = [gene.x for gene in best_individual.chromosome]
    y = [gene.y for gene in best_individual.chromosome]
    annotations = [gene.name for gene in best_individual.chromosome]
    plt.figure(figsize=(14, 8), dpi=75)
    plt.plot(x, y, "o-")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(
        f"Najkrótsza droga {best_individual} o długości {best_individual.dist:.3f}")
    plt.grid(visible=True)
    plt.xlim(0, 11)
    plt.ylim(0, 11)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(range(11))
    ax.set_yticks(range(11))
    for i, annotation in enumerate(annotations):
        ax.annotate(annotation, (x[i], y[i]), bbox=dict(
            boxstyle='round,pad=0.5', fc='yellow'))
    plt.tight_layout()

    x = [gene.x for gene in worst_individual.chromosome]
    y = [gene.y for gene in worst_individual.chromosome]
    annotations = [gene.name for gene in worst_individual.chromosome]
    plt.figure(figsize=(14, 8), dpi=75)
    plt.plot(x, y, "o-")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(
        f"Najdłuższa droga {worst_individual} o długości {worst_individual.dist:.3f}")
    plt.grid(visible=True)
    plt.xlim(0, 11)
    plt.ylim(0, 11)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(range(11))
    ax.set_yticks(range(11))
    for i, annotation in enumerate(annotations):
        ax.annotate(annotation, (x[i], y[i]), bbox=dict(
            boxstyle='round,pad=0.5', fc='yellow'))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
