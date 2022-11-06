from typing import Callable
import matplotlib.pyplot as plt


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
    offset = 0 - min_val if min_val < 0 else 0
    bin_len = len(bin(max_val + offset)) - 2
    fitness_function = get_fitness_function("-0.1 * x**2 + 3 * x + 9")
    print(fitness_function(32))
    print(min_val, max_val, offset, bin_len, bin(max_val + offset))


if __name__ == "__main__":
    main()
