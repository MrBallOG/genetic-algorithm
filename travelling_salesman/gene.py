import math
from typing_extensions import Self


class Gene:
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.name}({self.x},{self.y})"

    def calc_distance(self, gene: Self) -> float:
        return math.sqrt((self.x - gene.x) ** 2 + (self.y - gene.y) ** 2)
