import matplotlib.pyplot as plt
from individual import Individual
from population import Population
from gene import Gene
import re
import ast

# x = [["A", 1, 2], ["B", 11, 4], ["C", 10, 5],
#      ["D", 3, 7], ["E", 4, 9], ["F", 5, 10]]
# y = [Gene(a[0], a[1], a[2]) for a in x]
# Individual.set_class_vars(y)
# print(Individual.dist_dict)
# i1 = Individual()
# i2 = Individual()


# def pch(i: List[Gene]):
#     text = ''
#     for j in range(len(i)):
#         text += i[j].name + "(" + str(i[j].x) + str(i[j].y) + ")"

#     print(text)


# pch(i1.chromosome)
# pch(i2.chromosome)
# i1, i2 = i1.crossover(i1, i2)
# print("mutacja")
# i2.mutate()
# pch(i2.chromosome)


def main() -> None:
    message = "Proszę podać argumenty oddzielone średnikiem w kolejności:\n"
    message += "-liczba pokoleń\n"
    message += "-liczba osobników w populacji\n"
    message += "-prawdopodobieństwo mutacji\n"
    message += "-współrzędne miast\n"
    message += "np.: 50;100;0.01;A(4,4), B(1,1), C(8,9), D(2,10), E(4,10), F(6,9), G(5,6), H(1, 8), I(8,7), J(9,4)\n"
    message += "Powyższy przykład przedstawia wartości domyślne\n"
    message += "Argumenty można zostawiać puste, z czego na końcu nie trzeba pamiętać o średnikach\n"
    message += "np.: 50;;0.5;0.01\n"

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

#     for i in range(len(arg_list_default)):
#         if arg_list_final[i] is None:
#             arg_list_final[i] = arg_list_default[i]

#     generation_count = arg_list_final[0]
#     population = Population(arg_list_final[5], arg_list_final[4], arg_list_final[6],
#                             arg_list_final[2], arg_list_final[3], arg_list_final[1])

#     best = []
#     worst = []
#     average = []
#     temp = population.get_max_min_avg_fitness()
#     best.append(temp[0])
#     worst.append(temp[1])
#     average.append(temp[2])

#     for _ in range(generation_count - 1):
#         population.select_using_roulette_selection()
#         population.crossover()
#         population.mutate()

#         temp = population.get_max_min_avg_fitness()
#         best.append(temp[0])
#         worst.append(temp[1])
#         average.append(temp[2])

#     x = [i + 1 for i in range(generation_count)]
#     plt.figure(figsize=(14, 8), dpi=75)
#     plt.plot(x, best, "o-", label="maksymalne przystosowanie")
#     plt.plot(x, average, "o-",  label="średnie przystosowanie")
#     plt.plot(x, worst, "o-",  label="minimalne przystosowanie")
#     plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#     plt.xlabel("Pokolenie")
#     plt.ylabel("Przystosowanie")
#     plt.title("Przystosowanie osobników w kolejnych pokoleniach")
#     plt.tight_layout()

#     x = [i for i in range(Individual.min_val, Individual.max_val + 1)]
#     y = [Individual.calc_fitness(x_val) for x_val in x]
#     plt.figure(figsize=(14, 8), dpi=75)
#     plt.plot(x, y, "o-")
#     plt.xlabel("Wartość osobnika")
#     plt.ylabel("Przystosowanie")
#     plt.title("Przystosowanie dla kolejnych wartości osobników")
#     plt.tight_layout()
#     plt.show()


if __name__ == "__main__":
    main()
