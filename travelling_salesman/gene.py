from math import sqrt
from typing_extensions import Self


class Gene:
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y

    @staticmethod
    def calc_distance(g1: Self,  g2: Self) -> float:
        return sqrt((g1.x - g2.x) ** 2 + (g1.y - g2.y) ** 2)
